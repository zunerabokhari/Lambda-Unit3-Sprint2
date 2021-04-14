'''Queries to Explore Data'''


# Selects everything in the table
select_all = '''
SELECT *
FROM charactercreator_character;'''

# Selects the total number of Characters in charactercreator_character
total_characters = """
SELECT DISTINCT(COUNT(character_id))
FROM charactercreator_character;"""


# Select total number of items in armory_item
total_items = """
SELECT DISTINCT(COUNT(item_id))
FROM armory_item;"""


# Selects total weapons
weapons = """
SELECT COUNT(*)
FROM armory_weapon;"""


# Calculates how many items are not weapons 
non_weapons = """total_items - weapons"""


# Selects total items each character has
character_items = """
SELECT character_id, COUNT(*)
FROM charactercreator_character_inventory
GROUP BY character_id;"""







