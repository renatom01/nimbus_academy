# Importing library
import random

def multiply_func():
    """
    This function randomly generates pairs of integers A and B (both in the range [1, 9]),
    calculates their product C = A * B, and prints the values of A and C.
    The function continues this process until a pair (A, B) is found such that
    the product C equals 4. Upon finding such a pair, it prints a success message
    and exits the loop.

    Returns:
        String contaning the values of A and B that resulted in 4 when multiplied.

    """
    while True:
        # Generate random integers A and B in the range [1, 9]
        A = random.randint(1, 9)
        B = random.randint(1, 9)

        # Calculate the product C = A * B
        C = A * B

        # Print the values of A and C
        print(f"A: {A}, C: {C}")

        # Check if the product C equals 4
        if C == 4:
            # Print success message and break out of the loop
            print(f"Success! A: {A}, B: {B}")
            break

# Function calling
multiply_func()