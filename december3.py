# Santa's Christmas Magic - Number Transformation
"""
Santa has a four-digit number on his list.
Creates a new two-digit number by removing the two middle digits.
Example: 1235 -> 15
"""


def transform_number(number):
    """
    Remove the two middle digits from a four-digit number.
    
    Args:
        number: A four-digit integer (1000-9999)
    
    Returns:
        A two-digit number formed by first and last digits
    
    Raises:
        ValueError: If number is not four digits
        TypeError: If input is not numeric
    """
    # Validate input type
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")
    
    # Validate that it's a four-digit number
    if not (1000 <= number <= 9999):
        raise ValueError("Number must be a four-digit number (1000-9999)")
    
    # Convert to string to access digits
    number_str = str(number)
    
    # Extract first and last digits
    first_digit = number_str[0]
    last_digit = number_str[3]
    
    # Create new two-digit number
    new_number = int(first_digit + last_digit)
    
    return new_number


def main():
    """Main function to handle user input and display results."""
    try:
        number = int(input("Enter a four-digit number: "))
        
        # Transform the number
        result = transform_number(number)
        
        # Display result
        print(f"Original number: {number}")
        print(f"New number (magic applied): {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
