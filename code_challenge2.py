#a = 1000
#b = 500
#c = 200
#d = 100
#e = 50
#f = 20
#g = 10
#h = 5
#i = 1

money = 6456

print("Money to deposit -->", money)

a = money//1000
money = money - a*1000

print("Amount of 1000:", a)

b = money//500
money = money - b*500

print("Amount of 500:", b)

c = money//200
money = money - c*200

print("Amount of 200:", c)

d = money//100
money = money - d*100

print("Amount of 100:", d)

e = money//50
money = money - e*50

print("Amount of 50:", e)

f = money//20
money = money - f*20

print("Amount of 20", f)

g = money//10
money = money - g*10

print("Amount of 10", g)

h = money//5
money = money - h*5

print("Amount of 5", h)

i = money//1
money = money - i*1

print("Amount of 1", i)


