import numpy as np
from common_methods import is_solved, make_grid_from_string
from complex_solver import complex_method
from simple_solver import simple_method

unsolved_str_1 = '050000190000000042910027568345001906700340000890206003008700210160008004000100685'  # easy
unsolved_str_2 = '000940000008070100069020005450600008036805020082000000004280003010000057000001980'  # medium
unsolved_str_3 = '600500100800004360300900000100080200000000000050400600070200400010009002000000093'  # hard

unsolved = make_grid_from_string(unsolved_str_2)
print("unsolved-")
print(unsolved)
print("solving...")
solved = simple_method(unsolved)
if is_solved(solved):
    print(solved)
else:
    print("simple method did not work")
    print("using complex method")
    complex_method(solved)

# TODO Complex sudoku solver
#   if the simple solver doesn't work
#   find the squares with minimum number of ones
#   then check which of these can be filled to maximise certainty:
#       filling this number should:
#           reduce the most number of ones in the rest of the grid.
#   then do the simple solve.
#   if it doesnt work, try another one.
#   if none of them work, then we need to go two levels deep...


# TODO
#   what do i want in my linked list?
#       an array of 9 linked lists
#       for a linked list i should be able to
#       add an element
#       iterate over it
