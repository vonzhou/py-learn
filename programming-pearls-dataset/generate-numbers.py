#!/usr/bin/python

f = open("numbers.txt", "w");

for i in range(0, 9999999):
	s = str(i)
	s = s.zfill(7)
	s = s + '\n'
	f.write(s)

f.close()


