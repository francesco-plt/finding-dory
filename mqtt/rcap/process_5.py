# mosquitto_sub -h 131.175.120.117 -t '#' -v > mqtt_5.txt

d = []

with open("mqtt_5.txt") as f:
	for l in f:
		d.append(l.split(' ', 1))

print("Total MQTT messages: ", len(d))
t = {}
for l in d:
	#print("l: ", l)
	old = t.get(l[0], [])
	if l[1] not in old:
		t[l[0]] = old + [l[1]]

#print(d)

for k in d:
	#print(len(k), k[0], k[1:])
	pass
	
#print("\n*****noises*****")
noises = []
for l in d:
	if 'noise' in l[0]:
		#print(l)
		# noises are all useless
		noises.append(l[0])
		pass

for n in noises:
	t.pop(n, None)

print("\n\n*****de-noised*****\n")
	
for k, v in sorted(t.items()):
	print(len(v), k, v)

