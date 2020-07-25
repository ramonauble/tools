#   wv_gen
#   an arbitrary sampled waveform generator
#   by ramona a d-w-b
#   7-18-20
#   >+>.>|/+\|<.<+<
#   _______
#   --___--
#     |||___-π-___...
#     |||---|-|---|||
#    / π \       / π \
#    \___/       \___/

gen_wv = open("waveform.txt", "wt") #open wave text file in wd for writing
                                    #create if not present
                                    #overwrite if already exists

for x in range(256):                #x = [0, 255] - runs 256 times
    y = x                           #output = input - 1:1 linear function
    gen_wv.write(str(y))            #output result to file
    if (x < 255):                   #if not last value
        if (((x + 1) % 16) == 0):       #if 16th value in row
            gen_wv.write(",")               #add comma and no space - end of line
            gen_wv.write("\n")              #add newline to proceed to next row
        else:                           #else (values 1-15)
            gen_wv.write(", ")               #add comma and space for value separation 
gen_wv.close()                      #close file - operation finished
    
    
    
    





