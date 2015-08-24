#!/usr/bin/python
# encoding = utf8

import csv
import socket, struct
import sys

f = open("dbip-city.csv", "r") #
fout = open("dbip-city2.csv", "w")

def IP2Int(ip):
    o = map(int, ip.split('.'))
    res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
    return res


def ip2int(ip):
    """
    Convert an IP string to unsigned int
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!I", packedIP)[0]               

for row in f:
	# 删除所有的引号，方便后面的处理
	row = row.replace('"', '')
	cells = row.split(",")
	count = len(cells)
	low = ip2int(cells[0])
	hi = ip2int(cells[1])
	res = str(low) + "," + str(hi)

	for i in range(2, count):
		res = res + "," + cells[i];

	fout.write(res);

f.close()
fout.close();

