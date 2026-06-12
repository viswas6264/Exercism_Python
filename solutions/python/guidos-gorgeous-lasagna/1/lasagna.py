"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    '''This func() just returns the baking time remained'''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
bake_time_remaining(30)

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(layers):
    '''This returns the preparation time in minutes'''
    return layers*PREPARATION_TIME
preparation_time_in_minutes(3)
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers, elapsed_bake_time):
    '''This returns the time taken by all layers and the time consumed for doing that '''
    return preparation_time_in_minutes(layers)+elapsed_bake_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

print(bake_time_remaining.__doc__)
print(preparation_time_in_minutes.__doc__)
print(elapsed_time_in_minutes.__doc__)