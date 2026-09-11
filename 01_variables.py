#Variables
my_string_variable = "My String Variable"
print(my_string_variable)

my_integer_variable = 10
print(my_integer_variable)

my_integer_to_string_variable = str(my_integer_variable)
print(my_integer_to_string_variable)
print(type(my_integer_to_string_variable))

my_boolean_variable = True
print(my_boolean_variable)

#Concatenación de variables en un print
print(my_string_variable, my_integer_variable, my_integer_to_string_variable, my_boolean_variable)
print("Este es el valor:", my_boolean_variable)

#Algunas funciones del sistema 
print(len(my_string_variable)) # Devuelve la longitud de la variable

#Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Sofia", "Pinto", "Sofi", 30
print("Me llamo:", name, surname,". Mi alias es:", alias, "y tengo", age, "años.")

#Input
""""
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
"""

#Cambio de tipo de dato
name = 30
age = "Sofia"
print(name)
print(age)

#¿Forzamos el tipo de dato de una variable?
address: str = "Mi dirección"
address = True
address = 5
address = 1.5
print(type(address))




