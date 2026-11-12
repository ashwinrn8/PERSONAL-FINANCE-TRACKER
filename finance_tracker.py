expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            description, amount = line.strip().rsplit(": ", 1)
            expenses.append({"description": description, "amount": float(amount)})
except FileNotFoundError:
    pass

print("\nSaved expenses:")
total = 0

for expense in expenses:
    print(expense["description"], "-", expense["amount"])
    total = total + expense["amount"]

print("Total so far:", total)

while True:
    description = input("What did you spend money on? (or type 'done'): ")

    if description.lower() == "done":
        break

    amount = float(input("How much did it cost? "))

    expenses.append({"description": description, "amount": amount})

print("\nYour expenses:")

total = 0

for expense in expenses:
    print(expense["description"], "-", expense["amount"])
    total = total + expense["amount"]

print("Total spent:", total)

with open("expenses.txt", "w") as file:
    for expense in expenses:
        file.write(expense["description"] + ": " + str(expense["amount"]) + "\n")

print("Expenses saved to expenses.txt")
