import getpass

username = 'djenelle'
password = 'cuteako'

u = input('Input Username --->  ')
p = getpass.getpass('Input Password --->  ')

if username == u and p == password :
	print('ACCESS GRANTED CUTIE')
else :
	print('ACCESS DENIED SORRY')