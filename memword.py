#!/usr/bin/python
print "\n\n"
word_n = int(raw_input("\033[1;31mWhat is your memory word's number?\033[1;m "))
word_v = int(raw_input("\033[1;32mWhat is the value of the word? \033[1;m"))
v = 0
getBin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
total = (getBin(int(word_v)))
print "\n" + total + "\n"
lst=[int(i) for i in str(total)]
lst.reverse()

if word_v < 65536:
	for bit in lst:
		if lst[v] == 1:
			print "\t\t\033[1;36mMB" + str(word_n) + format(v, 'x') + " is ON\033[1;m"
			v += 1
		else:
			v += 1
else:
	for bit in lst:
		if lst[v] == 1:
			if v < 16:
				print "\t\t\033[1;36mMB" + str(word_n) + format(v, 'x') + " is ON\033[1;m"	
			else:
				print "\t\t\033[1;36mMB" + str((word_n)+1) + format(v-16, 'x') + " is ON\033[1;m"
			v += 1
		else:
			v += 1
