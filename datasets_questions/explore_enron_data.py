#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print len(enron_data)

# count = 0
# for person in enron_data:
#   feature = enron_data[person]
#   if feature["poi"] == 1:
#     count += 1
# print "Count: ", count

# with open("../final_project/poi_names.txt") as fp:
#   data = fp.read().strip().splitlines()
#   data = data[2:]

#   print "Count: ", len(data)

# print enron_data["PRENTICE JAMES"]["total_stock_value"]

sorted_keys = sorted(enron_data.keys())

# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# print sorted_keys

# print enron_data["SKILLING JEFFREY K"]["total_payments"]
# print enron_data["LAY KENNETH L"]["total_payments"]
# print enron_data["FASTOW ANDREW S"]["total_payments"]


# q_salary = 0
# for person in enron_data:
#   if enron_data[person]["salary"] != "NaN":
#     q_salary += 1
# print q_salary

# count = 0
# for person in enron_data:
#   feature = enron_data[person]
#   if feature["email_address"] != "NaN": 
#     count += 1
# print count

# count = 0
# for person in enron_data:
#   feature = enron_data[person]

#   if feature["total_payments"] == "NaN":
#     count += 1
# print (100.0 * count) / len(enron_data)

# count = 0
# for person in enron_data:
#   feature = enron_data[person]
#   if feature["poi"] == True:
#     if feature["total_payments"] == "NaN":
#       count += 1
# print (100.0 * count) / len(enron_data)

# count = 0
# for person in enron_data:
#   feature = enron_data[person]
#   if feature["total_payments"] == "NaN":
#     count += 1
# print count

poi_count = 0
count = 0
for person in enron_data:
  feature = enron_data[person]
  if feature["poi"] == True:
    poi_count += 1
    if feature["total_payments"] == "NaN":
      count += 1
print poi_count, count