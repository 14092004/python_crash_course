#A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
menu_foods = ('Chicken Wings','Burger','Pizza','Pasta')
print("You can choose from the following:")
for food in menu_foods:
    print('-' , food)
menu_foods = ('Chicken Wings','Burger','Dosa','Salad')
print("\nOur menu has been updated.")
print("You can now choose from the following:")
for item in menu_foods:
    print("- " + item)
