import sys

my_name = sys.argv[0]
return_line = ""

f = open(my_name, 'r')
for line in f:
    for var in line[::-1]:
        return_line += var
        if len(return_line) == len(line):
            print(return_line)
    return_line = ""
f.close()
