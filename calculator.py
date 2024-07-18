def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) given a weight in kilograms and height in meters.

    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: Calculated BMI
    """
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    """
    Determine the BMI category given a BMI value.

    Parameters:
    bmi (float): Calculated BMI

    Returns:
    str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {category}")
