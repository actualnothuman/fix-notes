import shutil
import os
import string

#### Var 

i = 0 # Search is supposed to prefer directories over files. 
dir_path = "/home/user/obsidian" # Enter where your obsidian dir lies

paragraph = [] # Adds up line for line and joins them, also checks for information for categorization
filename = str(input("Filename of the file you want to fix?: "))
error = [i for i in string.printable] #If the name generation doesnt work it just takes characters from this list (only place where string module is used)
newfile = False
file_path = dir_path + "/" + filename


####


with open(file_path, "a") as f:
    f.write("\n" + "/")

with open(file_path, "r") as f:
    for line in f:

        if newfile and (line != "\n"):
        
        # Creating a new file or appending to an existing one

            print(paragraph[0])
            x = paragraph[0]
            
            if x[:2] == "in":
                
                x = paragraph[0].split()
                filedir = x[1]
                print(filedir + "test")
                i = 0

                for root, dirs, files in os.walk(dir_path):
                    # searchs if file/dir exists already (prefers directiories)
                    
                    if i == 0:
                        for fil in files:
                
                            if fil.find(filedir) != -1:
                                x = str(fil)
                                print(x[-3:])
                                if x[-2:] == "md":
                                    path = root+'/'+fil	
                                    print (path)
                                
                                    print("test1")

                        if i == 0:
                            for di in dirs:
                        
                                if di.find(filedir) != -1:
                                    path = root+'/'+str(di)	
                                    print (path)
                                    i += 1
    


                if i == 0:
                # appended in gefundener Datei
                    with open(path, "a") as n:
                        n.write("\n")
                        n.write("".join(paragraph))
                

                        print("test2")

                elif i >= 0:
                # erstellt file im gefundenen Ordner
                    tag = path.split("/")
                    tag = tag[-1]
                    if (tag[2] == "0") or (tag == "3pa37-xnyty") or (tag == "obsidian"):
                        tag = ""
                    else:
                        tag == "[" + tag + "]"
                    try:
                        with open((path + "/" + (paragraph[1] + ".md")), "x") as n:
                            n.write("\n")
                            n.write("".join(paragraph))
                            n.write(tag)
                    except:
                        with open((path + "/" + error.pop() + ".md"), "x") as n:
                            n.write("\n")
                            n.write("".join(paragraph))
                            n.write(tag)
    

                
                        print("test3")

            else:
            # fügt an todo an, Achtung potenziell Schleife!
                with open(dir_path + "/" + "todo.md", "a") as n:
                    n.write("\n")
                    n.write("".join(paragraph))

                    print("test4")



            paragraph = []
            paragraph.append(line)
            newfile = False



        elif line != "\n":
        # Adding new lines to existing paragraph
            print(paragraph)
            paragraph.append(line)



        else:
        # Empty line shows that paragraph has ended, will be written in file in next step
            newfile = True




















