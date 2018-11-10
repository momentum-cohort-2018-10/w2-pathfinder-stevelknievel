# BEGIN TEST FILE NOTES:
# from pathfinder  import ElevationMap, pathfinder

# def test_print_one_elevation():
#     print(elevations[0][1])

# def test_dimensions_of_elevation_list():
#   print(len(elevation_list))
#   print(len(elevation_list[0]))

# def test_elevations_list_list_comprehension():
#   print(elevation_list[0][2])

# def test_max_elevation_list():
#   print(max(elevation_list))

# def test_min_elevation_list():
#   print(min(elevation_list))

# def test_min_height_from_whole_txt_file():
#   print(min(elevation_list))

# def test_max_height_from_whole_txt_file():
#   print(max(elevation_list))

# def test_elevation_to_colors_formula(number):
#   print(elevation_to_colors_formula(5500))


# row = data[0]
# for index in range(len(row)):
#     print(index(row))



# will give us both index and number in the data
# puts data from file and puts them into pixels:

# for y, row in enumerate(data):
#     for x, num in enumerate(row):
#         img.putpixel((x, y), (num, num, num))

# img.save('text.png')


# x = how many items in row
# y = how many rows in list

# find the maximum elevation in the data and use that as the top, find the lowest and use as bottom, and then scale.  Take elevation, .... watch Clinton video with more talking about this.

# have to remember the index and value of each coordinate at the same time.

# start small, start with your data looking something like this:
# [[1,2,1], [2,3,2], [1,1,3]]

# PYTHON BUILT IN FUNCTION ABS (absolute value)

# Really good option: use a dictionary or a list of tuples.  once you do that, it comes down to update the current place (by minimum absolute value)

#how to get whereto go tothenext spot: 
# int((current elevation divided by max elevation) * 255)



# list(enumerate(["a", "b", "c"]))
# gives us:
# [(0, 'a')]