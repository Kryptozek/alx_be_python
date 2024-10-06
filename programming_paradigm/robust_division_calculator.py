# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division while handling errors like division by zero and non-numeric inputs."""
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
