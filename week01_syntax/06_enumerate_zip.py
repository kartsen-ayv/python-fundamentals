days = ["Monday", "Tuesday", "Wednesday"]
fruits = ["banana", "orange", "peach"]
drinks = ["coffee", "tea", "beer"]
desserts = ["tiramisu", "ice cream", "pie", "pudding"]

for index, day in enumerate(days):
    print(f"{index + 1}. {day}")

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)


english = "Monday", "Tuesday", "Wednesday"
french = "Lundi", "Mardi", "Mercredi"

en_fr = dict(zip(english, french))
print("\n".join(f"{k}: {v}" for k, v in zip(english, french)))
