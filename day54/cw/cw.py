#davaleba 1
def division_calculator():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = numerator / denominator
        print(f"Result: {result}")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    
    except Exception as e:
        print(f"Error: Please enter valid numbers. ({e})")
    
    finally:
        print("Operation complete.")

