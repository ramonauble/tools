
#   posFinder
#   finds the center point XYZ locations for n objects evenly distributed over a length m
#       for use with blender (or whatever)
#   by rae
#   6-1-24 | 4:something pm

outputFile = open("posFinder.txt", "wt")  #open output text file in wt mode for writing
                                            #create if not present
                                            #overwrite if already exists
rows = 0;

objectCount = int(input("How many objects you got, bub?: "))
objectWidth = float(input("Okay, great stuff. How wide is each object? (in mm): "))
objectSpace = float(input("Cool beans. How much space between each object? (in mm): "))
axis = input("Got it. Which axis should they be distributed on? (x, y, z): ")
direction = input("Nice - should that be positive or negative going? (+/-): ")
objectOffset = 0
offsetTrue = input("Should the objects be offset from the starting position? (y/n): ")
if (offsetTrue == "y"):
    objectOffset = float(input("By how much? (in mm): "))
objectGroup = 0
groupSpace = 0
groupTrue = input("Should the objects be grouped (have an extra space inserted every n objects)? (y/n): ")
if (groupTrue == "y"):
    groupCount = int(input("Okay - how many objects in each group? (0: no grouping | 1+: objects in group): "))
    groupSpace = float(input("And by how much should each group be spaced? (in mm): "))
xStart = float(input("Alright pal. What is the X position of the starting point?: "))
yStart = float(input("What's the starting Y position?: "))
zStart = float(input("And the starting Z?: "))
index = {"x":xStart, "y":yStart, "z":zStart}
objCnt = 0
print("Okay. Let's roll.")

if (direction == "+"):
    index[axis] += objectOffset
elif (direction == "-"):
    index[axis] -= objectOffset

for objSel in range(objectCount): #loop over each object
    if (groupTrue == "y"):
        if (objCnt < groupCount):
            objCnt+= 1
        else:
            if (direction == "+"):
                index[axis] += groupSpace
            elif (direction == "-"):
                index[axis] -= groupSpace
            #print(str(objCnt))
            objCnt = 0
    print("object " + str(objSel) + ": " + '{0:04f}'.format(index["x"]) + ", " + '{0:04f}'.format(index["y"]) + ", " + '{0:04f}'.format(index["z"]))
    outputFile.write("object " + str(objSel) + ": " + '{0:04f}'.format(index["x"]) + ", " + '{0:04f}'.format(index["y"]) + ", " + '{0:04f}'.format(index["z"]))
    outputFile.write("\n")
    
    if (direction == "+"):
        index[axis] += (objectWidth + objectSpace)
    elif (direction == "-"):
        index[axis] -= (objectWidth + objectSpace)





#for x in range(256):                #x = [0, 255] - runs 256 times
    #y = x                           #output = input - 1:1 linear function
    #gen_wv.write(str(y))            #output result to file
    #if (x < 255):                   #if not last value
        #if (((x + 1) % 16) == 0):       #if 16th value in row
            #gen_wv.write(",")               #add comma and no space - end of line
            #gen_wv.write("\n")              #add newline to proceed to next row
        #else:                           #else (values 1-15)
            #gen_wv.write(", ")               #add comma and space for value separation 
outputFile.close()                      #close file - operation finished
    
    
    
    
