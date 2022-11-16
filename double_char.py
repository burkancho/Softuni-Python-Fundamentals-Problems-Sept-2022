command = input()
double_command = ""
while command != "End":
    if command != "SoftUni":
        for letter in (command):
            double_command += letter * 2
        print(double_command)
    command = input()
    double_command = ""
