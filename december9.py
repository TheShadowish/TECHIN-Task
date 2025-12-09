# Santa's Perfect Christmas Melon
"""
Santa is looking for the perfect Christmas melon.
Finds the melon whose weight is closest to the average weight.
"""


def find_perfect_melon(weights):
    """
    Find the melon closest to the average weight.
    
    Args:
        weights: List of melon weights (positive real numbers)
    
    Returns:
        Tuple of (melon_number, average_weight)
        where melon_number is 1-indexed position
    
    Raises:
        ValueError: If weights list is empty or invalid
        TypeError: If weights are not numeric
    """
    # Validate input
    if not weights:
        raise ValueError("Must have at least one melon")
    
    if len(weights) == 0:
        raise ValueError("Weights list cannot be empty")
    
    # Validate all weights are numeric and positive
    for i, weight in enumerate(weights):
        if not isinstance(weight, (int, float)):
            raise TypeError(f"Weight at position {i} must be numeric")
        if weight < 0:
            raise ValueError(f"Weight at position {i} must be non-negative")
    
    # Calculate average weight
    average_weight = sum(weights) / len(weights)
    
    # Find the melon closest to average
    min_difference = float('inf')
    closest_melon_index = 0
    
    for i, weight in enumerate(weights):
        difference = abs(weight - average_weight)
        
        if difference < min_difference:
            min_difference = difference
            closest_melon_index = i
    
    # Return 1-indexed melon number and average weight
    melon_number = closest_melon_index + 1
    
    return melon_number, average_weight


def main():
    """Main function to handle user input and display results."""
    try:
        # Get number of melons
        n = int(input("Enter the number of melons: "))
        
        if n <= 0:
            raise ValueError("Number of melons must be positive (greater than 0)")
        
        # Get weights of melons
        print(f"Enter {n} melon weights (separated by spaces or one per line):")
        
        weights = []
        
        # Try to read from single line first
        try:
            weights_input = input("Weights: ").strip()
            
            # If input is empty, ask for line-by-line input
            if not weights_input:
                for i in range(n):
                    weight = float(input(f"Melon {i+1} weight: "))
                    weights.append(weight)
            else:
                # Parse space-separated values
                weight_values = weights_input.split()
                
                if len(weight_values) != n:
                    raise ValueError(f"Expected {n} weights, got {len(weight_values)}")
                
                for value in weight_values:
                    weights.append(float(value))
        
        except ValueError as e:
            if "could not convert" in str(e).lower():
                raise ValueError("All weights must be valid numbers")
            raise
        
        # Find the perfect melon
        melon_number, average_weight = find_perfect_melon(weights)
        
        # Display results
        print(f"\nChristmas Melon Analysis:")
        print("="*50)
        print(f"Number of melons: {n}")
        print(f"Melon weights: {weights}")
        print(f"Average weight: {average_weight:.2f}")
        print(f"\nPerfect melon: #{melon_number} with weight {weights[melon_number-1]:.2f}")
        print(f"Distance from average: {abs(weights[melon_number-1] - average_weight):.2f}")
        print("="*50)
        
        # Output in required format
        print(f"\n{melon_number} {average_weight:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
