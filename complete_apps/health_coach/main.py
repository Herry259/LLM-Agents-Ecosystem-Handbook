"""
Health Coach
============

An interactive program that calculates BMI and daily caloric needs and provides basic advice on fitness and nutrition.  This
application demonstrates how to build a complete user‑facing tool from the skeleton examples included in this repository.
"""

def calculate_bmi(weight: float, height_cm: float) -> float:
    """Return the Body Mass Index (BMI)."""
    height_m = height_cm / 100.0
    return weight / (height_m ** 2)


def bmr_harris_benedict(sex: str, weight: float, height_cm: float, age: int) -> float:
    """Calculate Basal Metabolic Rate using Harris–Benedict formula."""
    if sex.lower().startswith("m"):
        return 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)


def activity_factor(level: str) -> float:
    factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9,
    }
    return factors.get(level.lower(), 1.2)


def main() -> None:
    print("Welcome to the Health Coach!\n")
    try:
        age = int(input("Age (years): "))
        sex = input("Sex (M/F): ")
        height_cm = float(input("Height (cm): "))
        weight = float(input("Weight (kg): "))
        level = input("Activity level (sedentary/light/moderate/active/very active): ")
        goal = input("Goal (lose/maintain/gain): ")
    except Exception as e:
        print(f"Error: {e}. Please enter valid numeric values.")
        return

    bmi = calculate_bmi(weight, height_cm)
    bmr = bmr_harris_benedict(sex, weight, height_cm, age)
    cal_needs = bmr * activity_factor(level)

    print(f"\nYour BMI is {bmi:.1f}.")
    if bmi < 18.5:
        print("Underweight: you may need to gain weight.")
    elif bmi < 25:
        print("Normal: keep up the good work!")
    elif bmi < 30:
        print("Overweight: consider losing weight.")
    else:
        print("Obese: weight loss is recommended.")

    if goal.lower().startswith("l"):
        target_cal = cal_needs - 500
        print(f"To lose weight, aim for about {target_cal:.0f} calories per day.")
    elif goal.lower().startswith("g"):
        target_cal = cal_needs + 500
        print(f"To gain weight, aim for about {target_cal:.0f} calories per day.")
    else:
        target_cal = cal_needs
        print(f"To maintain your weight, aim for about {target_cal:.0f} calories per day.")

    print("\nGeneral advice:")
    print("- Eat a balanced diet rich in whole foods and minimise processed foods.")
    print("- Incorporate both cardio and strength training into your routine.")
    print("- Stay hydrated and prioritise adequate sleep.")


if __name__ == "__main__":
    main()