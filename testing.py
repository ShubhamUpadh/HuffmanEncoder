import unittest
import os
import sys
import random
import string

class randomStringGen:
    
    def __init__(self):
        self.rString =""
        self.result = {'':1}
    
    def genRandom(self):
        letters = string.ascii_letters +' '
        self.rString = "".join(random.choice(letters) for i in range(20000))
    
    def charFreq(self):
        for i in self.rString:
            if i in self.result:
                self.result[i] += 1
            else:
                self.result[i] = 1
    
    def writeString(self):
        with open(r'baseTests.txt','w',encoding='utf-8') as file:
            file.write(self.rString)
            
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
        #print(self.charFreq)
    
class TestHuff(unittest.TestCase):
    
    def test_String(self):
        randomString = randomStringGen()
        randomString.genRandom()
        randomString.charFreq()
        randomString.writeString()
        
        huffman = Huffman('baseTests')
        huffman.charCount()

        self.assertEqual(sorted(huffman.charFreq.items()),sorted(randomString.result.items()))
        
'''
if __name__ == '__main__':
    unittest.main()
'''