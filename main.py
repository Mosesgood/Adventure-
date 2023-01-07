ans = input("let play a game (y/n)")
if ans.lower().strip() == "y":
   ans = input("left door or right door (l/r)").lower().strip()
   if ans == "l":
        ans = input("you enter, blue door or red door (b/r)")

        if ans == "b":
            print("blue door")

   elif ans == "r":
        ans = input("you enter, green door or black door (g/b)")

        if ans == "g":
            print("green door")

            ans = input("you enter the green door, (a,b)")

            if ans == "a":
                print("you lost")


        else:
            print("black door")

else:
   print("End Game")
