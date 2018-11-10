from PIL import Image 

# Get Object Orientational: convert this entire thing into classes and methods. 
# Potential classes: FILE_OPEN_AND_CLEAN, ELEVATION_OPERATIONS, MAP CREATION, and more

with open('elevation_small.txt', 'r') as data_file:
    elevations = [line.strip('\n').split() for line in data_file]
    """opens, cleans txt file and new name"""

elevation_list = [[int(elevation) for elevation in row] for row in elevations]
"""makes each item in each list an integer"""


min_height = (min(min(elevation_list)))
max_height = (max(max(elevation_list)))
"""max and min elevations in each list"""


elevation_to_colors = [[abs(round((each - min_height)/(max_height - min_height)*255)) for each in elevations] for elevations in elevation_list]
"""Converts elevations into RGB scale 0-255 through every elevation in every list in larger list of lists. Notes to Steve: Abs is for absolute value, and is used bc this was returning negative values.  round is to ensure even intgers and not decimals.  Need to work on List Comprehensions.  These are so powerful, but this took me FOREVER!"""


height = len(elevation_to_colors)
width = len(elevation_to_colors[0])
img = Image.new('RGB', (height, width))
"""Image dimensions are height - # of lists, and width - # of rows, shown by [0]"""

for y, row in enumerate(elevation_to_colors):
    for x, num in enumerate(row):
        img.putpixel((x, y), (num, num, num))

img.save('steve_pathfinder_map.png')

"""steve_pathfinder_map.png is operational!  Need to start plotting that course now."""


