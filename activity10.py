a = 7
b = 3
c = 10

print( a > b or c < a )
print( a > b or c < a and c == b )
print( c < a and c == b )

print( not(a > b or c < a and c == b ))