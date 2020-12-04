from random import randint
low = 0
high = 100

correct = randint(low, high)
print(f"Guess a number between {high} and {low}:")

while True:
  guess = int(input())
  if guess < correct:
    print("Guess higher.")
  elif  guess > correct:
    print("guess lower.")
  else:
    print("You win!")
    break


