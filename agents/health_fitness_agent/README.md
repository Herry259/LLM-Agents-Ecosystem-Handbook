# Health & Fitness Agent

This example implements a **health and fitness assistant** that provides
personalised advice based on basic biometric information.  It calculates
your Body Mass Index (BMI), categorises it and recommends general
lifestyle tips.  While this is not a replacement for professional
medical guidance, it demonstrates how an agent can collect user input
and apply simple heuristics to generate useful outputs.

## Setup

No external dependencies are required; the script uses only the Python
standard library.

## Usage

```bash
python main.py
```

You will be prompted for the following details:

1. Gender (optional: may influence calorie estimates).
2. Age.
3. Height (in centimetres).
4. Weight (in kilograms).
5. Fitness goal (maintain, lose weight, gain weight).

The agent will output your BMI, its interpretation and suggestions for
diet and exercise.  Feel free to tweak the heuristics in `main.py` to
better suit your needs.

## Extending the Agent

- Integrate with APIs like [Nutritionix](https://www.nutritionix.com) to
  fetch detailed nutritional information.
- Use a chatbot framework (e.g. LangChain) to handle conversations
  spanning multiple turns and contexts.
- Incorporate wearable device data to track progress over time.