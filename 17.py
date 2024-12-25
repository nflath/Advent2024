registers = {}
ip = 0
instructions = []
import sys


for line in open("17.in").readlines():
    if "Register" in line:
        registers[line.split(":")[0][-1]] = int(line.split(":")[1])
        print(registers)
    if "Program" in line:
        instructions = [int(x) for x in line.split(":")[1].split(",")]
if len(sys.argv) > 1:
    registers["A"] = int(sys.argv[1])


def operand(op):
     if op <= 3:
         return op
     if op == 4:
         return registers["A"]
     if op == 5:
         return registers["B"]
     if op == 6:
         return registers["C"]
output = []

while ip < len(instructions):
            if instructions[ip] == 0:
                registers["A"] = int(registers["A"] / (2**operand(instructions[ip+1])))
                ip += 2
            elif instructions[ip] == 1:
                registers["B"] = registers["B"] ^ (instructions[ip+1])
                ip += 2
            elif instructions[ip] == 2:
                registers["B"] = (operand(instructions[ip+1])) % 8
                ip += 2
            elif instructions[ip] == 3:
                if registers["A"] == 0:
                    ip += 2
                else:
                    ip = instructions[ip+1]
            elif instructions[ip] == 4:
                registers["B"] = registers["B"] ^ registers["C"]
                ip += 2
            elif instructions[ip] == 5:
#                print(instructions[ip+1])
                output += [operand(instructions[ip+1]) % 8]
                ip += 2
            elif instructions[ip] == 6:
                registers["B"] = int(registers["A"] / (2**operand(instructions[ip+1])))
                ip += 2
            elif instructions[ip] == 7:
                registers["C"] = int(registers["A"] / (2**operand(instructions[ip+1])))
                ip += 2

print(",".join([str(x) for x in output]))
    
