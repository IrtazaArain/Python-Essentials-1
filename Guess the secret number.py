secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    number = int(input("Enter your guess: "))  # Added prompt inside input
    if number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
