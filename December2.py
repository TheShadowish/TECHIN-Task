# Santa's Midnight Clock Countdown
"""
Santa's magical workshop clock shows x hours and y minutes.
Calculates how many minutes and seconds have passed since midnight.
"""


def calculate_time_passed(hours, minutes):
    """
    Calculate minutes and seconds passed since midnight.
    
    Args:
        hours: Hours on the clock (0-23)
        minutes: Minutes on the clock (0-59)
    
    Returns:
        Tuple of (minutes_passed, seconds_passed)
    
    Raises:
        ValueError: If hours or minutes are out of valid range
        TypeError: If inputs are not numeric
    """
    # Validate input types
    if not isinstance(hours, int) or not isinstance(minutes, int):
        raise TypeError("Hours and minutes must be integers")
    
    # Validate input ranges
    if not (0 <= hours <= 23):
        raise ValueError("Hours must be between 0 and 23")
    if not (0 <= minutes <= 59):
        raise ValueError("Minutes must be between 0 and 59")
    
    # Calculate minutes passed since midnight
    m = hours * 60 + minutes
    
    # Calculate seconds passed since midnight
    s = m * 60
    
    return m, s


def main():
    """Main function to handle user input and display results."""
    try:
        x = int(input("Enter hours (0-23): "))
        y = int(input("Enter minutes (0-59): "))
        
        # Calculate time passed
        m, s = calculate_time_passed(x, y)
        
        # Display results
        print(f"\nMinutes passed: m = {m}")
        print(f"Seconds passed: s = {s}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()