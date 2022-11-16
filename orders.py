number_orders = int(input())
total_price = 0
order_price = 0
for order in range(number_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100:
        continue
    elif not 1 <= days < 32:
        continue
    elif not 1 <= capsules_per_day < 2001:
        continue

    order_price = capsules_per_day * days * price_per_capsule
    total_price += order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
else:
    print(f"Total: ${total_price:.2f}")