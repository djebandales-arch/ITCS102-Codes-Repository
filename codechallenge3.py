#INPUTS

name = input("Sender Name: ")
itemtype = input("Type of Item: ")

is_Fragile = bool(input("Fragile or Not: "))

if is_Fragile == True:
	print("It is Fragile")
else :
	print("--It is Not Fragile--")

weight = float(input("Weight in kg: "))

distance = float(input("Distance in km: "))


is_Express = bool(input("Express? "))

if is_Express == True:
	print("--Priority--")
else :
	print("--Not Priority--")

is_International = bool(input("International? "))

if is_International == True:
	print("--International--")
else:
	print("--Not International--")

#expected output

base_cost = (weight * 2.50) + (distance * 0.15)
if base_cost == 

#shipping
shipping = wi


