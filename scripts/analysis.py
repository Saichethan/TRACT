import csv

f = open("test.tsv", "r") #clean 
reader = csv.reader(f, delimiter="\t")

d = {1:0,2:0, 3:0}
next(reader)
c = 0
for line in reader:
	c = c+1
	#print(type(int(line[2])), c)
	if int(line[2]) is 1:
		d[1] = d[1] + 1
	elif int(line[2]) is 2:
		d[2] = d[2] + 1
	elif int(line[2]) is 3:
		d[3] = d[3] + 1
	else:
		print(line[-1], type(line[-1]))

print(d)
