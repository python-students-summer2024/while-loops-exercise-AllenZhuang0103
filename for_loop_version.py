def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit():
            num = int(num)
            if num >= 1:
                return num
            else:
                print("Please enter a number 1 or greater.")
        else:
            print("Please enter a valid integer.")

def sing(bottles):
    for i in range(bottles, 0, -1):
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle of beer on the wall.\n")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")

# num_bottles = get_starting_number()
# sing(num_bottles)