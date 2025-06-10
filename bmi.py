print("What is your weight?")
weight = int(input("Enter your weight (kg):\n"))
print("What is your height?")
height = float(input("Enter your height (m):\n"))
bmi = (weight / (height ** 2))
print(round(bmi, 2))

if 18 < bmi < 25:
    print("Your weight is normal. ✅")
    print("Tips: Maintain a balanced diet and regular exercise to stay healthy!")
elif bmi < 18:
    print("You are underweight. ⚠️")
    print("Tips: Increase calorie intake with nutrient-rich foods like nuts, dairy, and lean proteins. Consider consulting a nutritionist.")
else:
    print("You are overweight. ⚠️")
    print("Tips: Focus on portion control, eat more vegetables, and engage in regular physical activity. A doctor or dietitian can help with a plan.")
