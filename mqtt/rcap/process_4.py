# mosquitto_sub -h 131.175.120.117 -t '#' -v > mqtt_4.txt

d = []

with open("mqtt_4.txt") as f:
	for l in f:
		d.append(l.split(' ', 1))

print(d, len(d))
t = {}
for l in d:
	print("l: ", l)
	old = t.get(l[0], [])
	if l[1] not in old:
		t[l[0]] = old + [l[1]]

print(d)

for k in d:
	print(len(k), k[0], k[1:])
	
print("\n*****noises*****")
noises = []
for l in d:
	if 'noise' in l[0]:
		print(l)
		# noises are all useless
		noises.append(l[0])

for n in noises:
	t.pop(n, None)

print("\n\n*****de-noised*****\n")
	
for k, v in t.items():
	print(len(v), k, v)

