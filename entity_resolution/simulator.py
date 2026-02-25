import pandas as pd
import random
import string
import os

class Phonebooks:
    """
    A class for generating fake phonebooks for testing purposes.
    """
    def __init__(self, names:str, count:int, error=0.1):
        """
        Create a phonebook, and two duplicates with errors for training purposes.
        names:str is the source file for your list of names. It does not make a distinction between first and last.
        count:int is the number of first/last name pairs you want to generate.
        error:float is the rate of errors, from 0 to 1. A rate of 0.5 would mean every other character in a name, on average, would be replaced.
        """
        self.original=None
        self.genBook(path=names, count=count)
        self.error1=self.original
        self.error2=self.original
        self.error1=self.error1.map(lambda x: mistake(x,error))
        self.error2=self.error2.map(lambda x: mistake(x,error))

    def genBook(self,path:str,count:int):
        """generate the original list of names"""
        first=[]
        last=[]
        with open(path) as f:
            names=f.read()
            lnames=names.lower().splitlines(False)
        for i in range(count):
            first=first+[lnames[random.randrange(0, len(lnames))]]
            last=last+[lnames[random.randrange(0, len(lnames))]]
        self.original=pd.DataFrame({'First':first, 'Last':last})

def mistake(name,error):
    """"
    A function that applies random errors to a string.
    """
    new=name
    i=0
    for char in range(len(name)):
        check=random.uniform(0,1)
        if check>error:
            type=3
        else:
            type=random.randrange(3)
        if type==3:
            i+=1
        elif type==2:#deletion
            new=new[:i]+new[i+1:]
        elif type==1:#replacement
            i+=1
            new=new[:i]+random.choice(string.ascii_lowercase+"*")+new[i+1:]
        elif type==0:#insertion
            new=new[:i]+random.choice(string.ascii_lowercase+"*")+new[i:]
            i+=2
        #print(new)
        #print("---")
    return new

if __name__ == "__main__":
    path=path=os.path.join("data","names.txt")
    books=Phonebooks(names=path,count=20,error=0.1)