import re

class Instruction:
    def __init__(self, text):
        match = re.match(r"(\w{3}) ([+-]\d+)", text)
        self.op = match.group(1)
        self.arg = int(match.group(2))
        self.visits = 0
        
    def __repr__(self):
        return f"{self.op} {self.arg}"
    def __str__(self):
        return self.__repr__()

example_data = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

with open("day08input.txt") as f:
    data = f.read()

#data = example_data

instructions = [Instruction(x) for x in data.splitlines()]

for edit_instruction in instructions:
    orig_op = edit_instruction.op
    if orig_op == "nop":
        edit_instruction.op = "jmp"
    elif orig_op == "jmp":
        edit_instruction.op = "nop"
    else:
        continue

    for x in instructions:
        x.visits = 0

    instruction_ptr = 0
    accumulator = 0

    while True:
        if instruction_ptr == len(instructions):
            break

        i = instructions[instruction_ptr]
        i.visits += 1
        if i.visits > 1:
            break
        if i.op == "nop":
            pass
        elif i.op == "acc":
            accumulator += i.arg
        elif i.op == "jmp":
            instruction_ptr += i.arg
            continue
        instruction_ptr += 1

    if instruction_ptr == len(instructions):
        print(instruction_ptr)
        print(accumulator)

    edit_instruction.op = orig_op
