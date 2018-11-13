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
"""Converts elevations into RGB scale 0-255."""


height = len(elevation_to_colors)
width = len(elevation_to_colors[0])
img = Image.new('RGB', (height, width))
"""Image dimensions are height (# of lists), and width (# of rows, shown by [0])."""

for y, row in enumerate(elevation_to_colors):
    for x, num in enumerate(row):
        img.putpixel((x, y), (num, num, num))


img.save('steve_pathfinder_map.png')
"""steve_pathfinder_map.png is operational!"""


def Y():
    for y, row in enumerate(elevation_to_colors):
        if abs(y - (y+1)) < y:
            return (y+1)
        elif abs(y - (y-1)) < y:
            return (y-1)
        elif abs(y - y) < (y+1):
            return y
        elif abs((y+1) - (y-1)) < y:
            return ((y+1) or (y-1)).random


# ImageDraw Attempt -- To do this, import ImageDraw above
# im = Image.open('steve_pathfinder_map.png')
# draw = ImageDraw.Draw(im)
# draw.line((0, 300), ((x+1), Y), fill=128)
# im.show()
# im.save('steve_pathfinder_map_RED_LINE.png')

# THIS GIVES A STRAIGHT LINE ACROSS! However when I try to take the function "Y" and stick it in the 2nd position for draw.line coordinates, the instrucitons are being met with error message:  
# "Traceback (most recent call last):
#   File "pathfinder.py", line 51, in <module>
#     draw.line((0, 300), ((x+1), Y), fill=None)
# TypeError: line() got multiple values for argument 'fill'"


# putpixel Attempt
im = Image.open('steve_pathfinder_map.png')
im.putpixel((x+1), Y), (255, 0, 0)
im.show()
im.save('steve_pathfinder_map_RED_LINE.png')
