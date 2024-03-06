import os
import sys
import heapq

class Node:
    def __init__(self,alphabet=None,freq=None):
        self.alphabet = alphabet
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self,other):
        return self.freq < other.freq
    def __eq__(self,other):
        return self.freq == other.freq
    
class Huffman:
    def __init__(self,fileName):
        self.fileName = fileName if fileName[-4:] =='.txt' else fileName + '.txt'
        self.outputFile = self.fileName[:-4] + 'output'+'.txt'   # This will be the output file
        self.charFreq = {}      # We are storing this as a dictionary, it can be optimised to an array ????
        self.heap =[]
        self.root = None        # Store the root of the Binary Tree
        self.codeDict = {}      # Store the codes here
        self.encodedText = ""   # Store the encoded text here
        self.paddedText = ""    # We need to pad the text in order to convert it properly it to binary form
        self.byteArr = []       # This will store the code of each character in byte form
    
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
                if char in self.charFreq and char != "":
                    self.charFreq[char] += 1
                elif char != "":
                    self.charFreq[char] = 1
                if not char:
                    break
                #print(char)
        #print(self.charFreq['X'],self.charFreq['t'])
    
    def createHeap(self):
        # create a binary tree node first for alphabet and its corresponding frequency, and push the node in heap
        for key in self.charFreq:
            alphaFreq = self.charFreq[key]
            btNode = Node(alphabet=key, freq=alphaFreq)
            heapq.heappush(self.heap, btNode)
    
    def buildTree(self):
        # heap created, now start combining the nodes inside the heap to form the tree
        while len(self.heap) > 1:
            smallest1 = heapq.heappop(self.heap)
            smallest2 = heapq.heappop(self.heap)
            newNode = Node(freq = smallest1.freq + smallest2.freq)
            newNode.left = smallest1
            newNode.right = smallest2
            heapq.heappush(self.heap, newNode)
        # This variable will store the root of the Binary Tree
        self.root = heapq.heappop(self.heap)
        #self.printTree(self.root)
    
    def printTree(self,node):
        if node is None:
            return
        q = []
        q.append(node)
        while len(q):
            for i in range(len(q)):
                rt = q.pop(0)
                if rt.left:
                    q.append(rt.left)
                if rt.right:
                    q.append(rt.right)
                print(rt.alphabet,rt.freq, end=", ")
            print("")
    
    def createCodeDictHelper(self,node,currPath):
        # Helper Function for createCodeDict
        if node is None:
            return
        if node.alphabet is not None:
            self.codeDict[node.alphabet] = currPath
        self.createCodeDictHelper(node.left,currPath+"0")
        self.createCodeDictHelper(node.right,currPath+"1")
        return    
    
    def createCodeDict(self): 
        # Use the root of the BT to create the dictionary
        self.createCodeDictHelper(self.root,currPath="")
    
    def encodeText(self):
        # Open the file, read it character-wise and now use the codeDict to convert each character to code
        with open(self.fileName,'r',encoding='utf-8') as file:
            while True:
                char = file.read(1)     # read one character from the the file
                if not char:
                    break # End of file
                self.encodedText += self.codeDict[char]
                #print(char)
    
    def padEncodedText(self):
        # The logic behind padding is that we want to ensure that the conversion to binary is done properly
        # For example, 1001011001 will not be encoded properly as 1 byte = 8 bit so the file will be split as
        # 10010110 and 01
        # Padding will convert this to 10010110 and 01000000
        # Basically we will add extra 0s to ensure that this can be represented as a byte always 
        padding = 8 - len(self.encodedText) % 8
        self.paddedText = "".join(self.encodedText)
        for _ in range(padding):
            self.paddedText += "0"
        # Now we will store the info that we are padding the file
        paddingInfo = "{0:08b}".format(padding)
        #Now we will append this info to the beginning of the file
        self.paddedText = paddingInfo + self.paddedText
    
    def convertToBytes(self):
        # From the padded text, now convert it to bytes
        self.byteArr = []
        for i in range(0,len(self.paddedText),8):
            byte = self.paddedText[i:i+8]
            self.byteArr.append(int(byte,2))
        #print(self.byteArr,"here")
        self.byteArr = bytes(self.byteArr)
        #print(self.byteArr,"here2")
        '''
        for i in range
        '''
    
    def createEncodePaddedTextOutputFile(self):
        self.fileCheck()    # ensure that the file exists
        '''
        self.charCount()
        self.createHeap()
        self.buildTree()
        self.createCodeDict()
        self.encodeText()
        self.padEncodedText()
        self.convertToBytes()
        with open('debug.txt','w') as file:
            file.write(str(self.paddedText))
        print(len(self.encodedText),len(self.paddedText))
        # Now we will encode this file
        '''
        with  open(self.outputFile,'wb') as output:
            self.charCount()    # count the frequency of characters
            self.createHeap()   # create a heap
            self.buildTree()    # build tree using the heap values
            self.createCodeDict()   # create the codes for characters using the Tree
            self.encodeText()   # encode the txt file using the codes from CodeDict dictionary
            self.padEncodedText()   # pad the encoded text
            self.convertToBytes()   # convert the padded encoded text to Bytes 
            output.write(self.byteArr)  # write the ouput file
            print("Writing output file")
    
#print(sys.argv[1])
huffman = Huffman(sys.argv[1])
huffman.createEncodePaddedTextOutputFile()