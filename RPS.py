import random
win = 0
loss = 0

while True:
    num = random.randrange(1, 4, 1)
    user = int(input("Please pick one of the folowing!\n1. Rock\n2. Paper\n3. Scissors\n--------------"))
    choice = {1:"Rock", 2:"Paper", 3:"Scissors"}
    x = "null"

    if user == 1 and num == 1:
      x = "TIED"
    elif user == 1 and num == 2:
      x = "LOST"
      loss += 1
    elif user == 1 and num == 3:
      x ="WON"
      win += 1
    elif user == 2 and num == 1:
      x = "WON"
      win += 1
    elif user == 2 and num == 2:
      x = "TIED"
    elif user == 2 and num == 3:
     x ="LOST"
     loss += 1
    elif user == 3 and num == 1:
      x = "LOST"
      loss += 1
    elif user == 3 and num == 2:
      x = "WON"
      win += 1
    elif user == 3 and num == 3:
      x ="TIED"

    print(f"\nYou picked {choice[int(user)]} and the bot picked {choice[int(num)]}, you {x}!\n")
    print(f"win:{win} / loss:{loss}")

    if win == 5:
        break