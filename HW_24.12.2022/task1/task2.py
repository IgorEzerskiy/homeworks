import sys

my_name = sys.argv[0]

f = open(my_name, 'r')
for line in f:
    print(line)
f.close()
