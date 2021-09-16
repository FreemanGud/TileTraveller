
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
    if movement == "n" or movement == "N":
        move_north(location)
    elif movement == "e" or movement == "E":
        move_east(location)
    elif movement == "s" or movement == "S":
        move_south(location)
    elif movement == "w" or movement == "W":
        move_west(location)
    else:
        print("Not a valid direction!")
    return location

def local(location):
    print(location)
    return location

def travel(location):
    travel_text = f'You can travel: '
    if location == [1,1] or location ==[2, 1]:
        print(travel_text, "(N)orth")
        movement = input("Direction:")
        if movement == "n" or movement =="N":
            move(movement, location)
            
        else:
            print("Invalid direction!")

    elif location == [1,2]:
        print(travel_text, "(N)orth or (E)ast or (S)outh")
        movement = input("Direction:")
        if movement == "n" or movement == "N" or movement == "e" or movement == "E" or movement == "s" or movement == "S" :
            move(movement, location)
            
        else:
            print("Invalid direction!")
    
    elif location == [1,3]:
        print(travel_text, "(E)ast or (S)outh")
        movement = input("Direction:")
        if movement == "e" or movement == "E" or movement == "s" or movement == "S" :
            move(movement, location)
            
        else:
            print("Invalid direction!")
    
    elif location == [2,2]:
        print(travel_text, "(S)outh or (West)")
        movement = input("Direction:")
        if movement == "s" or movement == "S" or movement == "w" or movement == "W" :
            move(movement, location)
            
        else:
            print("Invalid direction!")
        
    elif location == [2,3]:
        print(travel_text, "(E)ast or (West)")
        movement = input("Direction:")
        if movement == "e" or movement == "E" or movement == "w" or movement == "W" :
            move(movement, location)
            
        else:
            print("Invalid direction!")

    elif location == [3,3]:
        print(travel_text, "(S)outh or (West)")
        movement = input("Direction:")
        if movement == "s" or movement == "S" or movement == "w" or movement == "W" :
            move(movement, location)
            
        else:
            print("Invalid direction!")

    elif location == [3,2]:
        print(travel_text, "(N)orth or (S)outh")
        movement = input("Direction:")
        if movement == "n" or movement == "N" or movement == "s" or movement == "S":
            move(movement, location)
            
        else:
            print("Invalid direction!")


        
    return movement, location


    

def main():
    travel_text = f'You can travel: '
    location = [1, 1]
    running = True
    while location != [3, 1]:
        # local(location)
        travel(location)
    print("Victory!")
        




if __name__ == '__main__':
    main()