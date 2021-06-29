// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@24576 
D=A 
@key 
M=D
@i 
M=0


(ACT)
    @i
    M=0
    @SCREEN 
    D=A 
    @addr
    M=D 

    @key 
    D=M
    @PRESS
    D;JEQ 
    @NOPRESS
    D;JNE
    @ACT
    0;JMP
    



(NOPRESS)
    @i 
    D=M 
    @8191
    D=D-A 
    @ACT 
    D;JEQ

    @addr 
    A=M 
    M=0 
    
    @i 
    M=M+1
    @1
    D=A 
    @addr 
    M=D+M
    @NOPRESS
    0;JMP
    
(PRESS) 
    @i 
    D=M 
    @8191
    D=D-A 
    @ACT 
    D;JEQ

    @addr 
    A=M 
    M=-1 
    
    @i 
    M=M+1
    @1
    D=A 
    @addr 
    M=D+M
    @PRESS
    0;JMP
    



