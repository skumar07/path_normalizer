def normalize_string(s):
    stack1 = [] # Holds the '/' that needs to be put in the final path
    stack2 = [] # Holds the directory names that need to be put into the final path
    tempstring = ""
    finalstring = ""
    counter = 0

    for i in range(len(s)):
        char = s[i]         # Each character in the input path

        if i == len(s) - 1:
            stack2.append(tempstring + char)    # Append all directory names to stack2

        if char == "/":
            stack2.append(tempstring) # Appends directory name
            stack1.append(char) # Appends '/'
            tempstring = "" 

        elif char == ".":
            try:
                counter += 1
                if counter == 1:
                    stack1.pop() # Gets rid of the first '/'
                else:
                    stack2.pop() # Gets rid of parent directory
                    stack1.pop() # Gets rid of '/' in front of removed parent directory
            except:
                raise Exception("Bad input string")
        else:
            tempstring += char # Makes the string of the directory 
            
    for i in range(len(stack1)):
        finalstring += stack2[i] + stack1[i]

    return finalstring + stack2[-1]




        
                
            
        
