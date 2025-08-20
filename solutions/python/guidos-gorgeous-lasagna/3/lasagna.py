"""Lasagna cooking time calculator.

This program provides functions to calculate baking time remaining,
preparation time, and total elapsed time when cooking a lasagna.
"""
#constants 
EXPECTED_BAKE_TIME= 40
PREPARATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param EXPECTED_BAKE_TIME: int - a constant(in minutes) to reperesent the cooking time of lasagna in the oven.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - bake_time_remaining (in minutes).

    The function that takes the actual time to bake a lasagna and takes one argument of
    how many minutes the lasagna has been in the stove and returns how many minutes the lasagna to be cooked
    based on the constant EXPECTED_BAKE_TIME
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calculate the remaining bake time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - preparation time required to make the lasagna layers (in minutes).

    The function takes one argument the number of layers and then it return the amount of time it takes to make
    the amount of time it takes to make the lasagna layers based on the PREPARATION_TIME.
    """
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time