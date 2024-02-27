import os
import sys

class Huffman:
    
    def __init__(self,fileName):
        self.fileName = fileName + '.txt'
        self.charFreq = {}      # We are storing this as a dictionary, it can be optimised to an array ????
    
    def fileCheck(self):
        #print(self.fileName)
        if not os.path.isfile(self.fileName):
            print("File doesn't exist")
            sys.exit()
        else:
            print("File exists")
    
    def charCount(self):
        with open(self.fileName,'r',encoding='utf-8') as file:
            while True:
                char = file.read(1)
                if char in self.charFreq:
                    self.charFreq[char] += 1
                else:
                    self.charFreq[char] = 1
                if not char:
                    break
                #print(char)
        print(self.charFreq['X'],self.charFreq['t'])
    
#print(sys.argv[1])
huffman = Huffman(sys.argv[1])
huffman.fileCheck()
huffman.charCount()