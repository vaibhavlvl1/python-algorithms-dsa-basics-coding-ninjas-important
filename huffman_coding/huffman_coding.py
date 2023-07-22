# Imports
import os
import heapq


class Node:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.freq < other.freq
    
    def __eq__(self,other):
        return self.freq == other.freq



class HuffmanCoding:
    def __init__(self,path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}


    ####################### compressing #######################################

    def make_freq_dict(self,text):
        dic = {}
        for letter in text:
            dic[letter] = dic.get(letter,0)+1

        return dic

    def build_heap(self,d):

        for char, freq in d.items():
            node = Node(char,freq)

            heapq.heappush(self.heap,node)

    def build_tree(self):

        while len(self.heap)>1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            node = Node(None,node1.freq + node2.freq)
            node.left = node1
            node.right = node2

            heapq.heappush(self.heap,node)
            
    def build_codes_helper(self,root,bit_string):
        if root is None:
            return ""
        
        if root.char != None:
            self.codes[root.char]=bit_string
            self.reverse_codes[bit_string] = root.char

        self.build_codes_helper(root.left,bit_string+"0")
        self.build_codes_helper(root.right,bit_string+"1")
    
    def build_codes(self):
        root = heapq.heappop(self.heap)

        self.build_codes_helper(root,"")

    def get_encoded_text(self,text):
        enc_text = ""

        for letter in text:
            enc_text += self.codes[letter]

        return enc_text
    
    def get_padded_enc_text(self,text):
        pad_amt_int = 8-(len(text)%8)
        pad_amt_bin = "{0:08b}".format(pad_amt_int)

        pad_right = text+"0"*pad_amt_int
        pad_front = pad_amt_bin+pad_right

        return pad_front
    
    def get_byte_array(self,text):
        byte_array = []

        for i in range(0,len(text),8):
            bit = text[i:i+8]
            byte = int(bit,2)
            byte_array.append(byte)

        return byte_array

    def compress(self):
        file_name,file_ext = os.path.splitext(self.path)
        output_path = file_name+".cbin"

        with open(input_path,"r") as file, open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()
            freq_dict = self.make_freq_dict(text)

            self.build_heap(freq_dict)

            self.build_tree()

            self.build_codes()
            enc_text = self.get_encoded_text(text)
            
            padd_enc_text = self.get_padded_enc_text(enc_text)

            byte_array = self.get_byte_array(padd_enc_text)
            final_bytes = bytes(byte_array)
            output.write(final_bytes)
        return output_path
    
    ############################## decompress ############################################
    def remove_padding(self,text):
        pad_amt_bin = text[:8]
        pad_amt_int = int(pad_amt_bin,2)

        depad_rear = text[:-1*pad_amt_int]

        depad_front = depad_rear[8:]

        return depad_front

    def decode(self,text):
        orig_text = ""
        curr_bit = ""

        for letter in text:
            curr_bit+=letter
            if curr_bit in self.reverse_codes:
                orig_text += self.reverse_codes[curr_bit]
                curr_bit = ""
        return orig_text


    def decompress(self,input_path):
        file_name,file_ext = os.path.splitext(input_path)
        output_path = file_name+".dbin"

        with open(input_path,'rb')as file,open(output_path,'w')as output:
            bit_string = ""
            byt = file.read(1)

            while byt:
                byt = ord(byt)
                bit = bin(byt)[2:].rjust(8,"0")
                bit_string+=bit
                byt = file.read(1)

            depad_enc_text = self.remove_padding(bit_string)
            

            orig_text = self.decode(depad_enc_text)

            output.write(orig_text)








######### Main ####################

input_path = os.getcwd()

input_path+=r"/huffman_coding/sample.txt"

H = HuffmanCoding(input_path)

output = H.compress()

H.decompress(output)