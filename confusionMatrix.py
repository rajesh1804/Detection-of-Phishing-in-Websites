#rajesh m
import ast

with open('phishing5.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())
#print (mylist)

# Python script for confusion matrix creation. 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
with open('phishing5.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())
actual = [-1,0,-1,-1,1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1] 

predicted = mylist
results = confusion_matrix(actual, predicted) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :',accuracy_score(actual, predicted)) 
print ('Report : ')
print (classification_report(actual, predicted))
