import math

def paint_calc():
    # ask user for height, width, and coverage of wall
    wall_height = int(input("What is the height of the wall? "))
    wall_width = int(input("What is the width of the wall? "))
    can_coverage = int(input("What is the coverage size? "))

    # calculate number of cans
    num_cans = (wall_height * wall_width) / can_coverage
    round_up_cans = math.ceil(num_cans)
    print(f"You will need {round_up_cans} cans to paint your wall.")

paint_calc()

