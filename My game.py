
try:
    nums = int(input("Enert your lucky number within ten"))

    if nums is 1:
        print("You are lucky")
    if nums is 2:
        print("You are fucked off")
    if nums is 3:
        print("You are crazy")
    if nums is 4:
        print("You are amazing")
    if nums is 5:
        print("You are lazy")
    if nums is 6:
        print("You ill get one more chance")
    if nums is 7:
        print("You need to drive a lorry")
    if nums is 8:
        print("you have to swim in the floor")
    if nums is 9:
        print("You have to cut your finger")
    if nums is 10:
        print("You hace to love someone")

    if nums >=10:
        print("enter value within ten")

except ValueError as e:
    print("hey dood need only numeric numers", e)
finally:
    print("Game Over")