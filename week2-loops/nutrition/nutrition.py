foods = [
    {"name": "apple", "type": "fruit", "calories": 130},
    {"name": "avocado", "type": "fruit", "calories": 50},
    {"name": "banana", "type": "fruit", "calories": 110},
    {"name": "cantaloupe", "type": "fruit", "calories": 50}
]
# case insensitive
item = input("Item: ").lower()
# using for loop to check all the item list
for food in foods:
    if food["name"] == item: # check for matching name, if found then print the calories of the food
        print("Calories:", food["calories"]) 