import os

import pandas as pd

from Utils.Get import get_data, get_nan, get_duplicate
from Utils.Graphics import plot_month

if __name__ == '__main__':
	file_path_Train = "Files/DailyDelhiClimateTrain.csv"
	file_path_Test = "Files/DailyDelhiClimateTest.csv"
	if not (os.path.isfile(file_path_Train) and os.path.isfile(file_path_Test)):
		print("fichiers manquants")
		exit()
	
	# Creation and cleaning of variables
	dataFrame_Train = get_data(file_path_Train, sep=',', txt=True)
	dataFrame_Test = get_data(file_path_Test, sep=',', txt=True)
	
	# We concat all the data to have only one dataframe to use
	dataFrame = pd.concat([dataFrame_Train, dataFrame_Test], axis=0).reset_index(drop=True)
	del (dataFrame_Test, dataFrame_Train)
	
	print("Get information about duplicates and nan in the dataFrame")
	print("Nan: ")
	print(get_nan(dataFrame))
	print("Duplicates: ")
	print(get_duplicate(dataFrame, 'date'))
	
	# There is one duplicate row :
	# this is the last row of Train dataset and the first of Test dataset.
	# We keep the row from Test dataset
	dataFrame.drop_duplicates(subset=['date'], keep='last', inplace=True)
	dataFrame = dataFrame.reset_index(drop=True)
	
	# change dtype of date from 'object' to 'datetime' and change the index
	dataFrame['date'] = pd.to_datetime(dataFrame['date'])
	dataFrame.set_index("date", inplace=True)
	
	plot_month(dataFrame, 'meantemp', 2013, 1, '%d', ["Days", "Mean Temperatures", "Mean temperatures per day"])
