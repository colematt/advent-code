#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()
import z3

testdata = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

def solveA(data:str) -> int:
    def get_goal(lights:str) -> tuple[bool,...]:
        return tuple(True if c == "#" else False for c in lights.strip("[]"))

    def get_buttons(diagrams:list[str], size:int) -> list[list[bool]]:
        buttons:list[list[bool]] = list()
        for diagram in diagrams:
            diagram = eval(diagram)
            b = [False for _ in range(size)]
            if type(diagram) == int:
                b[diagram] = True
                buttons.append(b)
            else:
                for idx in diagram:
                    b[idx] = True
                buttons.append(b)
        return buttons

    # Parse machines
    lines = [line.split() for line in data.splitlines()]
    machines = [(get_goal(line[0]), get_buttons(line[1:-1], len(line[0])-2)) for line in lines]
    counter:int = 0

    # Solve machines
    for i,machine in enumerate(machines):
        # Initialize machine
        goal, buttons = machine
        lights, count = tuple(False for _ in range(len(goal))), 0
        queue = [(lights, count)]
        history = {lights}
        
        # Solve machine
        while queue:
            lights, count = queue.pop(0)
            # Solution found, stop queue
            if lights == goal:
                counter += count
                break
            # Solution not found, add states from pressing each button to queue
            else:
                for button in buttons:
                    next = tuple(l1 ^ l2 for l1,l2 in zip(lights, button))
                    if next not in history:
                        queue.append((next,count+1))
                        history.add(next)
        # Solution found, add its count to the counter, 
        # iterate to next machine
        ic(i,counter)
    return counter


def solveB(data:str) -> int:
    def get_buttons(bstrs:list[str]) -> list[list[int]]:
        blist = list()
        for bstr in bstrs:
            if type(eval(bstr)) == int:
                blist.append([int(eval(bstr))])
            else:
                blist.append([int(b) for b in eval(bstr)])
        return blist

    def get_joltages(jolts:str) -> list[int]:
        return [int(j) for j in jolts.strip("{}").split(",")]

    # Parse machines
    lines = [line for line in data.splitlines()]
    machines = [(get_buttons(line.split()[1:-1]), get_joltages(line.split()[-1])) 
                for line in lines]
    ic(machines)
    answer:int = 0

    # Solve machines
    for i,machine in enumerate(machines):
        # Initialize machine
        buttons, joltages = machine
        bs = [z3.Int(f"b{i}") for i in range(len(buttons))]
        optimizer = z3.Optimize()

        # Add solution constraints
        optimizer.add(
            [
                z3.Sum(bs[b] for b, button in enumerate(buttons) if j in button)
                == joltage
                for (j, joltage) in enumerate(joltages)
            ]
        )
        optimizer.add([b >= 0 for b in bs])

        # Solve machine
        optimizer.minimize(z3.Sum(bs))
        ic(optimizer.check(), optimizer.model())
        assert optimizer.check() == z3.sat
        model = optimizer.model()
        answer += sum(model[b].as_long() for b in bs) # pyright: ignore[reportOptionalMemberAccess, reportAttributeAccessIssue]
        ic(i, answer)
    return answer


if __name__ == "__main__":
    assert solveA(testdata) == 7
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 33
    submit(str(solveB(data)), part='b')