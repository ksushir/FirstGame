print("Welcome to my game!")
name = input("What is your name?")
age = int(input("What is your age?"))

print("Hello", name, "you age", age, "years old.")

health = 10

print("You are staring with", health, "health")

if age >= 18:
    print("You are old enought!")

    wants_to_play = input("Do you want to play?").lower()
    if wants_to_play == "yes":
        print("Lets play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input(
                "Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print(
                    "You managed to ger across, but were bit by a fish and lost 5 health")
                health -= 5

            ans = input(
                "You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print(
                    "You go to the house and are greted by the owner... He doesnt like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health, and you lose the game...")
                else:
                    print("You have survied.. You win!")
            else:
                print("You feel in the river and lost...")

        else:
            print("You feel down and lose")

    else:
        print("Cya...")

else:
    print("You are not old enought to play...")
