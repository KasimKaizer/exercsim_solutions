"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(number_of_layers):
  """Calculate the preperation time.

  :param number_of_layers: int - the number of layers in the lasagna.
  :return: int - total time elapsed (in minutes) preparing.

  This function takes one integer representing the number of lasagna
  layers. It then calculates the total preparation time.
  """
  return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
  """Calculate the elapsed cooking time.

  :param number_of_layers: int - the number of layers in the lasagna.
  :param elapsed_bake_time: int - time the lasagna has been baking in the oven.
  :return: int - total time elapsed (in minutes) preparing and baking.

  This function takes two integers representing the number of lasagna
  layers and the time already spent baking the lasagna. It calculates
  the total elapsed minutes spent cooking (preparing + baking).
  """
  return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
