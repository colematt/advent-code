#!/usr/bin/env python3

from aocd import data, submit
from ast import literal_eval

def solveA(data:str) -> int | None:
    lines = tuple(line for line in data.splitlines())
    rawlens = tuple(len(s) for s in lines)
    evallens = tuple(len(literal_eval(s)) for s in lines if len(s.strip()) > 0)
    return sum(rawlens) - sum(evallens)


def solveB(data:str) -> int:
    rawlens = tuple(len(s) for s in data.split("\n"))
    quotelens = tuple(len('"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"')
                    for s in data.split("\n") if len(s) > 0)
    return sum(quotelens) - sum(rawlens)


if __name__ == "__main__":
    submit(str(solveA(data)), part='a')
    submit(str(solveB(data)), part='b')