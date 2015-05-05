import sys

if(len(sys.argv) != 4):
    print('Format -> python3 postprocessmegam.py <INPUT_FILE> <CLASS1> <CLASS2>')
    sys.exit()

inputfilename = sys.argv[1]
class1 = sys.argv[2]
class2 = sys.argv[3]

with open(inputfilename) as inputfile:
    for line in inputfile:
        line = line.rstrip('\n')
        splitstr = line.split('\t')
        value = int(splitstr[0])
        if(value == 1):
            print(class1)
        else:
            print(class2)
