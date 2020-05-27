item_name = input('Enter food item name:\n')

item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))
total_cost = item_quantity * item_price
total_cost1 = ('{:.2f}'.format(total_cost))
print()
print('RECEIPT')
print(item_quantity, item_name,'@','$'+'{:.2f}'.format(item_price), '=','$'+total_cost1)
print("Total cost: $"+total_cost1)

print()
print()
item_name2 = input('Enter second food item name:\n')
item_price2 = float(input('Enter item price:\n'))
item_quantity2 = int(input('Enter item quantity:\n'))
print()
total_cost2 = item_quantity2 * item_price2
total_cost22 = ('{:.2f}'.format(total_cost2))
# print()
print('RECEIPT')
print(item_quantity, item_name,'@','$'+'{:.2f}'.format(item_price), '=','$'+total_cost1)
print(item_quantity2, item_name2,'@','$'+'{:.2f}'.format(item_price2), '=','$'+total_cost22)
total_cost3 = (item_quantity * item_price) + (item_quantity2 * item_price2)
print("Total cost: $"+'{:.2f}'.format(total_cost3))

tip = total_cost3 * .15
print()
print('15% gratuity: $'+'{:.2f}'.format(tip))
total_with_tip = ((item_quantity * item_price) + (item_quantity2 * item_price2)) + (total_cost3 * .15)
print('Total with tip: $'+'{:.2f}'.format(total_with_tip))