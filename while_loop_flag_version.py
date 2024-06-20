def get_starting_number():
    num = int(input("How many bottles of beer on the wall? "))
    if num >= 1:
        return num
    else:
        print("Please enter a number 1 or greater.")

def sing(bottles):
    current_bottles = bottles
    flag = True
    while flag:
        if current_bottles == 0:
            flag = False
            print("No more bottles of beer on the wall!")
        elif current_bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            flag = False
        elif current_bottles == 2:
            print(f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer.")
            print(f"Take one down, pass it around, {current_bottles - 1} bottle of beer on the wall.")
            current_bottles -= 1
        else:
            print(f"{current_bottles} bottles of beer on the wall, {current_bottles} bottles of beer.")
            print(f"Take one down, pass it around, {current_bottles - 1} bottles of beer on the wall.")
            current_bottles -= 1
