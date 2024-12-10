''' COMPILER JAS'''
import sys
#read arguments
program_filepath = sys.argv[1]

print("[CMD] Parsing")

#Tokenize Program

#read file lines
program_lines =[]
with open (program_filepath, "r") as program_file:
    program_lines = [
        line.strip() 
            for line in program_file.readlines()]
program =[]
for line in program_lines:
    parts = line.split(" ")
    opcode = parts [0]
        
    #check for empty line
    if opcode == "":
        continue

    #store opcode token
    program.append(opcode)

    #handle each opcode
    if opcode == "PUSH":
        number = int(parts[1])
        program.append(number)
    elif opcode == "PRINT":
        #PARSE STRING LITERAL
        string_literal =''.join(parts[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0":
        #READ LABEL
        label = parts[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        #READ LABEL
        label = parts[1]
        program.append(label)

'''
Compile to assembly
'''

asm_filepath = program_filepath[:-4] + ".asm"
out =open(asm_filepath, "w")

out.write(""";-- header --
bits 64
default rel
""")         

out.write(""";-- variables --
section .bss
""")

out.write(""";-- contants --
section .data
""")

out.write(""";-- Entry Point--
section .text
global main
extern ExitProcess
extern printf
extern scanf
          

main:
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
""")

ip = 0
while ip < len(program):
    opcode = program[ip]
    ip += 1

    if opcode.endswith(":"):
        out.write(f";-- Label --\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip += 1

        out.write(f";-- PUSH --\n")
        out.write(f"\tPUSH {number}\n")
    elif opcode == "POP":
        out.write(f";-- POP --\n")
        out.write(f"\tPOP\n")


out.close()

