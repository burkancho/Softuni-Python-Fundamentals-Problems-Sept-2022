budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_1l_milk = 1.25 * price_flour
price_bread = price_eggs + price_flour + price_1l_milk * 0.25
count_colored_eggs = 0
count_bread = 0
while budget - price_bread >= 0:
    count_bread += 1
    count_colored_eggs += 3
    if count_bread % 3 == 0:
        count_colored_eggs -= count_bread - 2
    budget -= price_bread
print(f"You made {count_bread} loaves of Easter bread! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.")