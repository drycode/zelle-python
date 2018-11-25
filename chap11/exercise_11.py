#censorship program

def main():
    filename = 'exercise_11.txt'
    infile = open(filename, 'r')
    outfile = open('exercise_11(1).txt', 'w')
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 4:
                words[i] = '****'
        line = ' '.join(words)
        print((line), file = outfile)
    infile.close()
    outfile.close()

main()

