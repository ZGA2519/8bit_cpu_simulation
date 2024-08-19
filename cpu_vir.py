import sys
from typing import List
"""
    8 bit intruction set
    4 bit opcode
    4 bit operand
    HLT   [address] --> 0000_[address]
    ADD   [address] --> 0001_[address]
    SUB   [address] --> 0010_[address]
    LOAD  [address] --> 0100_[address]
    STORE [address] --> 1000_[address]
"""

control_unit:     int = 0
accumulator_unit: int = 0
alu:              int = 0  # Arithmetic and Logical Unit

memory: List[int] = [0b0000_0000] * 255 # Main Memory

pc:  int = 100             # Program Counter start at 100
cir: int = 0               # Current Instruction Register
mar: int = 0               # Memory Address Register
mdr: int = 0               # Memory Data Register

def print_memory(op: str) -> str:
    def format(num: int) -> str:
        binary = f"{num:08b}"
        return binary[:4] + '_' + binary[4:]
    print(f"\n######################### {op.upper()} #################################\n")
    print(f"{pc=} \t\t\tcontrol_unit={format(control_unit)}")
    print(f"cir={format(cir)}\t\t{accumulator_unit=}")
    print(f"{mar=}\t\t\t{alu=}")
    print(f"mdr={format(mdr)}")
    print("Memory usage")
    print("-------------------\t--------------------------")
    for data1, data2 in zip(enumerate(memory[:16]), enumerate(memory[100:116])):
        print(f"| {data1[0]} \t| {data1[1]}\t |\t| {data2[0]+100} {'*' if data2[0]+100 == pc else ''}\t|\t{format(data2[1])} |")
    print("-------------------\t--------------------------")

# Add your code here
if len(sys.argv) < 2:
    print("Usage: python cpu_vir.py <filename>")
    sys.exit(1)
    
with open(sys.argv[1], 'r') as file:
    for line in file:
        exec(line.strip()) # Load program into memory
    
    
print_memory("Starting CPU")
if input("Enter to next intruction block or enter `q` to quit.").lower() == 'q': exit()

while True:
    
    # Fetch
    mar = pc
    mdr = memory[mar]
    cir = mdr
    pc += 1
    print_memory("fetch")
    if input("Enter to next intruction block or enter `q` to quit.").lower() == 'q': break
    
    # Decode
    control_unit = cir
    opcode     = (control_unit >> 4) & 0b1111
    operand   = control_unit & 0b1111
    print_memory('Decode')
    if input("Enter to next intruction block or enter `q` to quit.").lower() == 'q': break
    
    # Execute 
    """
    HLT   0000 0000
    ADD   0001 0000
    SUB   0010 0000
    LOAD  0100 0000
    STORE 1000 0000
    """
    if opcode == 0b0000:            # Halt 
        print_memory('Execute')
        break
    
    elif opcode == 0b0001:          # Add operation
        mar = operand
        mdr = memory[mar]
        alu = accumulator_unit
        accumulator_unit = mdr
        alu = alu + accumulator_unit
        accumulator_unit = alu
        
    elif opcode == 0b0010:         # Sub operation
        mar = operand
        mdr = memory[mar]
        alu = accumulator_unit
        accumulator_unit = mdr
        alu = alu - accumulator_unit
        accumulator_unit = alu
        
    elif opcode == 0b0100:         # Load operation
        mar = operand
        mdr = memory[mar]
        accumulator_unit = mdr
        
    elif opcode == 0b1000:         # Store operation
        mar = operand
        mdr = accumulator_unit 
        memory[mar] = mdr
        
    print_memory('Execute')  
    if input("Enter to next intruction block or enter `q` to quit.").lower() == 'q': break
    
    