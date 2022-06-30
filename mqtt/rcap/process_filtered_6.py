coap_pos = [[10, 6], [2, 10], [4, 8], [8, 0], [4, 4], [2, 6], [6, 0], [4, 10], [0, 6], [2, 4], [0, 4], [8, 8], [6, 8], [4, 0], [6, 2], [8, 10], [6, 10], [2, 2], [10, 10], [10, 0], [0, 2], [8, 2]]

with open("manual_filter_6.txt") as f:
	mqtt_pos = []
	for l in f:
		mqtt_pos += [list(map(int, map(float, l.split('|', 1)[0].split(",", 1))))]
	
	print("mqtt_pos: ", mqtt_pos, "of len ", len(mqtt_pos))
	
	duplicates = False
	for m in mqtt_pos:
		if m in coap_pos:
			print("[WARNING] position ", m, "both in mqtt and in coap")
			duplicates = True
	print("mqtt, coap duplicate check: ", duplicates)
	
	
	holes = []
	for y in range(10, -1, -1):
			print("\n\t{}\t".format(y), end="")
			for x in range(0,11, 1):
				if x % 2 == 1 or y % 2 == 1:
					print("     ", end="") 
				elif [x, y] in mqtt_pos:
					print(" [M] ", end="")
				elif [x, y] in coap_pos:
					print(" [C] ", end="")
				else:
					print(" [ ] ", end="")
					holes.append([x,y])
			print("\n", end="")
	print("\n\t\t", end="")
	for x in range(0,11,1):
		print("  {}  ".format(x), end="")
	print("\n", end="")
	print("holes: ", holes, "of count", len(holes))
