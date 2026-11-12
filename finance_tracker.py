expenses = []

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

with open("expenses.txt", "a") as file:
    for expense in expenses:
        file.write(expense["description"] + ": " + str(expense["amount"]) + "\n")

print("Expenses saved to expenses.txt")
