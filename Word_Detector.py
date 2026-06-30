import os

def isword(filename,word):
    with open(filename,"r") as f:
        file_content = f.read()
    if word in file_content.lower():
        return True
    else:
        return False
        
    
if __name__ == "__main__":
    
    A=[]
    word = input("Enter the word you want to find\n")
    dir_contents = os.listdir()
    nfile = 0
    found = 0
    numer_of_word = 0
    for items in dir_contents:
        if items.endswith("txt"):
            found = isword(items,word)
        if (found):
            print(f"Word found in {items}")
            nfile+=1
            A.append(items)
        else: 
            print(f"Word is not found in {items}")
    print("------------ Word detector ------------")
    print(f"The word found in {nfile} files and the files are {A}")

        