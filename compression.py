""" 
Here is the demo how compression works.
We take ceratin word in the form of string and compress/decompress it.
character take atleast 8bits depending upon the machine but can be denoted by certain bits.
This is the main principle of this algorithm.
We take word(included symbols, numbers and blank spaces) and convert into bits.
we get atleast the 50% less occupied compressed data.
"""

from sys import getsizeof
from typing import Set, Dict, List
from math import log

class CompressData:
    def __init__(self, original: str) -> None:
        self._compress(original)

    
    def assign_bits(self, word_set: Set) -> Dict:
        assignment: Dict = {}
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if  numbers not in list(word_set):  
            for i in range(len(word_set)):
                assignment[list(word_set)[i]] = bin(i)

            print(f"Assigned bits to unique characters: {assignment}")
            return assignment

        else:
            raise ValueError("Contains symbols or number")

        
    def _compress(self, word: str) -> int:
        self.number_of_bits: int = round(log(len(word_in_set)) / log(2) + 0.5)
        self.bit_string: int = 1
        self.dict_letters: Dict = self.assign_bits(word_in_set)
        word_in_set: Set = set(word)
            
        for letter in word:
            self.bit_string <<= self.number_of_bits
            self.bit_string |= int(self.dict_letters[letter], 2)

        print(f"\nThe assigned encrypted data: {self.bit_string}")
        print(f"In binary format: {bin(self.bit_string)}")
        print(f"The size of compressed data: {getsizeof(self.bit_string)}")

        if self._decompress():
            print("Decompression is Successful.")

        else:
            raise Exception("something wrong...")
        

    def _decompress(self) -> bool:
        word: str = ""
        keys = list(self.dict_letters.keys())
        values = list(self.dict_letters.values())
        bits_selecting = bin(2**self.number_of_bits - 1)
        for i in range(0, self.bit_string.bit_length()-1, self.number_of_bits):
            bits: int = bin(self.bit_string >> i & int(bits_selecting,2))
            word += str(keys[values.index(bits)])

        print(f"\n\nDecrypted data from compressed data: {word[::-1]}")
        print(f"Size of decrypted data: {getsizeof(word)}")
        
        return word[::-1]

    def __str__(self):
        self._decompress()


if __name__ == "__main__":
    original: str = input("Enter the word(note: any numbers or symbols or blank space is also available)?")
    print(f"\n\nYour original word: {original}")
    print(f"Size of original: {getsizeof(original)}")
    compress: CompressData = CompressData(original)
    print("\n-----------------------------------------------------------------------------------------------")
    print(f"original and decommpredded are the same: {original.upper() == compress._decompress().upper()}") 
    print(f"{(getsizeof(compress.bit_string)/getsizeof(original)) * 100}% reduction of space.") 
