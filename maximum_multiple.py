divisor = int(input())
boundary = int(input())
# for current_number in range(boundary + 1):
#     if current_number % divisor == 0 and current_number > 0:
#         n = current_number
# print(n)

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        break
print(current_number)