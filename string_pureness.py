n = int(input())

for _ in range(n):
    pure = True
    string = str(input())
    for letter in (string):
        if letter == "." or letter == "," or letter == "_":
            pure = False
    if pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")