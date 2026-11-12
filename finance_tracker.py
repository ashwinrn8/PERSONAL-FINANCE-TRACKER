expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().rsplit(": ", 2)

            if len(parts) == 2:
                description, amount = parts
                category = "Uncategorized"
            else:
                description, category, amount = parts

            expenses.append({
                "description": description,
                "category": category,
                "amount": float(amount)
            })
except FileNotFoundError:
    pass

print("\nSaved expenses:")
total = 0

for expense in expenses:
    print(
        expense["description"],
        "|",
        expense["category"],
        "|",
        expense["amount"]
    )
    total = total + expense["amount"]

print("Total so far:", total)

while True:
    description = input(
        "\nWhat did you spend money on? (or type 'done'): "
    )

    if description.lower() == "done":
        break

    category = input("Category (Food, Transport, Bills, etc.): ").strip()

    while category == "":
        print("Please enter a category.")
        category = input("Category: ").strip()

    while True:
        amount_text = input("How much did it cost? ")

        try:
            amount = float(amount_text)

            if amount <= 0:
                print("Enter an amount greater than 0.")
                continue

            break
        except ValueError:
            print("Please enter a number, like 3 or 3.50.")

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

print("\nYour expenses:")
total = 0

for expense in expenses:
    print(
        expense["description"],
        "|",
        expense["category"],
        "|",
        expense["amount"]
    )
    total = total + expense["amount"]

print("Total spent:", total)

with open("expenses.txt", "w") as file:
    for expense in expenses:
        file.write(
            expense["description"]
            + ": "
            + expense["category"]
            + ": "
            + str(expense["amount"])
            + "\n"
        )

print("Expenses saved to expenses.txt")
