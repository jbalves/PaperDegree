from pyroc import *
random_sample  = random_mixture_Model()  # Generate a custom set randomly
print random_sample

#Example instance labels (first index) with the decision function , score (second index)
#-- positive class should be +1 and negative 0.

roc = ROCData(random_sample)  #Create the ROC Object
roc.auc() #get the area under the curve
roc.plot(title='ROC Curve') #Create a plot of the ROC curve