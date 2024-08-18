# 8-bit CPU Simulation
8-bit CPU Simulation using von Neumann Architecture <br> 
For this instruction, 8 bits are separated by a set of 4-bit op code and 4-bit operand.

## Code 1 line per instruction

```HLT```                        Halt process <br> 
```ADD   [address]```            Add value of [address] to accumulater <br> 
```SUB   [address]```            Sub value of [address] to accumulate <br> 
```LOAD  [address]```            Load value from [address] to accumulater <br> 
```STORE [address]```            Store value of to accumulater to [address] <br> 
```MEMSET [address] [valuse]```  Set value of [address] to [value] <br> 

## Usage 

compile to machine code
```
    python asm_compiler.py <input> <output>
```

run
```
    python cpu_vir.py <machine_code>
