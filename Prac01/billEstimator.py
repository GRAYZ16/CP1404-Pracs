__author__ = "Joshua Gray"

print("Electricity Bill Estimator\n")

price = float(input("Enter cents per kWh: "))
dailyUse = float(input("Enter daily use in kWh: "))
billingDays = float(input("Enter number of billing days: "))

estimatedBill = (price / 100) * dailyUse * billingDays

print("Estimated Bill: ${:.2f}".format(estimatedBill))