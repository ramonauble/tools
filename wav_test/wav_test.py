#---------------------------------------------
#wav_test
#by ramona a •w•          
#7-25-20                  helper program to validate file operations        
#><>|^*^|<><              ---------------------------------------------------------
#_______                  • this program compares the header chunks of 2 wav files
#--___--                    • prints "all good!" if same (byte-for-byte)
#  |||___-π-___...          • prints "ruh roh..." for compare mismatch (not the same)
#  |||---|||---|||        
# / π \       / π \       
# \___/       \___/     
#---------------------------------------------

file1 = open("sample1.wav", mode = "rb")
file2 = open("sample2.wav", mode = "rb")

header1 = file1.read(44)
header2 = file2.read(44)

b2Index = 0
same = 1 #assumes headers are the same; cleared only on compare mismatch

for byte1 in header1:   
    if(byte1 != header2[b2Index]):  #compare mismatch
        same = 0
        break
    b2Index+= 1
    
if (same):
    print("all good!")
else:
    print("ruh roh...")
    