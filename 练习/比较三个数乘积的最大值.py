a = 135
b = 98
c = 129

ab = a * b
ac = a * c
bc = b * c
max = 0

print(ab,ac,bc)

#先找出ab和ac中的最大值
if ab > ac :
    max = ab
else:
    max = ac

#然后用最大值和bc比较
if bc > max:
    max = bc

print(f"{max}")