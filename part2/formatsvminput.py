import sys
import os
import json


if(len(sys.argv) != 5):
    print('Format -> python3 formatsvminput.py <DIR> <CLASS1> <OUT_TRAIN_FILE> <MODE>')
    sys.exit()

trainingdir = sys.argv[1]
class1 = sys.argv[2]
outputfilename = sys.argv[3]
mode = sys.argv[4]

if(not os.path.isdir(trainingdir)):
    print(trainingdir + ' is not a directory.')
    sys.exit()

outputfile = open(outputfilename, 'w')

files = os.listdir(trainingdir)
if(mode == 'training'):
    vocab = {}
else:
    with open('vocab.json', 'r') as vocabfile:
        vocab = json.load(vocabfile)
index = 0

for f in sorted(files):

    trainingfilepath = trainingdir + os.path.sep + f
    with open(trainingfilepath, 'r', errors='ignore') as trainingfile:
        if(mode == 'training'):
            splitstring = f.split('.')
            label = splitstring[0]
            if(label == class1):
                outputfile.write('+1 ')
            else:
                outputfile.write('-1 ')
        else:
            outputfile.write('+1 ')

        feature_counts = {}
        features = []
        for line in trainingfile:
            features.extend(line.rstrip('\n').split(' '))

        for feature in features:
            feature = feature.strip('!@#$%^&*()<>,.?/-_+={}[]\'~`:;1234567890\\\"|')
            if feature not in vocab:
                index = index + 1
                vocab[feature] = index
            feature_counts[vocab[feature]] = feature_counts.setdefault(vocab[feature], 0) + 1

        feature_indexes = feature_counts.keys()
        for index in sorted(feature_indexes):
            outputfile.write(' ' + str(index) + ':' + str(feature_counts[index]))

    outputfile.write('\n')

with open('vocab.json', 'w+') as vocabfile:
    json.dump(vocab, vocabfile)
