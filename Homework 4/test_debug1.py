"""
This program contains a function to
compute the square root
of a non-negative integer without
using a built-in sqrt() function.

It has bug(s).

There are no tests (yet).

Your job is to
1) include in this program a sufficient
suite of pass/fail tests to thoroughly
test the function and expose all error(s).

2) Generate a screenshot that
demonstrates your use of a debugger
to step through the function. Specifically it should
illustrates the execution point of a test at
which the function makes (or is about to make)
a mistake.

3) fix the code and document your fix(es).
Include additional tests if you feel it
necessary to thoroughly test the function.

You will submit your updated version of this
file (along with a separate document containing
the screenshot and answered questions).

File:  test_debug1.py
Author: Aaron Deever
Author: Michael J. O'Connor

"""

def root(x):
    """
    This function computes the square root of an integer
    without using a built-in sqrt() function.  The technique
    is similar to long division.  Only the integer
    portion of the square root is computed.
    PRECONDITION:  x is integer and x >= 0.
    The function simply returns (None) if x < 0.
    :param x: the value to take the square root of
    :return: the root, truncated to just the integer
    portion of the root.
    """

    if x < 0:
        return

    # determine how many digits are in the number
    digits = 0
    val = x
    while val > 0:
        val = val // 10 # dividing by 10 effectively removes a low-order digit
        digits += 1

    # digits processed in pairs; consider number has a 0
    # in front if necessary to make number of digits even
    if digits % 2 == 1:
        digits += 1

    # go through digits two at a time
    pairsRemaining = digits / 2
    ans = 0
    remainder = 0

    while pairsRemaining > 0:
        # bring down next two digits
        
        remainder = 100 * remainder + nextTwoDigits(pairsRemaining,x)
        print("remainder=",remainder)
        # compute the next digit of the answer
        d = nextAnswerDigit(ans, remainder)

        # use this digit and update the remainder
        remainder = updateRemainder(ans, remainder, d)

        #update current answer based on new digit
        ans = 10 * ans + d

        pairsRemaining -= 1

    return ans


def nextTwoDigits(pairsRemaining, x):
    """
    Grabs the next two highest order digits that
    haven't yet been processed.
    :param pairsRemaining: how many pairs of digits have not yet
    been processed
    :param x: original number
    :return: the two digits as a two-digit number
    """

    # skip over low order pairs of digits
    pairsToSkip = pairsRemaining - 1
    print("Prior to loop:x=",x," pairsToSkip=",pairsToSkip," pairsRem=",pairsRemaining)
    while pairsToSkip > 0:
        print("iteration #",pairsToSkip," x=",x)
        x = x // 100  # dividing by 100 removes a low-order pair of digits
        print("iteration #", pairsToSkip, " x=", x)
        pairsToSkip -= 1

    # grab and return the next pair as 2-digit number
    print("returning from nextTwoDigits=",x)
    """
    **************************************************************************
    I KNOW THAT THIS FUNCTION IS WHERE THE ERROR LIVES. IT IS NOT RETURNING
    TWO DIGITS, WHICH CAUSES ALL THE OTHER FUNCTIONS TO MISBEHAVE. I AM JUST
    UNSURE HOW TO REPAIR IT. I COULD CONVERT ALL THE INT TO STRINGS AND
    SPLICE THEM,OR SETUP ANOTHER FOR LOOP TO REMOVE THE APPROPRIATE DIGITS FROM X.
    ***************************************************************************
    """
    return x


def nextAnswerDigit(currentAnswer, remainder):
    """
    computes the next digit of the answer based on the
    currentAnswer and the current remainder.
    :param currentAnswer: answer so far
    :param remainder: remainder so far
    :return: the next digit of the answer
    """

    # first we double the currentAnswer
    currentAnswer *= 2

    # then we want the largest digit, d, such that
    # current answer with d added as a last digit, then
    # multiplied by d, is less than or equal to the current remainder

    d = 9
    while d >= 0:
        product = (10*currentAnswer + d) * d
        if product <= remainder:
            return d
        d -= 1

def updateRemainder(currentAnswer, remainder, newDigit):
    """
    Based on the new answer digit just calculated, this
    function computes the new remainder.  (Really this
    could be folded into the nextAnswerDigit function,
    which could return the new digit and the new remainder,
    but we haven't discussed how to have a function
    return multiple values yet.)
    :param currentAnswer: answer so far
    :param remainder: remainder so far
    :param newDigit: new digit to be appended to current answer
    :return:
    """

    currentAnswer *= 2
    product = (10*currentAnswer + newDigit) * newDigit
    return remainder - product

if __name__ == "__main__":
    print("The square root of 59368 is",root(59368))