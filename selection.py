#!/usr/bin/python
import sys


def selection(fo1,fo2):
	for line in fo1:
		line = line.strip()
		if "GH" in line:
			fo2.write(line + '\t' + 'Glycoside Hydrolases' + '\n')
		elif "GT" in line:
			fo2.write(line + '\t' + "GlycosylTransferases" + '\n')
		elif "PL" in line:
			fo2.write(line + '\t' + "Polysaccharide Lyases" + '\n')
		elif "AA" in line:
			fo2.write(line + '\t' + 'Auxiliary Activities' + '\n')
		elif "CE" in line:
			fo2.write(line + '\t' + 'Carbohydrate Esterases' + '\n')

f1 = open(sys.argv[1],'r') 
f2 = open(sys.argv[2],'w')

selection(f1,f2)

f1.close()
f2.close()