infile = open("sean_test.txt", "r")

lines = []
for line in infile.readlines():
    lines.append(line)
print(len(lines))
