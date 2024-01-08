# Ejercicio: Creación de diccionarios de Python

"""
Exercise: Create and modify a Python dictionary
Python dictionaries allow you to model more complex data. 
Dictionaries are a collection of key/value pairs, and are 
very common in Python programs. Their flexibility allows you 
to dynamically work with related values without having to 
create classes or objects.

Managing planet data
You want to create a program which will store and display 
information about planets. To start you will use one planet. 
Create a variable named planet. Store the following values as 
a dictionary:
"""

planet = {
    "name": "Mars",
    "moons": 2
}

print(planet)

"""
Display planet data
With the variable created, you will now display information. You can retrieve information by either using get or square brackets ([ ]) and the key name. Add the code to display the planet information in the following format:

__ has __ moon(s)

If you were working with Earth, the output would be Earth has 1 moon(s)

Note: You can use whatever string formatting option you like.
"""

print(f"{planet.get('name')} has {planet.get('moons')} moon(s)")

"""
Add circumference information
You can update existing keys or create new ones by either using the update method or using square brackets ([ ]). When you're using update, you pass in a new dictionary object with the updated or new values. When using square brackets, you specify the key name and assign a new value.

Add a new value to planet with a key of 'circumference (km)'. This new value should store a dictionary with the planet's two circumferences:

polar: 6752
equatorial: 6792
Finally, add the code to print the polar circumference of the planet. You can use whatever sentence formatting you wish.
"""

planet.update({"circumference (km)": {"polar":6752, "equatorial":6792}})

print(f"{planet.get('name')} has a polar circumference of {planet['circumference (km)']['polar']}")

# Ejercicio: Programación dinámica con diccionarios

"""
Calculating values
In this scenario, you will calculate both the total number of moons
in the solar system and the average number of moons a planet has. 
You will do this by using a dictionary object.

Start by creating a variable named planet_moons as a dictionary 
with the following key/values:

mercury: 0,
venus: 0,
earth: 1,
mars: 2,
jupiter: 79,
saturn: 82,
uranus: 27,
neptune: 14,
pluto: 5,
haumea: 2,
makemake: 1,
eris: 1
"""

planet_moons = {
    "mercury": 0,
    "venus": 0,
    "earth": 1,
    "mars": 2,
    "jupiter": 79,
    "saturn": 82,
    "uranus": 27,
    "neptune": 14,
    "pluto": 5,
    "haumea": 2,
    "makemake": 1,
    "eris": 1
}

"""
Obtain a list of moons and number of planets
Python dictionaries allow you to retrieve all the values and 
keys by using the values and keys methods, respectively. 
Each method returns a list containing the data, which can 
then be used like a regular Python list. You can determine 
the number of items by using len, and iterate through it 
by using for loops. In the dictionary you created, 
the planet names are keys and the number of moons are the values.

Start by retrieving a list with the number of moons, 
and store this in a variable named moons. Then obtain the total 
number of planets and store that value in a variable named 
total_planets.
"""

moons = planet_moons.values()
print(moons)

total_planets = len(planet_moons.keys())
print(total_planets)

"""
Determine the average number of moons
You will finish this exercise by determining the average number 
of moons. Start by creating a variable named total_moons; 
this will be your counter for the total number of moons. 
Then add a for loop to loop through the list of moons, 
adding each value to total_moons. Finally, calculate the average 
by dividing total_moons by total_planets and displaying the value.
"""
total_moons = 0

for moon in planet_moons.values():
    total_moons += moon

average_moons = total_moons / total_planets

print(f"Each planet has an average of: {average_moons} moons")