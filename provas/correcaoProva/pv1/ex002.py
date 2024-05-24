a = True
b = False
c = True
x = 10
y = 8
z = 10

print(f'A) {x<(y-10)}')
print(f'B) {not(a and c) and (a or b)}')
print(f'C) {not(a) and not(b) or (y <= z)}')
print(f'D) {not(x == y) or (a and c)}')
print(f'E) {(x<y) and not(a or b or c)}')
print(f'F) {(z>(x+y)) or (a or b)}')
