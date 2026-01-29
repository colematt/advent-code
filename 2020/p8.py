#!/usr/bin/python3

from aocd import data, submit
from icecream import ic

testdata = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def run(program,acc=0,pc=0) -> tuple[int,int]:
    """
    {Execute a program with initialized values, until a cycle is encountered or
    the program terminates. Return the final accumulator and pc values.}
    
    :param      program:     The program instruction stream
    :type       program:     {list[str]}
    :param      acc:         The accumulator initial value
    :type       acc:         int
    :param      pc:          The program counter initial value
    :type       pc:          int
    
    :returns:   { Final program state (acc,pc) }
    :rtype:     { tuple }
    
    :raises     ValueError:  { Raises exception if an unidentified opcode is encountered }
    """
    unvisited = set(program)
    
    # While loop checks to make sure we aren't beginning a cycle
    # or that the program has terminated (ie. pc is out of bounds)
    while pc < len(program) and program[pc] in unvisited:
        address,(opcode,operand) = program[pc]
        operand = int(operand)
        unvisited.remove(program[pc])

        # Execute the instruction
        if opcode == 'acc':
            acc += operand
            pc += 1
        elif opcode == 'jmp':
            pc += operand
        elif opcode == 'nop':
            pc += 1
        else:
            raise ValueError("Unrecognized opcode %s" % opcode)

    # Return a 2-tuple of the final accumulator value and program counter value
    return acc,pc


def debug(program,acc=0,pc=0) -> tuple[int,int]:
    """
    { For each instruction in a program, try permuting its opcode to see if 
      infinite loops can be resolved. If so, return the final accumulator and 
      program counter value when the loop is fixed. Otherwise, return None. }

    :param      program:  The program
    :type       program:  { type_description }
    :param      acc:      The acc
    :type       acc:      number
    :param      pc:       { parameter_description }
    :type       pc:       number

    :returns:   Final program state or None
    :rtype:     { {tuple, None} }
    """

    # For each address, permute if a 'jmp' or 'nop',
    # then run the program. If it halts properly, report the accumulator
    for addr in range(len(program)):
        # Fetch the instruction to be permuted
        inst = program[addr]
        address,(opcode,operand) = inst
        
        # Permute the instruction if needed
        if opcode == 'jmp':
            opcode = 'nop'
            program[addr] = (address,(opcode,operand))
        elif opcode == 'nop':
            opcode = 'jmp'
            program[addr] = (address,(opcode,operand))
        else:
            pass

        # Execute the program
        acc,pc = run(program)

        # Report if fixed, restore otherwise
        if pc >= len(program):
            break
        else: 
            program[addr] = inst
    if pc >= len(program):
        return acc,pc
    else:
        raise Exception("Program could not be fixed!")


def printState(program,state):
    """
    Pretty prints a program state.

    :param      program:  The program
    :type       program:  { list[str] }
    :param      state:    Program state to be unpacked
    :type       state:    { tuple }
    """
    try:
        print("acc: %i, pc: %i is %s" % (*state,repr(program[state[1]])))
    except IndexError:
        print("acc: %i, pc: %i Terminated" % (state))


def solveA(data:str) -> int:
    program = list(enumerate(tuple(line.split()) for line in data.splitlines()))
    acc, pc = run(program)
    return acc


def solveB(data:str) -> int:
    program = list(enumerate(tuple(line.split()) for line in data.splitlines()))
    acc, pc = debug(program)
    return acc


if __name__ == "__main__":
    assert solveA(testdata) == 5
    submit(str(solveA(data)), part='a')
    assert(solveB(testdata) == 8)
    submit(str(solveB(data)), part='b')
