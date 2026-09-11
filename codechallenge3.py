#Package Details (INPUT)

print("=========================================")
name = input("Sender Name: ")
itemtype = input("Type of Item: ")
is_Fragile = bool(input("Is the Item Fragile or Not? (Enter \"yes\" if yes, enter \"no\" if no): ") == "yes")
weight = float(input("Weight (kg): "))
distance = float(input("Distance (km): "))

is_International = bool(input("International? (Enter \"yes\" if yes, enter \"no\" if no): ") == "yes")
is_Express = bool(input("Express? (Enter \"yes\" if yes, enter \"no\" if no): ") == "yes")


#Calculations

base_cost = (weight * 2.50)+(distance * 0.15)

#FREESHIPPING
if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
	print("--Congratulations, you've got FREESHIPPING!!!--")
	total = 0

#INTERNATIONAL/EXPRESS
elif is_International and is_Express:
	print("--International Express is applied--")
	total = (base_cost * 1.40) + 50

#EXPRESS OR HEAVY INTERNATIONAL
elif weight > 20 and is_Express or is_International:
	total =  (base_cost * 1.20) + 25
	print("--Express or Heavy International is applied--")

#OVERSIZED
elif weight > 30 or distance > 1000:
	print("--Your Product is Oversized--")
	total = (base_cost) + 30
else:
	total = base_cost
	print(--"Oversized is applied--")

ShippingFee = total - base_cost

print("========================================")
print("DJ'S EXPRESS COMPANY ORDER SUMMARY")
print("----------------------------------------")
print("NAME: ", name)
print("ITEM: ", itemtype)
print("WEIGHT: ", weight)
print("DISTANCE: ",distance)
print("FRAGILE? ",is_Fragile)
print("INTERNATIONAL? ",is_International)
print("EXPRESS?", is_Express)
print("TOTAL: ", total)
print("/nThe total shipping cost: ", ShippingFee)
print("========================================")



