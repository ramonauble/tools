
#   txtToBin
#   converts a string of text into a formatted series of binary ASCII strings
#       optional integer shift allows for "encryption" before  conversion
#   by rae
#   5-26-24 | 5:something pm

charToInt = ['(' ,')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
          '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
          'Y', 'Z', '[', '$', ']', '^', '_', '`', 'a', 'b', 'c', 'd',
          'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

strMap = ['○','□','△','x','◎︎','▣','◬',"+"]

outputString = open("output.txt", "wt")   #open output text file in wt mode for writing
                                          #create if not present
                                          #overwrite if already exists
rows = 0;

print("")
inputString = input("Enter a string to convert (no spaces pls ;_;): ")
bytesPerRowT = input("Enter the number of bytes per row: ")
bytesPerRow = int(bytesPerRowT)
offsetValsT = input("Would you like to offset the ASCII character values by an arbitrary integer? (y/n): ")
if (offsetValsT == "y"):
    offsetVal = input("Enter the integer offset: ")
    offsetNum = int(offsetVal)
else:
    offsetNum = 0
base = input("Would you like the output to be in decimal, octal or binary format? (d: decimal | o: octal | b: binary): ")
if (base == "o"):
    remap = input("Would you like to remap the octal values? (y/n): ")

def outputByte(fRow, fX):
    if (row > 0):
        print('{0:08b}'.format(charToInt.index(inputString[(fRow * bytesPerRow) + fX]) + 40 + offsetNum, end=" "))
        outputString.write('{0:08b}'.format(charToInt.index(inputString[(fRow * bytesPerRow) + fX]) + 40 + offsetNum, end=" "))
    else:
        print('{0:08b}'.format(charToInt.index(inputString[(fX * fRow) + fX]) + 40 + offsetNum, end=" "))
        outputString.write('{0:08b}'.format(charToInt.index(inputString[(fX * fRow) + fX]) + 40 + offsetNum, end=" "))
    outputString.write(" ")

def outputOct(fRow, fX):
    if (row > 0):
        outputBuf = '{0:03o}'.format(charToInt.index(inputString[(fRow * bytesPerRow) + fX]) + 40 + offsetNum, end=" ")
        if (remap == "y"):
            inputBuf = list("aaa")
            inputBuf[0] = strMap[int(outputBuf[0])]
            inputBuf[1] = strMap[int(outputBuf[1])]
            inputBuf[2] = strMap[int(outputBuf[2])]
            outputBuf = "".join(inputBuf)
        print(outputBuf)
        outputString.write(outputBuf)
    else:
        outputBuf = '{0:03o}'.format(charToInt.index(inputString[(fX * fRow) + fX]) + 40 + offsetNum, end=" ")
        if (remap == "y"):
            inputBuf = list("aaa")
            inputBuf[0] = strMap[int(outputBuf[0])]
            inputBuf[1] = strMap[int(outputBuf[1])]
            inputBuf[2] = strMap[int(outputBuf[2])]
            outputBuf = "".join(inputBuf)
        print(outputBuf)
        outputString.write(outputBuf)
    outputString.write(" ")

def outputDec(fRow, fX):
    if (row > 0):
        print('{0:03}'.format(charToInt.index(inputString[(fRow * bytesPerRow) + fX]) + 40 + offsetNum, end=" "))
        outputString.write('{0:03}'.format(charToInt.index(inputString[(fRow * bytesPerRow) + fX]) + 40 + offsetNum, end=" "))
    else:
        print('{0:03}'.format(charToInt.index(inputString[(fX * fRow) + fX]) + 40 + offsetNum, end=" "))
        outputString.write('{0:03}'.format(charToInt.index(inputString[(fX * fRow) + fX]) + 40 + offsetNum, end=" "))
    outputString.write(" ")

for row in range(0, len(inputString)//bytesPerRow):
    rows = row;
    for x in range(0, bytesPerRow):
        if (base == "b"):
            outputByte(row, x)
        elif (base == "o"):
            outputOct(row, x)
        elif (base == "d"):
            outputDec(row, x)
    print("")
    outputString.write("\n")
if (len(inputString)%bytesPerRow != 0):
    for x in range(0, len(inputString)%bytesPerRow):
        if (base == "b"):
            outputByte(row, x)
        elif (base == "o"):
            outputOct(row, x)
        elif (base == "d"):
            outputDec(row, x)




#for x in range(256):                #x = [0, 255] - runs 256 times
    #y = x                           #output = input - 1:1 linear function
    #gen_wv.write(str(y))            #output result to file
    #if (x < 255):                   #if not last value
        #if (((x + 1) % 16) == 0):       #if 16th value in row
            #gen_wv.write(",")               #add comma and no space - end of line
            #gen_wv.write("\n")              #add newline to proceed to next row
        #else:                           #else (values 1-15)
            #gen_wv.write(", ")               #add comma and space for value separation 
outputString.close()                      #close file - operation finished
    
    
    
    
