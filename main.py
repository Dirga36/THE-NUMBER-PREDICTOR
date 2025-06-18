import re

print("=" * 50)
print("THE NUMBER PREDICTOR 🔮")
print("=" * 50)

while True:
    user_input = input("\n👉 Insert a number:\n> ").strip()
    digits = ''.join(filter(str.isdigit, user_input))
    
    if digits:
        num = int(digits)
        print("\nResult:", num)
        print("\nHave a great day!")
        print("=" * 50)
        break
    else:
        print("No number found!")
        print("Try again.\n")
