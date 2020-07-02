#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

from sklearn import tree
from sklearn import cross_validation

train_features, test_features, train_labels, test_labels = cross_validation.train_test_split(features, labels, test_size=0.30, random_state=42)

clf = tree.DecisionTreeClassifier()

# clf.fit(features, labels)
# print clf.score(features, labels)

clf.fit(train_features, train_labels)
pred = clf.predict(test_features)
print pred
print test_labels
print clf.score(test_features, test_labels)

from sklearn.metrics import precision_score, recall_score

print "Precision:", precision_score(test_labels, pred)
print "Recall:", recall_score(test_labels, pred)