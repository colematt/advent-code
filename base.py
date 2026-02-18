from aocd import data, submit
from aocd.examples import Example
from aocd.models import Puzzle
from icecream import ic

def get_example(year:None|int=None, day:None|int=None, part:None|str=None) -> str:
    if not year:
        year = 2020
    if not day:
        day = 1
    if not part:
        part = "a"

    try:
        if len(Puzzle(year=year,day=day).examples) == 1 or part == None:
            return Puzzle(year=year,day=day).examples[0].__getattribute__("input_data")
        else:    
            if part.casefold == "a":
                return Puzzle(year=year,day=day).examples[0].__getattribute__("input_data")
            elif part.casefold == "b":
                return Puzzle(year=year,day=day).examples[1].__getattribute__("input_data")
            else:
                raise ValueError("Unrecognized part: %s", part)
    except:
        pass
