# Spellchecker takes file input and checks each word against dictionary input. Non-dictionary
# words are printed to the screen

class SpellCheck:
    def __init__(self, infile, dictionary):
        self.f_to_check = infile
        self.dict = dictionary
        self.infile = infile
        self.words = []
        self.text = []
        self.read_infile()
        self.read_dict()
        for word in self.text:
            #Accomodates test dictionary (only includes words of length >= 4)
            if len(word) >= 4:
                self.binary_search(self.words, word)

    def read_dict(self):
        with open(self.dict, 'r') as f:
            for word in f.readlines():
                self.words.append(word.strip())
            

    #TODO: Process infile to create a list of words accounting for punctuation and capitalization
    def read_infile(self):
        with open(self.infile, 'r') as f:
            for line in f.readlines():
                words = line.split()
                for word in words:
                    self.text.append(word.strip("!@#$%^&*()'~`><:;,.][}{\|").lower())

    def binary_search(self, arr, inword):
        #Base case: if empty array, inword not in dictionary
        if len(arr) == 0:
            print(inword + " is not in dictionary.")
            return False
        else:
            #Find middle of list, assign value to variable dictword 
            mid = len(arr) // 2
            dictword = arr[mid]
            #if inword in dictionary, return True
            if inword == dictword:
                return True
            else:
                #Initiate variables for top and bottom of list 
                left = arr[:mid]
                right = arr[mid+1:]

                if inword < dictword:
                    return self.binary_search(left, inword)
                else:
                    return self.binary_search(right, inword)
                
            
def main():
    SpellCheck('testdoc.txt', 'eng_dictionary.txt')
main()
        