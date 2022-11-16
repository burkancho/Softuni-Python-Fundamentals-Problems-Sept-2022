quantity_of_decoration = int(input())
days_left_until_christmas = int(input())
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
points_ornament_set = 5
points_tree_skirt = 3
points_tree_garland = 10
points_tree_lights = 17

budget = 0
total_spirit = 0
for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decoration += 2
    if day % 2 == 0:
        budget += quantity_of_decoration * price_ornament_set
        total_spirit += points_ornament_set
    if day % 3 == 0:
        budget += quantity_of_decoration * (price_tree_skirt + price_tree_garland)
        total_spirit += points_tree_skirt + points_tree_garland
    if day % 5 == 0:
        budget += quantity_of_decoration * price_tree_lights
        total_spirit += points_tree_lights
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        budget += price_tree_skirt + price_tree_garland + price_tree_lights
        total_spirit -= 20
if days_left_until_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")