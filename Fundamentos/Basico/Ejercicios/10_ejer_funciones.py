def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
print(distance_from_earth("Moon"))

print(distance_from_earth("Saturn"))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))


"""
Aunque pasar funciones directamente a otras funciones como entrada
es útil, existe la posibilidad de que se reduzca la legibilidad. 
Este patrón es especialmente problemático cuando las funciones 
requieren muchos argumentos.
"""
total_days = days_to_complete(238855, 75)

print(round(total_days))


#### Exercise: Work with arguments in functions
"""
Required arguments in functions are used when functions need 
those arguments to work properly. In this exercise, 
you'll construct a fuel report that requires information 
from several fuel locations throughout the rocket ship.
"""

"""
Create a report generation function
Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.

Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:

Fuel report:
    Main tank: ##
    External tank: ##
    Hydrogen tank: ##
"""

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

# Testing the function
generate_report(2,5,6)


from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())


#### Exercise: Work with keyword arguments in functions
"""
In the prior exercise you created a report for a ship with three 
fuel tanks. What happens if the ship has multiple tanks? 
Keyword arguments can be a perfect solution for this type of 
a situation. With keyword arguments a caller can provide multiple 
values which your code can interact with.
"""

"""
Create an updated fuel report function
Create a new function named fuel_report. The function will accept 
a keyword arguments parameter named fuel_tanks. Add the code to 
loop through the entries provided to generate the following output,
where name is the name of the keyword argument and value is 
the value:

name: value
name: value
"""
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

"""
Call the function
With the function created, it's time to call it! Pass in the following values for the keyword arguments:

main = 50
external = 100
emergency = 60
"""
fuel_report(main=50, external=100, emergency=60)
