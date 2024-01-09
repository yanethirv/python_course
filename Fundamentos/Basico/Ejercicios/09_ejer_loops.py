"""
código para pedir a los usuarios que introduzcan valores y, 
después, permitirles usar done cuando desee terminar
"""
user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done: ')

"""
Agregar los valores introducidos a una lista, y finalizar
la ejecución del programa al escribir "Done".
"""
# Create the variable for entrada
entrada = ''
# Create the list to store the values
entradas = []

# The while loop
while entrada.lower() != 'done':
    # Check if there's a value in entrada
    if entrada:
        # Store the value in the list
        entradas.append(entrada)
        print(entradas)
    # Prompt for a new value
    entrada = input('Enter a new value, or done when done: ')

#print(entradas)

## EJERCICIO: CREACION DE UN BUCLE "WHILE"
"""
Using while loops in Python
In Python, while loops let you run code an unknown number of times. The loops examine a Boolean condition and, as long as the condition is true, the code inside the loop will run. This is very useful for situations like prompting a user for values.

In this exercise, you're creating an application that prompts a user to enter a list of planets. In a later exercise, you'll add code that displays the list. For now, though, you'll create only the code that prompts the user.

Start by adding two variables, one for the input from the user, named new_planet, and another variable for the list of planets, named planets.
"""

new_planet = ''
planets = []

"""
Create a while loop
Starting with the variables you've just created, create a while loop. The while loop will run while new_planet is not set to done.

Inside the loop, check to see whether the new_planet variable contains a value, which should be the name of a planet. This is a quick way to see whether the user has entered a value. If they have, your code will append that value to the planets variable.

Complete the while loop by using input to prompt the user to enter a new planet name or done if they're done entering planet names. You'll store the value from input in the new_planet variable.

Finally, outside of the while loop, print the list of planets by using print.

As you complete this part of the exercise, pay attention to tab levels to ensure code is run at the correct time.
"""

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
        
    new_planet = input("What is a planet? ")

print("Planet list:", planets)

"""
Exercise - Loop over a list
In the previous exercise, you created code to prompt users to enter a list of planet names. In this exercise, you'll complete the application by writing code that displays the planet names one by one.

The first cell contains the code from the prior exercise, without the print statement. Run the cell and provide a list of planets. (Enter a planet name and select "Submit". For each new entry, overtype the previous entry and select "Submit".)

# Display the list of planets
The planets variable stores the planet names that a user entered. 
You'll now use a for loop to display those entries.

Create a for loop to iterate over the planets name list. 
You can use planet as the name of the variable for each planet. 
Inside the for loop, use print to display each planet name.
"""
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done: ')

for planet in planets:
    print(f'I have discovered {planet}!')
