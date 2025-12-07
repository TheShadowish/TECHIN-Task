# Santa's Christmas Concert Seating Plan
"""
Santa is organizing a big Christmas concert with a seating arrangement.
Each row has 2 more seats than the previous row.
Calculates the total number of seats needed.
"""


def calculate_total_seats(num_rows, first_row_seats):
    """
    Calculate the total number of seats for the concert hall.
    
    The seating follows an arithmetic sequence:
    - Row 1: k seats
    - Row 2: k + 2 seats
    - Row 3: k + 4 seats
    - ...
    - Row n: k + 2(n-1) seats
    
    Formula: s = n*k + 2*(0 + 1 + 2 + ... + (n-1))
             s = n*k + 2*n*(n-1)/2
             s = n*k + n*(n-1)
             s = n*(k + n - 1)
    
    Args:
        num_rows: Number of rows (n) - must be positive integer
        first_row_seats: Number of seats in first row (k) - must be positive integer
    
    Returns:
        Total number of seats (s)
    
    Raises:
        ValueError: If parameters are invalid
        TypeError: If inputs are not numeric
    """
    # Validate input types
    if not isinstance(num_rows, int) or not isinstance(first_row_seats, int):
        raise TypeError("Number of rows and first row seats must be integers")
    
    # Validate input ranges
    if num_rows <= 0:
        raise ValueError("Number of rows must be positive (greater than 0)")
    if first_row_seats <= 0:
        raise ValueError("First row seats must be positive (greater than 0)")
    
    # Calculate total seats using arithmetic sequence formula
    # s = n*k + n*(n-1) = n*(k + n - 1)
    total_seats = num_rows * (first_row_seats + num_rows - 1)
    
    return total_seats


def display_seating_plan(num_rows, first_row_seats):
    """
    Display the seating plan visually.
    
    Args:
        num_rows: Number of rows
        first_row_seats: Number of seats in first row
    """
    print("\n" + "="*50)
    print("SEATING PLAN")
    print("="*50)
    
    total = 0
    for row in range(1, num_rows + 1):
        seats_in_row = first_row_seats + 2 * (row - 1)
        total += seats_in_row
        print(f"Row {row:2d}: {seats_in_row:3d} seats {'🎄' * (seats_in_row // 2)}")
    
    print("="*50)
    print(f"Total seats: {total}")
    print("="*50 + "\n")


def main():
    """Main function to handle user input and display results."""
    try:
        n = int(input("Enter the number of rows (n): "))
        k = int(input("Enter the number of seats in the first row (k): "))
        
        # Calculate total seats
        s = calculate_total_seats(n, k)
        
        # Display results
        print(f"\nNumber of rows: {n}")
        print(f"First row seats: {k}")
        print(f"Total seats needed: {s} 🎫")
        
        # Ask if user wants to see the seating plan
        show_plan = input("\nWould you like to see the seating plan? (yes/no): ").lower().strip()
        if show_plan in ['yes', 'y']:
            display_seating_plan(n, k)
        
        # Verify with manual calculation
        print("\nVerification:")
        manual_total = 0
        for row in range(1, n + 1):
            seats_in_row = k + 2 * (row - 1)
            manual_total += seats_in_row
            print(f"  Row {row}: {seats_in_row} seats")
        print(f"  Manual total: {manual_total}")
        
        if manual_total == s:
            print("✅ Calculation verified!")
        else:
            print("❌ Calculation error!")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
