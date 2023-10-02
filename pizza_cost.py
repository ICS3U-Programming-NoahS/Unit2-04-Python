#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Sept. 28th, 2023
# This program asks the user for the diameter of
# the pizza in cm. It then calculates and displays
# the total cost of the pizza.
import constants


def main():
    # Get the diameter of the pizza
    diameter = float(input("Enter the diameter of the pizza (cm): "))

    # Calculate the subtotal, tax and total cost
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # Display the total cost back to the user
    print("")
    print("The total cost is = ${:.2f}".format(total))


if __name__ == "__main__":
    main()
