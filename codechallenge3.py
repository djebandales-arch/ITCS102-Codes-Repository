#Package Details (INPUT)

print("=========================================")
name = input("Sender Name: ")
itemtype = input("Type of Item: ")
weight = float(input("Weight in kg: "))
distance = float(input("Distance in km: "))
is_Fragile = bool(input("Is the Item Fragile or Not? (True/False): "))
is_International = bool(input("International?(True/False) "))
is_Express = bool(input("Express? "))


#Calculations

base_cost = (weight * 2.50)+(distance * 0.15)

#FREESHIPPING
if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
	total = 0

#INTERNATIONAL EXPRESS
elif is_International and is_Express:
	total = (base_cost * 1.40) + 50

#EXPRESS OR HEAVY INTERNATIONAL
elif weight > 20 and is_Express or is_International:
	total =  (base_cost * 1.20) + 25

#OVERSIZED
elif weight > 30 or distance > 1000:
	total = (base_cost) + 30
else:
	total = base_cost

ShippingFee = total - base_cost

print("========================================")
print("EXPRESS COMPANY")
print("NAME: ", name)
print("ITEM: ", itemtype)
print("WEIGHT: ", weight)
print("DISTANCE: ",distance)
print("FRAGILE? ",is_Fragile)
print("INTERNATIONAL? ",is_International)
print("EXPRESS?", is_Express)
print("TOTAL: ", total)
print("The total shipping cost: ", ShippingFee)
print("========================================")



