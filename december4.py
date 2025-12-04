# Santa's Magical Toy Bag - Price Calculator
"""
Santa Claus is preparing his gift bag and checking toy prices.
Calculates the total price and count of toys costing more than 10 EUR.
Input ends when 0 is entered.

Example:
Input: 5.6; 6.7; 12.3; 15.7; 0
Output:
Total price of magical toys: 28.0 EUR
Number of magical toys: 2
"""


def calculate_magical_toys():
    """
    Calculate total price and count of toys costing more than 10 EUR.
    
    Reads toy prices from user input until 0 is entered.
    A toy is "magical" if its price is more than 10 EUR.
    
    Returns:
        Tuple of (total_price, count) for magical toys
    
    Raises:
        ValueError: If price is negative or invalid input
    """
    total_price = 0.0
    count = 0
    
    while True:
        try:
            # Get price input from user
            price = float(input("Enter toy price (or 0 to finish): "))
            
            # Check if input is the termination signal
            if price == 0:
                break
            
            # Validate that price is not negative
            if price < 0:
                print("Error: Price cannot be negative. Please enter a valid price.")
                continue
            
            # Check if toy is magical (costs more than 10 EUR)
            if price > 10:
                total_price += price
                count += 1
        
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
    
    return total_price, count


def main():
    """Main function to display Santa's magical toy summary."""
    print("Welcome to Santa's Toy Price Calculator!")
    print("Enter toy prices one by one. Enter 0 when finished.\n")
    
    # Calculate magical toys
    total_price, count = calculate_magical_toys()
    
    # Display results
    print("\n" + "="*50)
    if count > 0:
        print(f"Total price of magical toys: {total_price} EUR")
        print(f"Number of magical toys: {count}")
    else:
        print("No magical toys found in the list.")
        print(f"Total price of magical toys: 0.0 EUR")
        print(f"Number of magical toys: 0")
    print("="*50)


# Santa's workshop starts here
if __name__ == "__main__":
    main()
