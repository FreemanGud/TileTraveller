def check_victory(location):
    if location == [3, 3]:
        victory = True
    return victory

def move_north(location):
    location[1] +=1
    return location

def move_east(location):
    location[0] +=1
    return location

def move_south(location):
    location[1] -=1
    return location

def move_west(location):
    location[0] -=1
    return location

def move(movement, location):
    if movement == "n" or "N":
        move_north(location)
    elif movement == "e" or movement == "E":
        move_east(location)
    elif movement == "s" or movement == "S":
        move_east(location)
    elif movement == "w" or movement == "W":
        move_east(location)
    else:
        print("Not a valid direction!")
    return location
    
def main():
    travel_text = f'You can travel: '
    location = [1, 1]
    running = True
    while running == True:
        if location == [1, 1] or location == [2,1]:
            print(travel_text, "north")
            movement = input("Direction: ")
            move(movement, location)
        # elif location == []
        # movement = input("Direction: ")

if __name__ == '__main__':
    main()