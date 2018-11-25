#censorship program
def illegalWord(word):
    filename = 'exercise_12.txt'
    text = open(filename, 'r')
    censors = []
    for x in text.readlines():
        censors.append(x)
    for i in range(len(censors)):
         censors[i] = censors[i].strip('\n')
    for cen in censors:
        print(cen)
        if word == cen:
            return True
def main():
    filename = 'exercise_11.txt'
    infile = open(filename, 'r')
    outfile = open('exercise_11(1).txt', 'w')
    
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if illegalWord(words[i]):
                words[i] = '****'
        line = ' '.join(words)
        print((line), file = outfile)
    infile.close()
    outfile.close()

main()

