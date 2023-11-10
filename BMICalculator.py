weight = input("Add meg a súlyod (kg): ")
tall = input("Add meg a magasságod (m): ")
bmi = int(int(weight) / (float(tall) ** 2))
print("A te BMI értéked: " + str(bmi))