#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic

type shape = list[str]
type region = tuple[int,int,list[int]]

testdata = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

def parse(data:str) -> tuple[list[shape],list[region]]:
    # Parse input data
    sections = list(data.split("\n\n"))
    shapestrs, regionstrs  = sections[:-1], sections[-1]

    shapes:list[shape] = list()
    for shapestr in shapestrs:
        shapes.append([row for row in shapestr.split("\n")[1:]])
        
    regions:list[region] = list()
    for regionstr in regionstrs.split('\n')[:-1]:
        dimensions, *counts = regionstr.split()
        width,length = (int(d) for d in dimensions.rstrip(':').split('x'))
        counts = [int(i) for i in counts]
        regions.append((width,length,counts))

    return shapes, regions


def solveA(data:str) -> int | None:
    # Get puzzle input
    shapes, regions = parse(data)

    # Get number of tiles in each shape and shape dimensions
    shape_num_tiles: list[int] = [sum(row.count('#') for row in shape) 
                                  for shape in shapes]
    shape_max_length = max(len(shape) for shape in shapes)
    shape_max_width = max(max(len(shape[row]) for row in range(len(shape))) 
                          for shape in shapes)
    
    # Do oracle of fitness tests:
    # 1) #shapes < (region #rows // shape rows) * (region #cols // shape cols)
    # 2) #shapes' tiles < region area
    answer = 0
    hard = 0
    for region in regions:
        width,length,counts = region

        # Get max presents lower bound (assumes no interlocking)
        # If the number of presents to pack is smaller than the lower bound,
        # add to answer tally and continue
        max_presents_lower_bound = ((length // shape_max_length) 
                                    * (width // shape_max_width))
        if max_presents_lower_bound > sum(counts):
            answer += 1
            continue

        # If the presents' tile count sum is greater than the total area,
        # there is no way to pack into the region
        shape_tile_count = sum(x*y for x,y in zip(shape_num_tiles, counts))
        region_num_tiles = width * length
        if region_num_tiles < shape_tile_count:
            continue

        # HACK: We need to do NP-complete packing :(
        hard += 1
        ic(region, hard)

    ic(len(regions))
    return answer

if __name__ == "__main__":
    #solveA(testdata)
    submit(str(solveA(data)), part='a')
    # assert solveA(testdata) == 2