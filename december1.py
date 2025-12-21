def calculate_tile_cost(length, width, m2price, extra_percentage=None):
    """
    Calculate the total cost of tiles for Santa's room renovation.
    
    Args:
        length: Room length in meters (float or int)
        width: Room width in meters (float or int)
        m2price: Price per square meter in coins (float or int)
        extra_percentage: Extra percentage for losses (default None - user must provide)
    
    Returns:
        Total cost including extra percentage for losses (float)
    
    Raises:
        ValueError: If any parameter is negative or zero
        TypeError: If parameters are not numeric
    """
    # Validate input parameters
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)) or not isinstance(m2price, (int, float)):
        raise TypeError("All parameters must be numeric (int or float)")
    
    if length <= 0 or width <= 0 or m2price <= 0:
        raise ValueError("Length, width, and price must be positive numbers")
    
    if extra_percentage is None:
        raise ValueError("Extra percentage must be provided")
    
    if extra_percentage < 0 or extra_percentage > 1:
        raise ValueError("Extra percentage must be between 0 and 1 (0-100%)")
    
    # Calculate floor area
    floor_area = length * width
    
    # Add extra tiles for losses
    total_area_with_extra = floor_area * (1 + extra_percentage)
    
    # Calculate total cost
    total_cost = total_area_with_extra * m2price
    
    return round(total_cost, 2)


def main():
    """Main function to demonstrate tile cost calculation."""
    try:
        # Get user input
        length = float(input("Enter room length (meters): "))
        width = float(input("Enter room width (meters): "))
        m2price = float(input("Enter price per square meter (coins): "))
        percentage_input = float(input("Enter extra percentage for losses (e.g., 10 for 10%): "))
        
        # Convert percentage to decimal (e.g., 10 -> 0.1)
        extra_percentage = percentage_input / 100
        
        total_cost = calculate_tile_cost(length, width, m2price, extra_percentage)
        print(f"\nTotal cost: {total_cost} coins")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    main()