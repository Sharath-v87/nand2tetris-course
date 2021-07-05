#Final fully functioning hack assembler
from instruction import *
from symboltable import *

symbol=Symboltable()
f = open("Pong.asm",'r')
paranvar=''
labels={}
labaddr=0
final_instruction=""
varlabels={}
varadd=16
for line in f :
    if line.startswith("//") or line.startswith("\n") or line == '':
        continue
    if paranvar in labels:
        pass
    elif paranvar not in labels:
        labels[paranvar]=labaddr
    line=line.replace("\n","")
    line=line.strip()
    if line.startswith("(") :
        #print(line)
        line=line.lstrip("(")
        line=line.rstrip(")")
        paranvar=line
        #print(paranvar)
        continue
    labaddr+=1
#print(labels)
f.seek(0)
for l in f:
    #print(l)
    l=l.rstrip()
    l=l.lstrip()
    l=l.replace("\n","")
    pp=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
    if l.startswith("//") or l.startswith("\n") or l == '':
        continue
    if "//" in l:
        l=l.split('//')[0]
        l=l.strip()
    if l.startswith("@"):
        #print(l)
        if l[1] == "R" and l[2] in pp:
            final_instA=symbol.reg_symbols(l[1:])
            final_instruction+=final_instA+"\n"
            #print(l[1])
        elif l[1:] == "SCREEN" or l[1:] == "KBD" or l[1:] == "SP" or l[1:] == "LCL" or l[1:] == "ARG" or l[1:] == "THIS" or l[1:] == "THAT" :
            final_instA=symbol.predefined_symbols(l[1:])
            final_instruction+=final_instA+"\n"
            #print(l[1:])
        elif l[1:] in labels :
            p=labels[l[1:]]
            #print(final_instA)
            final_instA=format(p, "b").zfill(16)
            final_instruction+=final_instA+"\n"
            #print(labels)
            #print(l[1:])
        elif l[1:] in varlabels:
            final_instA=varlabels[l[1:]]
            final_instruction += final_instA + "\n" 
        # elif type(l[1:]) == str:
        #     varlabels[varadd]=l[1:]
        #     varadd += 1
        #     print(varlabels)
        else:
            try:
                if type(int(l[1:])) == int:
                    if int(l[1:]) < 16:
                        m="R"+l[1:]
                        final_instA=symbol.reg_symbols(m)
                        final_instruction += final_instA + "\n" 
                        #print(final_instA)
                    else :
                        final_instA=format(int(l[1:]), "b").zfill(16)
                        final_instruction += final_instA + "\n" 
            except:
                if l[1:] not in varlabels:
                    lol=format(varadd, "b").zfill(16)
                    varlabels[l[1:]]=lol
                    varadd += 1
                    #print(varlabels)
                    final_instA=varlabels[l[1:]]
                    final_instruction += final_instA + "\n" 

    else:
        if l.startswith("("):
            continue
        
        else:
            #print(l)
            final_cinstruction=instruction_translate(l)
            #print(final_cinstruction)
            final_instruction += final_cinstruction + "\n"
#print(final_instruction)
with open('pong.hack', 'w') as f:
    for Line in final_instruction:
        f.write(Line)