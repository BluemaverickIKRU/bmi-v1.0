#BMI Calculator V0.1
print("Welcome to BMI Calculator v1.0")
print("-------------------------------")
name = input("Type your name: ")
age = input("Type your age: ")
height = input("Type you height in Cm: ")
weight = input("Type your weight in kg: ")
height_meter = int(height) * 0.01
bmi = int(weight) / (height_meter) **2 
print("Your BMI is:",bmi)

if (bmi > 25):
    print("Status : Your should excersise regularly :)")

elif (bmi < 18):
    print("Status : Your should have a proper diet and eat well :)")

else:
    print("Status : Your are good.Never stop doing what you are doing now :)")    

print("Thank you for using our app :)")
print("------------------------------")
