import sys
from typing import List

def assemble(instruction: str) -> int:
    """
    Assembles a single instruction into an 8-bit machine code.
    
    For 'MEMSET', it returns a tuple (address, value) for direct memory setting.

    Parameters:
    instruction (str): The assembly instruction to compile.

    Returns:
    int or tuple: The compiled 8-bit machine code, or a tuple for 'MEMSET'.
    """
    op_codes = {
        'HLT': 0b0000 << 4,
        'ADD': 0b0001 << 4,
        'SUB': 0b0010 << 4,
        'LOAD': 0b0100 << 4,
        'STORE': 0b1000 << 4
    }

    parts = instruction.split()
    if parts[0].upper() == "MEMSET":
        address = int(parts[1])
        value = int(parts[2])
        return address, value
    
    op_code = op_codes[parts[0].upper()]
    
    if len(parts) > 1:
        argument = int(parts[1])
        return op_code | argument
    else:
        return op_code

def compile_program(assembly_code: List[str]) -> List[int]:
    """
    Compiles a list of assembly instructions into machine code.

    Parameters:
    assembly_code (List[str]): The list of assembly instructions.

    Returns:
    List[int]: The compiled list of machine code instructions.
    """
    machine_code = []
    memory_initialization = []

    for line in assembly_code:
        compiled = assemble(line)
        if isinstance(compiled, tuple):  # It's a MEMSET instruction
            memory_initialization.append(compiled)
        else:
            machine_code.append(compiled)
    
    return machine_code, memory_initialization

if len(sys.argv) < 3:
    print("Usage: python assembler.py <assembly_file> <output_file>")
    sys.exit(1)
    
assembly_code = []
with open(sys.argv[1], 'r') as assembly:
    assembly_code = assembly.readlines()

machine_code, memory_initialization = compile_program(assembly_code)

with open(sys.argv[2], 'w') as output:
    for address, value in memory_initialization:  # Write MEMSET instructions
        output.write(f"memory[{address}] = {value}\n")
        
    for address, code in enumerate(machine_code, start=100):  # Start storing at address 100
        output.write(f"memory[{address}] = 0b{code:08b}\n")
    