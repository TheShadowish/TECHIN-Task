# Christmas Lights Pattern Generator
"""
Santa's programmable Christmas lights system.
Generates an N × N grid of lights based on numeric rules.
"""


def generate_lights_pattern(n):
    """
    Generate an N × N Christmas lights grid pattern.
    
    Rules for each cell at position (row, col) where row, col start from 1:
    - If (row + col) is divisible by 15 (both 3 and 5): 'G'
    - If (row + col) is divisible by 5: 'S'
    - If (row + col) is divisible by 3: 'T'
    - Otherwise: '.'
    
    Args:
        n: Grid size (positive integer)
    
    Returns:
        List of strings representing the grid with border
    
    Raises:
        ValueError: If n is not positive
        TypeError: If n is not numeric
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Grid size must be an integer")
    
    if n <= 0:
        raise ValueError("Grid size must be positive (greater than 0)")
    
    grid = []
    
    # Add top border
    top_border = '#' * (n * 2 + 3)
    grid.append(top_border)
    
    # Generate each row
    for row in range(1, n + 1):
        row_str = '# '
        
        for col in range(1, n + 1):
            total = row + col
            
            # Check divisibility rules (check both 3 and 5 first)
            if total % 15 == 0:  # Divisible by both 3 and 5
                row_str += 'G'
            elif total % 5 == 0:  # Divisible by 5
                row_str += 'S'
            elif total % 3 == 0:  # Divisible by 3
                row_str += 'T'
            else:  # Not divisible by 3 or 5
                row_str += '.'
            
            # Add space between characters
            row_str += ' '
        
        row_str += '#'
        grid.append(row_str)
    
    # Add bottom border
    bottom_border = '#' * (n * 2 + 3)
    grid.append(bottom_border)
    
    return grid


def display_pattern(n):
    """
    Display the Christmas lights pattern.
    
    Args:
        n: Grid size
    """
    grid = generate_lights_pattern(n)
    
    print()
    for line in grid:
        print(line)
    print()


def main():
    """Main function to handle user input and display results."""
    try:
        n = int(input("Enter the grid size (N): "))
        
        # Generate and display the pattern
        display_pattern(n)
        
        # Optional: Show the calculation details for verification
        show_details = input("Would you like to see the calculation details? (yes/no): ").lower().strip()
        if show_details in ['yes', 'y']:
            print(f"\nCalculation Details for N = {n}:")
            print("="*60)
            print(f"{'Row':<5} {'Col':<5} {'Sum':<5} {'÷3':<10} {'÷5':<10} {'÷15':<10} {'Result':<5}")
            print("-"*60)
            
            for row in range(1, n + 1):
                for col in range(1, n + 1):
                    total = row + col
                    div_3 = "Yes" if total % 3 == 0 else "No"
                    div_5 = "Yes" if total % 5 == 0 else "No"
                    div_15 = "Yes" if total % 15 == 0 else "No"
                    
                    if total % 15 == 0:
                        result = 'G'
                    elif total % 5 == 0:
                        result = 'S'
                    elif total % 3 == 0:
                        result = 'T'
                    else:
                        result = '.'
                    
                    print(f"{row:<5} {col:<5} {total:<5} {div_3:<10} {div_5:<10} {div_15:<10} {result:<5}")
            
            print("="*60)
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
