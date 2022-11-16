first_string = input()
second_string = input()
last_string = first_string
for letter in range(len(first_string) + 1):
    new_string = second_string[0:letter] + first_string[letter:len(first_string)]
    if new_string != last_string:
        print(new_string)
    last_string = new_string

