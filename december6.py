# Santa's Sleigh Flight Schedule
"""
Santa's magical sleigh takes off from the North Pole.
Calculates the landing time after a flight duration.
Handles flights that extend past midnight (next day).
"""


def calculate_landing_time(takeoff_hour, takeoff_minute, flight_duration_minutes):
    """
    Calculate the landing time of Santa's sleigh.
    
    Args:
        takeoff_hour: Hour of takeoff (0-23)
        takeoff_minute: Minute of takeoff (0-59)
        flight_duration_minutes: Duration of flight in minutes (can be large)
    
    Returns:
        Tuple of (landing_hour, landing_minute)
    
    Raises:
        ValueError: If parameters are out of valid range
        TypeError: If inputs are not numeric
    """
    # Validate input types
    if not isinstance(takeoff_hour, int) or not isinstance(takeoff_minute, int) or not isinstance(flight_duration_minutes, int):
        raise TypeError("All parameters must be integers")
    
    # Validate input ranges
    if not (0 <= takeoff_hour <= 23):
        raise ValueError("Takeoff hour must be between 0 and 23")
    if not (0 <= takeoff_minute <= 59):
        raise ValueError("Takeoff minute must be between 0 and 59")
    if flight_duration_minutes < 0:
        raise ValueError("Flight duration must be non-negative")
    
    # Convert takeoff time to total minutes since midnight
    total_minutes_at_takeoff = takeoff_hour * 60 + takeoff_minute
    
    # Add flight duration
    total_minutes_at_landing = total_minutes_at_takeoff + flight_duration_minutes
    
    # Handle next day (modulo 24 hours = 1440 minutes)
    total_minutes_at_landing = total_minutes_at_landing % (24 * 60)
    
    # Convert back to hours and minutes
    landing_hour = total_minutes_at_landing // 60
    landing_minute = total_minutes_at_landing % 60
    
    return landing_hour, landing_minute


def main():
    """Main function to handle user input and display results."""
    try:
        a = int(input("Enter takeoff hour (0-23): "))
        b = int(input("Enter takeoff minute (0-59): "))
        c = int(input("Enter flight duration in minutes: "))
        
        # Calculate landing time
        v, m = calculate_landing_time(a, b, c)
        
        # Display results
        print(f"\nTakeoff time: {a:02d}:{b:02d}")
        print(f"Flight duration: {c} minutes")
        print(f"Landing time: {v:02d}:{m:02d}")
        
        # Check if landing is on the next day
        takeoff_total = a * 60 + b
        landing_total = takeoff_total + c
        
        if landing_total >= 24 * 60:
            days_passed = landing_total // (24 * 60)
            print(f"\n🎅 Santa lands on the next day (after {days_passed} day(s))!")
        else:
            print(f"\n✨ Safe landing on the same day!")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


# Santa's workshop starts here
if __name__ == "__main__":
    main()
