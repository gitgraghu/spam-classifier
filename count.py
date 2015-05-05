import sys


def fscore(precision, recall):
    return ((2*precision*recall)/(precision+recall))

if(len(sys.argv) != 5):
    print("Format -> python3 count.py <OUT_FILE> <CLASS1COUNT> <CLASS1> <CLASS2>")
    sys.exit()

outfile = sys.argv[1]
class1_count = int(sys.argv[2])
class1 = sys.argv[3]
class2 = sys.argv[4]

count = 0
class1count = 0
class2count = 0
totalclass1 = 0
totalclass2 = 0

with open(outfile, 'r') as f:
    for line in f:
        count = count + 1
        if(count <= class1_count):
            if(line.rstrip("\n") == class1):
                class1count = class1count + 1
                totalclass1 = totalclass1 + 1
            elif(line.rstrip("\n") == class2):
                totalclass2 = totalclass2 + 1
        else:
            if(line.rstrip("\n") == class2):
                class2count = class2count + 1
                totalclass2 = totalclass2 + 1
            elif(line.rstrip("\n") == class1):
                totalclass1 = totalclass1 + 1

print("NUM OF DOCS: " + str(count))
print(class1 + " COUNT: " + str(class1count))
print(class2 + " COUNT: " + str(class2count))
print("TOTAL " + class2 + ": " + str(totalclass1))
print("TOTAL " + class1 + ": " + str(totalclass2))
class1precision = class1count/(totalclass1)
class1recall = class1count/(class1_count)
class2precision = class2count/(totalclass2)
class2recall = class2count/(count - class1_count)
class1Fscore = fscore(class1precision, class1recall)
class2Fscore = fscore(class2precision, class2recall)

print(class1 + " precision: " + str(class1precision))
print(class1 + " recall: " + str(class1recall))
print(class2 + " precision: " + str(class2precision))
print(class2 + " recall: " + str(class2recall))
print(class1 + " F-score: " + str(class1Fscore))
print(class2 + " F-score: " + str(class2Fscore))
