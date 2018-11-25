# Write a program that solves word jumble problems. 

# Program generates all anagrams of an array, then checks them against 
# a dictionary. The program prints the dictionary word(s) > 4 letters that correspond(s) 
# with the anagram. 

class WordTruer:
    def __init__(self, dictionary, string):
        self.dictionary = dictionary
        self.string = string
        self.anagrams = self.permute(self.string)
        self.twords = []
        self.dwords = []
        self.read_dict()
        
        self.check_anagrams()
        self.summary()

    def read_dict(self):
        with open(self.dictionary, 'r') as f:
            for word in f.readlines():
                self.dwords.append(word.strip())

    def permute(self, s):
        p = []
        if len(s) <= 1:
            p = [s]
        
        else:
            for i, let in enumerate(s):
                for perm in self.permute(s[:i] + s[i+1:]):
                    p += [let + perm] 
        return p
    # TODO: Incorporate gaddag algorithm to speed up check anagrams 
    def gaddag(self):
        pass
        
    def check_anagrams(self):
        for an in self.anagrams:
            if self.binary_search(self.dwords, an):
                self.twords.append(an)

    def binary_search(self, arr, inword):
        #Base case: if empty array, inword not in dictionary
        if len(arr) == 0:
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

    def summary(self):
        for word in self.twords:
            print(word)


WordTruer('eng_dictionary.txt', 'fish')