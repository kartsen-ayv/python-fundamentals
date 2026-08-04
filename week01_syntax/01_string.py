sent = "A duck goes into a bar..."

print(sent.replace('duck', 'rabbit'))

print(len(sent))
print(sent.startswith("a duck"))
print(sent.endswith("bar"))
print(sent.find("a"))
print(sent.rfind("a"))
print(sent.count("a"))
print(sent.isalnum())
print(sent.isalpha())

print(sent.strip("."))
print(sent.capitalize())
print(sent.title())
print(sent.upper())
print(sent.lower())
print(sent.swapcase())

print(sent.center(30))
print(sent.rjust(30))
print(sent.ljust(30))
