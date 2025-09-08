"""
Health & Fitness Agent
----------------------

This script collects basic health metrics from the user and returns a
simple analysis along with advice.  It demonstrates how to combine user
input with conditional logic and formulas (e.g., BMI) to produce a
personalised response.  It is not intended to replace professional
medical advice.
"""

def calculate_bmi(weight: float, height_cm: float) -> float:
    """Compute Body Mass Index from weight (kg) and height (cm)."""
    height_m = height_cm / 100.0
    return weight / (height_m ** 2)


def interpret_bmi(bmi: float) -> str:
    """Return a human‑readable category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if 18.5 <= bmi < 25:
        return "Normal weight"
    if 25 <= bmi < 30:
        return "Overweight"
    return "Obesity"


def advice_for_goal(goal: str) -> str:
    """Provide basic advice depending on the user's fitness goal."""
    goal = goal.lower()
    if goal == "maintain":
        return (
            "Maintain a balanced diet rich in fruits, vegetables and whole grains."
            " Aim for at least 150 minutes of moderate exercise per week and monitor your weight regularly."
        )
    if goal == "lose" or goal == "lose weight":
        return (
            "Create a caloric deficit by consuming slightly fewer calories than you burn."
            " Focus on lean proteins, high‑fibre foods and reduce processed sugars."
            " Incorporate both cardio and resistance training into your routine."
        )
    if goal == "gain" or goal == "gain weight":
        return (
            "Increase your caloric intake with nutrient‑dense foods such as nuts, avocados and whole grains."
            " Engage in strength training to build muscle and aim for a positive energy balance."
        )
    return "Set a clear goal (maintain, lose weight or gain weight) to receive customised advice."


def main() -> None:
    print("Welcome to the Health & Fitness Agent!")
    gender = input("Enter your gender (optional): ")
    age_input = input("Enter your age in years: ")
    height_input = input("Enter your height in cm: ")
    weight_input = input("Enter your weight in kg: ")
    goal = input("What is your goal? (maintain/lose weight/gain weight): ").strip()

    try:
        age = int(age_input)
        height_cm = float(height_input)
        weight = float(weight_input)
    except ValueError:
        print("Invalid input. Please enter numeric values for age, height and weight.")
        return

    bmi = calculate_bmi(weight, height_cm)
    bmi_category = interpret_bmi(bmi)
    advice = advice_for_goal(goal)

    print("\n--- Results ---")
    print(f"Your BMI is {bmi:.1f} ({bmi_category}).")
    print(advice)


if __name__ == "__main__":
    main()