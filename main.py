def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    # Taking user input for temperature in Celsius
    celsius = float(input("Enter the temperature in Celsius: "))

    # Converting Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    # Displaying the converted temperature in Fahrenheit with two decimal places
    print(f"Fahrenheit: {fahrenheit:.2f}")
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
