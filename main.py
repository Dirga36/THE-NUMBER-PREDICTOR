import re

print("=" * 50)
print("THE NUMBER PREDICTOR 🔮")
print("=" * 50)

while True:
    user_input = input("\n👉 Insert a number:\n> ").strip()

    # Look for a signed or unsigned number, possibly with a decimal
    match = re.search(r"-?\d+(?:\.\d+)?", user_input)

    if match:
        num_str = match.group()
        num = float(num_str) if '.' in num_str else int(num_str)
        
        print("\nResult:", num)
        print("\nHave a great day!")
        print("=" * 50)
        break
    else:
        print("No number found!")
        print("Try again.\n")
