"""
A Small program that allows a shipping company to quickly
work out total shipping charge.

Enter a number of items with associated cost
10% discount for shipments over $100
"""
__author__ = "Joshua Gray"

HEADER = "SHIPPING CALCULATOR V1.0"

print(HEADER)

itemQuantity = int(input("How many items are you wanting to ship? "))

while itemQuantity < 0:
	print("Invalid Number of Items\n")
	itemQuantity = int(input("How many items are you wanting to ship? "))


runningCost = 0.0

for i in range(itemQuantity):
	runningCost += abs(float(input("How much does item No.{} cost? $".format(i+1))))

if runningCost > 100:
	print("Total Cost: ${}".format(runningCost - runningCost * 0.1))
else:
	print("Total Cost: ${}".format(runningCost))
