import csv

f = open('info.csv')
r = csv.reader(f)
g1 = next(r)
g2 = next(r)
print(g1)
print (g2)
f.close()
input('hhhhhhhhhhhhh')
