def main():
	with open("coap_1.txt") as f:
		hits = []
	
		for l in f:
			l = l.split(' ', 2)
			if 'hit' == l[0]:
				hits.append(l[2])
	
		for l in hits:
			print(l)
		print(len(hits), "hits found")
	
		with open("coap_hits_1.txt", "w") as g:
			g.write("".join(hits))
	
		positions = []
		for l in hits:
			positions.append(list(map(int, map(float, l.split("||")[0][:-1].split(',')))))
		print("coap_positions = ", positions)
	
		for y in range(10, -1, -1):
			print("\n\t{}\t".format(y), end="")
			for x in range(0,11, 1):
				if x % 2 == 1 or y % 2 == 1:
					print("     ", end="") 
				elif [x, y] in positions:
					print(" [X] ", end="")
				else:
					print(" [ ] ", end="")
			print("\n", end="")
		print("\n\t\t", end="")
		for x in range(0,11,1):
			print("  {}  ".format(x), end="")
		print("\n", end="")
		
if __name__ == "__main__":
	main()
