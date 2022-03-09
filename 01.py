l = []

for i in range(1, 1000):
	if i%3==0 or i%5==0:
		l.append(i)

l = set(l)

q = 0
for u in l:
	q = q+u

print(q)