def move_north(location):
    location[1] += 1
    return location
def move_south(location):
    location[1] -= 1
    return location
def move_east(location):
    location[0] += 1
    return location
def move_west(location):
    location[0] -= 1
    return location

def stay(location):
    return location

def direction(input, location):
    if input == "n":
        move_north(location)
    elif input == "s":
        move_south(location)
    elif input == "e":
        move_east(location)
    elif input == "w":
        move_west(location)

def travel(location):
    if location == [1,1] or location == [2,1]:
        print("You can travel: (N)orth.")
        input_travel = input("Direction: ")
        if input_travel == "n":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [1,2]:
        print("You can travel: (N)orth or (S)outh or (E)ast")
        input_travel = input("Direction: ")
        if input_travel == "n" or input_travel == "s" or input_travel == "e":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [1,3]:
        print("You can travel: (E)ast or (S)outh")
        input_travel = input("Direction: ")
        if input_travel == "e" or input_travel == "s":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [2,3]:
        print("You can travel: (E)ast or (W)est")
        input_travel = input("Direction: ")
        if input_travel == "e" or input_travel == "w":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [2,2] or location == [3,3]:
        print("You can travel: (S)outh or (W)est")
        input_travel = input("Direction: ")
        if input_travel == "s" or input_travel == "w":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [3,2]:
        print("You can travel: (N)orth or (S)outh")
        input_travel = input("Direction: ")
        if input_travel == "n" or input_travel == "s":
            direction(input_travel, location)
        else:
            print("Not a valid direction!")
    elif location == [3,1]:
        print("Victory!")



def main():
    location = [1,1]
    running = True
    while running:
        travel(location)
        print(location)
        if location == [3,1]:
            running = False
            print("Victory!")


if __name__ == "__main__":
    main()
