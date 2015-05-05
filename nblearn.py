import sys
import json

# Check if arguments are passed correctly
if(len(sys.argv) < 3):
    print('Format -> python3 nblearn.py TRAININGFILE MODELFILE')
    sys.exit()

# Get the TRAININGFILE and MODELFILE
trainingfilepath = sys.argv[1]
modelfilepath = sys.argv[2]

# Open TRAININGFILE for reading
trainingfile = open(trainingfilepath, 'r', errors='ignore')

model = {}
class_count = {}
feature_count = {}
word_count = {}
prior_probability = {}
vocabulary = set()

# Go through file and count reqd statistics
for line in trainingfile.readlines():
    model['doc_count'] = model.setdefault('doc_count', 0) + 1

    features = line.rstrip('\n').split(' ')
    label = features[0]
    class_count[label] = class_count.setdefault(label, 0) + 1

    class_feature = feature_count.setdefault(label, {})
    class_word_count = word_count.setdefault(label, 0)

    for feature in features[1:]:
        feature = feature.strip('!@#$%^&*()<>,.?/-_+={}[]\'~`:;1234567890\\\"|')
        class_word_count = class_word_count + 1
        class_feature[feature] = class_feature.setdefault(feature, 0) + 1
        vocabulary.add(feature)
    word_count[label] = class_word_count
    feature_count[label] = class_feature

for label in class_count:
    prior_probability[label] = class_count[label]/model['doc_count']

model['class_count'] = class_count
model['feature_count'] = feature_count
model['word_count'] = word_count
model['prior_probability'] = prior_probability
model['vocab_count'] = len(vocabulary)
# Write JSON dump to model file
with open(modelfilepath, 'w+') as modelfile:
    json.dump(model, modelfile)
