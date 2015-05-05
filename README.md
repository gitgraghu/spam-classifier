## **Part I:**

[1.] Formatting Training Data:

    - python3 formatinput.py <TRAINING_DIR> <TRAINING_FILE> <mode>
    - mode can be training or development.

 > eg: python3 formatinput.py SPAM_training/ spam_training.txt training
        
[2.] Training Data model:

    - python3 nblearn.py <TRAINING_FILE> <MODEL_FILE>
    
 > eg: python3 nblearn.py spam_training.txt spam.nb

[3.] Classify Input Data:

    - python3 nbclassify.py <MODEL_FILE> <TEST_FILE>
    
 > eg: python3 nbclassify.py spam.nb spam_test.txt > spam.out

[4.] Calculating F-score:

    - python3 count.py <OUT_FILE> <CLASS1COUNT> <CLASS1> <CLASS2>

> eg: python3 count.py out 1000 HAM SPAM

## **Part II:**

**(1) SVM:** 

[1.] Formatting Training Data:

    - python3 formatsvminput.py <DIR> <CLASS1> <OUT_TRAIN_FILE> <MODE>
    - mode can be training or development

> eg: python3 formatsvminput.py ../../SPAM_training/ HAM spam_training.txt training

[2.] Training Data Model

    - svm_learn <TRAINING_FILE> <MODEL>

> eg: svm_learn spam_training.txt spam.svm.model

[3.] Classifying Input Data:

    - svm_classify <DEV_FILE> <MODEL> <PREDICTIONS>

> eg: svm_classify spam_dev.txt spam.svm.model predictions.out

[4.] PostProcess Output:

    - python3 postprocesssvm.py <PREDICTIONS> <CLASS1_LABEL> <CLASS2_LABEL>

> eg: python3 postprocesssvm.py predictions.out HAM SPAM > spam.svm.out


**(2) MegaM:**

[1.] Formatting Training Data:

    - python3 formatmegaminput.py <DIR> <CLASS1> <OUT_TRAIN_FILE> <MODE>
    - mode can be training or development

> eg: python3 formatmegaminput.py ../../SPAM_training/ HAM spam_training.txt training

[2.] Training Data Model

    - megam -fvals binary <TRAINING_FILE> > <MODEL>

> eg: megam -fvals binary spam_training.txt > spam.megam.model

[3.] Classifying Input Data:

    - megam -fvals -predict <MODEL> binary <DEV_FILE> > <OUTPUT_FILE>

> eg: megam -fvals -predict spam.megam.model binary spam_dev.txt > predictions.out

[4.] PostProcess Output:

    - python3 postprocessmegam.py <PREDICTIONS> <CLASS1_LABEL> <CLASS2_LABEL> > <OUTPUT_FILE>

> eg: python3 postprocessmegam.py predictions.out HAM SPAM > spam.megam.out

## **Part III:**

### **(1) Precision, Recall and F-score for each label (Naive Bayes)**

#### **Spam Classification:**
  - HAM:  F-Score = 0.987963, Precision = 0.990945, Recall = 0.985000
  - SPAM: F-Score = 0.967213, Precision = 0.959349, Recall = 0.975206

#### **Sentiment Classification:**
  - POS:  F-Score = 0.916429, Precision = 0.946466, Recall = 0.888240
  - NEG:  F-Score = 0.921417, Precision = 0.894717, Recall = 0.949760

### **(2) Precision, Recall and F-score for each label (SVM)**

#### **Spam Classification:**
  - HAM:  F-Score = 0.914972, Precision = 0.850515, Recall = 0.990000
  - SPAM: F-Score = 0.672597, Precision = 0.949748, Recall = 0.520661

#### **Sentiment Classification:**
  - POS:  F-Score = 0.903174, Precision = 0.893903, Recall = 0.912640
  - NEG:  F-Score = 0.901123, Precision = 0.910769, Recall = 0.891680

### **(3) Precision, Recall and F-score for each label (MegaM)**

#### **Spam Classification**
  - HAM:  F-Score = 0.952058, Precision = 0.923004, Recall = 0.983000
  - SPAM: F-Score = 0.850226, Precision = 0.942953, Recall = 0.774104

#### **Sentiment Classification**
  - POS:  F-Score = 0.943689, Precision = 0.945546, Recall = 0.941840
  - NEG:  F-Score = 0.943909, Precision = 0.942067, Recall = 0.945760

### **(4) 10% Reduction of Training Data:**

What happens exactly to precision, recall and F-score in  (on the development data) when only 10% of the training data is used to train the classifiers ?

This causes a huge reduction in F-score for SVM. However the F-score for Naive Bayes and MegaM only has a minimal decrease.

#####**Naive Bayes:**
  - HAM  F-score: 0.979083, Precision: 0.975198, Recall: 0.98300
  - SPAM F-score: 0.941504, Precision: 0.952112, Recall: 0.93112

#####**SVM:**
  - HAM  F-score: 0.863459, Precision: 0.762050, Recall: 0.99600
  - SPAM F-score: 0.248210, Precision: 0.928571, Recall: 0.14325

#####**MegaM:**
  - HAM  F-score: 0.975413, Precision: 0.978851, Recall: 0.972000
  - SPAM F-score: 0.933151, Precision: 0.924324, Recall: 0.942148