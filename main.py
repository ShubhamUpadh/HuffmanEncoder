import os
import sys

class Huffman:
    def __init__(self,fileName):
        self.fileName = fileName + '.txt'
    def fileCheck(self):
        #print(self.fileName)
        if not os.path.isfile(self.fileName):
            print("File doesn't exist")
            sys.exit()
        else:
            print("File exists")
#print(sys.argv[1])
huffman = Huffman(sys.argv[1])
huffman.fileCheck()