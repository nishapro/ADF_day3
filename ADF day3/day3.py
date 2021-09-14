"""
import packages
"""
import sys                                   # a module for command line
import logging                               # for showing flow of program
import re                                    # used for regular expression operation
import uuid                                  # used for generating random id's in python
from collections import Counter              # for using of container data types
class fileReadWrite:
    """
    It is a class for implementing read and write operations in python.
    """
    def __init__(self,filename):
        """
        this is a function for initialising the constructor for file read and write operations.
        """
        self.filename=filename
        self.words=[]
        self.text=""


    def read_file(self):
        """
        this is a function which is to read a file and slit the data into words and append to a list
        """
        try:
            file=open(self.filename,'r+',encoding='utf-8', errors='ignore')
            data=file.readlines()
            file.close()
        except :
            logging.error("exceptions occurred here")
            for word in data:
                self.words.extend(word.split())
                logging.info('file reading and splitting into words')
                logging.info(self.words)


    def write_file(self):
        """
        this  is a funtion that is used to write the output in a output file
        """
        try:
            outfile=open('self.text','w')
            outfile.write("-".join(self.words)+'\n')
            logging.info('file written in the output file successfully')
            outfile.close()
        except:
            logging.error("exception occurred")


class StringOperations(fileReadWrite):
    """ A class for functional operation"""
    def split_vowel(self):
        """
        this funtion is to split the words in the list based on vowels
        """
        vowels=[]
        try:
            for i in range(len(self.words)):
                res=(re.split('a|e|i|o|u|A|E|I|O|U',self.words[i]))
                vowels=vowels.append(res)
            logging.info("splitting word if vowels occured")
            logging.info("vowels")
            self.words=vowels[:]
        except:
            logging.error("exceptions occurred for spliting vowels: ")


    def index_word(self):
        """
        to create dictionary which are having index as key and word as a value.
        """
        logging.info("counter for index and word as values")
        return dict(enumerate(self.words))


    def unique_list(self):
        """
        for converting each word into unique list.
        """
        logging.info("unique list")
        return list(set(self.words))


    def most_repeated(self):
        """
        this funtion is to Print the word that was repeated maximum number of times.
        """
        try:
            logging.info("most repeated word in the given input file")
            self.index_count=Counter(self.words)
            return self.index_count.most_common(1)[0][0]
        except:
            logging.error("exceptions occurred for most repeated: ")


    def caps_third_alphabet(self):
        """
        this funtion is to Capitalize 3rd letter of every word
        """
        try:
            for i in range(len(self.words)):
                if len(self.words[i])>=3:
                    l=list(self.words[i])
                    l[2]=l[2].upper()
                    self.words[i]=''.join(l)
            logging.info("capitalizing every 3rd letter of a word")
            logging.info(self.words)
        except:
            logging.error("exceptions occurred for capitalisation of 3rd alphabet: ")

    def caps_every_fith_word(self):
        """
        this funtion is to Capitalize every 5th word in the given input file.
        """
        try:
            for i in range(4,len(self.words),5):
                self.words[i]=self.words[i].upper()
            logging.info("capitalizing every fifth word")
            logging.info(self.words)
        except:
            logging.error("exception occurred : ")

    def semi_colon_replace(self):
        """
         this funtion is to Use ; (semi-colon) for new line
        """
        try:
            logging.info("replacing the new line character with semi colon")
            for i in range(len(self.words)):
                self.words[i] = self.words[i].replace('\n', ';')
        except:
            logging.error("exception occurred : ")

    def starts_with_to(self):
        """
        this funtion is to print the word nd their length
        starting with 'to or To' in the input file.
        """
        count=0
        try:
            for word in self.words:
                if word.startswith("to") or word.startswith("To"):
                    count+=1
        except:
            logging.error("exception occurred for starting with to: ")

        return count


    def ends_with_ing(self):
        """
        Print the number of words ending with “ing” in the input file
        """
        count=0
        try:
            for i in self.words:
                if i.endswith("ing"):
                    count+=1
        except:
            logging.error("exceptions occurred for ending with ing: ")
        return count


    def is_palindrome(self):
        """
        this funtion is to Print the palindrome present in the file.
        """
        palindrome=[]
        try:
            for word in self.words:
                if word==word[::-1] and len(word)>1:
                    palindrome.append(i)
        except:
            logging.error("exceptions occurred for palindrome: ")
        return palindrome


    def unique_file_name(self):
        """
        this funtion is to Output file name should be generated with unique name.
        """
        try:
            logging.info("unique file creation")
            self.words=' '.join(self.words).split()
            self.text=str(uuid.uuid4())
            self.text+='.txt'
            self.write_file()
        except:
            logging.error("exceptions occurred for unique file name: ")
if __name__=="__main__":
    logging.basicConfig(filename="Adf_day3.txt", filemode='a',
                        format='%(asctime)s %(levelname)s-%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fileobj = StringOperations(sys.argv[1])
    fileobj.read_file()
    fileobj.write_file()
    print(fileobj.starts_with_to())
    print(fileobj.ends_with_ing())
    print(fileobj.most_repeated())
    print(fileobj.is_palindrome())
    print(fileobj.unique_list())
    print(fileobj.index_word())
    fileobj.split_vowel()
    fileobj.caps_third_alphabet()
    fileobj.caps_every_fith_word()
    fileobj.semi_colon_replace()
    fileobj.unique_file_name()
    