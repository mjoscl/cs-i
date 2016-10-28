"""
file: ____.py
language:python3
author: mjoscl@rit.edu michael j oconnor
description:

"""


# --IMPORT STATEMENTS--
# import turtle
#from rit_lib import * #make sure a copy is in the same directory!


# --CONSTANTS--
def CONSTANT_NAME():
    """
    this is a constant function which returns the constant named CONSTANT_NAME
    with a value of 100
    :return: the value of 100
    :rtype: int
    """
    return 100


# --CLASSES--
class CLASS_NAME(struct):
    """
    describe class and its slots
    """
    _slots=((slot1_type,'slot1_name'),(slot2_type,'slot2_name'),(slot3_type1,slot3,type2,'slot3_name'))


# --FUNCTIONS--
def function1():
    """
    this is a description of what this function does
    :param param1_name: description
    :type param1_name: type description
    :return: return description
    :rtype: the return type description
    """
    pass


def test_function1():
    """ Tests each of the flow decisions for validity """
    function1()
    pass


if __name__ == "__main__":
    """ this is a description of what the main function does """

    # main function calls here
    test_function1()
    # function1()