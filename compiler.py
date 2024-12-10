''' COMPILER JAS'''
import sys
#read arguments
program_filepath = sys.argv[1]

print(program_filepath)

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

print(program)