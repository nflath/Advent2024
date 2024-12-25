
import copy
import collections
registers_ = {}
ip = 0
instructions = []

for line in open("17.in").readlines():
    if "Register" in line:
        registers_[line.split(":")[0][-1]] = int(line.split(":")[1])
    if "Program" in line:
        instructions = [int(x) for x in line.split(":")[1].split(",")]
print(instructions)
def operand(op, registers):
     if op <= 3:
         return op
     if op == 4:
         return registers["A"]
     if op == 5:
         return registers["B"]
     if op == 6:
         return registers["C"]

output = []

def run(aval):
    registers = {
        "A" : aval,
        "B" : 0,
        "C" : 0}
    ip = 0
    output = []

    while ip < len(instructions):
            i = instructions[ip]
            o = instructions[ip+1]
            if instructions[ip] == 0:
                registers["A"] = int(registers["A"] / (2**operand(instructions[ip+1],registers)))
                ip += 2
            elif instructions[ip] == 1:
                registers["B"] = registers["B"] ^ (instructions[ip+1])
                ip += 2
            elif instructions[ip] == 2:
                registers["B"] = (operand(instructions[ip+1],registers)) % 8
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
                output += [operand(instructions[ip+1],registers) % 8]
                if output[-1] != instructions[len(output)-1]:
                    return False
                ip += 2
            elif instructions[ip] == 6:
                registers["B"] = int(registers["A"] / (2**operand(instructions[ip+1],registers)))
                ip += 2
            elif instructions[ip] == 7:
                registers["C"] = int(registers["A"] / (2**operand(instructions[ip+1],registers)))
                ip += 2
    return len(output) == len(instructions)

run(0b000001)

target_output = [2, 4,1]
m = None

def byt(a, i):
    return a[i] + (a[i+1] << 1) + (a[i+2] << 2)

for first_b in range(0,8):
#for first_b in [2]:
    output = []
    a = collections.defaultdict(int)
    a_idx = 0
    a[0] = first_b & 1
    a[1] = (first_b & 0b10) >> 1
    a[2] = (first_b & 0b100) >> 2
    output_idx = 0
    possible = True

    import pdb

    while output_idx < len(target_output):
       print("Target Output: ",target_output[output_idx],a_idx,a)
       # B = (A % 8) ^ 1
       b = (byt(a,a_idx) ^ 0b001)
       c_idx = a_idx + b
       b = b ^ 5
       for i in range(0, 3):
           if (c_idx+i) in a and a[c_idx+i] != ((target_output[output_idx] ^ b) & (1 << i)):
               possible = False
               break
           assert (((target_output[output_idx] ^ b) & (1 << i)) >> i) < 7
           a[c_idx + i] =  (((target_output[output_idx] ^ b) & (1 << i)) >> i)

       if not possible:
           print("Not possible, first_b")
           break
           
#       a[c_idx] = (target_output[output_idx] ^ b)
       b = b ^ byt(a,c_idx)
       output += [b % 8]
       output_idx += 1
       a_idx += 3
    
    
#   
    av = 0
#    print('b:',first_b, a)


    av = 0
    if possible and output == target_output:
        max_i = 0
        for i in a:
            max_i = max(i,max_i)
        for i in range(0, max_i+1):
            av += (a[i] << (i))
    if possible and not m:
        m = av
        if m == 0: print("ERROR", first_b)
    elif possible:
            m = min(m, av)
    if possible: print(first_b, possible, m, av,a)
#    exit()


print(m)

# Too high: 8379113107110109067862007130317757681303556
    
    






#aval = 0
#while not run(aval):
#    if(aval % 100000) == 0: print(aval)
#    aval += 1
#print(aval, output)
    
