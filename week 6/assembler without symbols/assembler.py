import re 
f = open("RectL.asm",'r')
final_instruction=""
for line in f:
    if line.startswith("//") or line.startswith("\n") or line == '':
        continue
#inst=input('enter the instruction')
    else:
        #print(line)
        inst=line
        words=str(inst)
        b=list(words)
        c=[]
        a=['0']
        if b[0] == '@':
            for i in b:
                if i != '@':
                    c.append(i)
            s = [str(i) for i in c]
            res = int("".join(s))
            final_inst=format(res, "b").zfill(16)
            #print(final_inst)
            final_instruction += final_inst + "\n"
            
        else:
        #converting C instruction to binary
            word2=str(line)
            l=list(word2)
            kewk=[]
            for i in l:
                if i == "=":
                    break
                else:
                    kewk.append(i)
            dest = str("".join(kewk))
            dest_value=[]
            if dest == "M":
                dest_value=['001']
            elif dest == "D":
                dest_value=['010']
            elif dest == "MD":
                dest_value=['011']
            elif dest == "A":
                dest_value=['100']
            elif dest == "AM":
                dest_value=['101']
            elif dest == "AD":
                dest_value=['110']
            elif dest == "AMD":
                dest_value=['111']
            else:
                dest_value=['000']
            #print(dest_value)

            flag=0
            condi=False
            kewk2=[]
            for j in l:
                if j == "=":
                    flag=1
            if flag == 1:
                for j in l:
                    if j == ";" or j == "\n":
                        break
                    if condi:
                        kewk2.append(j)
                    elif j == '=':
                        condi=True
            else :
                for j in l:
                    if j == ";" or j == "\n":
                        break
                    if True:
                        kewk2.append(j)

            comp= str("".join(kewk2))
            #print(comp)
            a_bit=['0']
            comp_value=[]
            if comp == '0':
                comp_value=['101010']
            elif comp == '1':
                comp_value=['111111']
            elif comp == '-1':
                comp_value=['111010']
            elif comp == 'D' :
                comp_value=['001100']
            elif comp == 'A' or comp == 'M':
                comp_value=['110000']
                if comp == 'A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == '!D':
                comp_value=['001101']
            elif comp == '!A' or comp == '!M':
                comp_value=['110001']
                if comp == '!A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == '-D':
                comp_value=['001111']
            elif comp == '-A' or comp == '-M':
                comp_value=['110011']
                if comp == '-A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D+1':
                comp_value=['011111']
            elif comp == 'A+1' or comp == 'M+1':
                comp_value=['110111']
                if comp == 'A+1':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D-1':
                comp_value=['001110']
            elif comp == 'A-1' or comp == 'M-1':
                comp_value=['110010']
                if comp == 'A-1':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D+A' or comp == 'D+M':
                comp_value=['000010']
                if comp == 'D+A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D-A' or comp == 'D-M':
                comp_value=['010011']
                if comp == 'D-A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'A-D' or comp == 'M-D':
                comp_value=['000111']
                if comp == 'A-D':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D&A' or comp == 'D&M':
                comp_value=['000000']
                if comp == 'D&A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            elif comp == 'D|A' or comp == 'D|M':
                comp_value=['010101']
                if comp == 'D|A':
                    a_bit=['0']
                else:
                    a_bit=['1']
            #print(comp)
            # print(a_bit)
            #print(comp_value)

            condi2=False
            kewk3=[]
            for k in l:
                if k == ';':
                    condi2=True
                elif condi2:
                    kewk3.append(k)
            jump= str("".join(kewk3))
            jump_value=[]
            if jump == "JGT":
                jump_value=['001']
            elif jump == "JEQ":
                jump_value=['010']
            elif jump == "JGE":
                jump_value=['011']
            elif jump == "JLT":
                jump_value=['100']
            elif jump == "JNE":
                jump_value=['101']
            elif jump == "JLE":
                jump_value=['110']
            elif jump == "JMP":
                jump_value=['111']
            else :
                jump_value=['000']

            Cinst=['111']
            Final_instruct = Cinst+a_bit+comp_value+dest_value+jump_value
            finale_instu= str("".join(Final_instruct))
            #print(finale_instu)
            final_instruction += finale_instu + "\n"

#print(final_instruction)
with open('rectL.hack', 'w') as f:
    for Line in final_instruction:
        f.write(Line)
        
    
    
    




