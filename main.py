'''It is decision of "Titanik" from Kaggle: "https://www.kaggle.com/competitions/titanic".'''

import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns


#Path to data
PATH_TO_TRAIN = "data/train.csv"
PATH_TO_TEST = "data/test.csv"


#Loading data
train_data = pd.read_csv(PATH_TO_TRAIN, index_col="PassengerId") # Training sample
test_data = pd.read_csv(PATH_TO_TEST, index_col="PassengerId")   # Test sample


#Drop useless columns
useless_columns = ["Name", "Ticket", "Cabin"] #There is very little data in the "Cabin"

train_data_clean = train_data.drop(columns=useless_columns)
test_data_clean = test_data.drop(columns=useless_columns)


#Inputing NaN data
train_data_full = inpute_data(train_data_clean)
test_data_full = inpute_data(test_data_clean)
