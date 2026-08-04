# all these structures could be dicrianaries.
lol = [["a", "b"], ["c", "d"], ["e", "f"]]
lot = [("a", "b"), ("c", "d"), ("e", "f")]
tol = (["a", "b"], ["c", "d"], ["e", "f"])
tot = (("a", "b"), ("c", "d"), ("e", "f"))
los = ["ab", "cd", "ef"]
tos = ("ab", "cd", "ef")

letters: dict[str, str] = dict(tot)

# adding elements
letters["g"] = "h"

# edit element
letters["a"] = "a"

print(letters)

users = {
    "Chapman": "Graham",
    "Cleese": "John",
    "Gilliam": "Terry",
    "Idle": "Eric",
    "Jones": "Terry",
    "Palin": "Michael",
}

other_users = {"Marx": "Groucho", "Howard": "Moe"}

# merge 2 dict
users.update(other_users)

# remove element by key
del users["Marx"]

# clear dict
other_users.clear()

# is element in dict
if "Howard_" in users:
    print("Find!")

# get element by key
other_users["Marx"]

# get all keys
print(users.keys())

# get all values
print(users.values())

print(";\n".join(f"{k}: {v}" for k, v in users.items()))

same_users = users
copy_users = users.copy()
