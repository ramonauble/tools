#   freq_gen
#   generates a formatted table of frequencies
#	within a bipolar semitone range, around middle A (440hz)
#	expressed as integer approximations (for use in SP)
#   by ramona a d+w-b
#   7-21-20
#   >+>.>|/^\|<.<+<
#   _______
#   --___--
#     |||___-π-___...
#     |||---|-|---|||
#    / π \       / π \
#    \___/       \___/

gen_freq = open("freqs.txt", "wt") 	#open frequency table text file in wt for writing
                                    #create if not present
                                    #overwrite if already exists

refFreq = 440.0						    #reference frequency - A440 - float for accuracy

for st_offset in range(-48, 48):            #-/+ 4 octaves around reference frequency
    pitch = refFreq * (2**(st_offset/12))   #calculates pitch accounting for reference frequency & semitone offset
    gen_freq.write(str(int(pitch)))         #converts pitch to an integer before converting to a string, then writes to file
    
    if (st_offset < 47):                    #if not last pitch
        if (((st_offset + 1) % 12) == 0):       #writes comma & newline only after every full octave
            gen_freq.write(",")
            gen_freq.write("\n")
        else:                               #else
            gen_freq.write(", ")                #writes comma & space after every pitch within the octave
            
gen_freq.close()                        #close frequency table text file
    
    
    





