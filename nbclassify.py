import sys
import json
import math


class NBClassifier():

    def __init__(self, model_obj):
        self.class_count = model_obj['class_count']
        self.doc_count = model_obj['doc_count']
        self.prior_probability = model_obj['prior_probability']
        self.word_count = model_obj['word_count']
        self.vocab_count = model_obj['vocab_count']
        self.feature_count = model_obj['feature_count']

    def classify(self, line):
        max_probability = -float("inf")
        the_class = ''
        for label in self.class_count:
            probability = math.log(self.prior_probability[label])
            for feature in line.split(' '):
                feature = feature.strip('!@#$%^&*()<>,.?/-_+={}[]\'~`:;1234567890\\\"|')
                feature_count = self.feature_count[label].get(feature, 0)
                word_count = self.word_count[label]
                probability = probability + math.log((feature_count + 1)/(word_count + self.vocab_count))
            if(probability > max_probability):
                max_probability = probability
                the_class = label
        return the_class

if __name__ == '__main__':

    if(len(sys.argv) < 3):
        print('Format -> python3 nbclassify.py MODELFILE TESTFILE')
        sys.exit()

    modelfilepath = sys.argv[1]
    testfilepath = sys.argv[2]
    outfilename = modelfilepath.split('.')[0] + '.out'

    model_data = open(modelfilepath)
    model_obj = json.load(model_data)

    classifier = NBClassifier(model_obj)
    with open(testfilepath, 'r') as testfile:
        for line in testfile:
            label = classifier.classify(line)
            print(label)
