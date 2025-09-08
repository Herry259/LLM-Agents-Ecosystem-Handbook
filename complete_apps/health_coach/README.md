# Health Coach

The **Health Coach** application is a simple interactive tool that collects basic personal information and provides general health
advice.  It showcases how to turn a skeleton into a usable product without requiring any external APIs.

## Features

* Calculates Body Mass Index (BMI) and categorises it according to standard ranges.
* Estimates daily caloric needs based on the Harris–Benedict equation, considering activity level.
* Offers general advice on nutrition and exercise tailored to the user’s goal (lose, gain or maintain weight).

## Usage

Run the application in a terminal:

```bash
python main.py
```

You will be prompted to enter your age, sex, height, weight, activity level and health goal.  The program will then display your
BMI, recommended caloric intake and some basic recommendations.  This example can be extended to call more advanced models or
agents as you explore the framework comparison provided in this repository.