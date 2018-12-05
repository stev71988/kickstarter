import pandas as pd
import csv

csvfile ="/Users/stephensim/Documents/Kickstarter/kickstarter-projects/ks-projects-201801.csv"

# Upload Dataset
print("Loading data...")
df = pd.read_csv(csvfile)
print("Loading data complete!")
print("Dataset has %d rows." % ( df["ID"].size)) #%d acts as a placeholder#

def addData(dataset):
	df['Dates'] = pd.to_datetime(df['launched']).dt.date
	df['Time'] = pd.to_datetime(df['launched']).dt.time
	df['Year'] = pd.to_datetime(df['launched']).dt.year
	df['Month'] = pd.to_datetime(df['launched']).dt.month
	df['Hour'] = pd.to_datetime(df['launched']).dt.hour
	df['Weekday'] = pd.to_datetime(df['launched']).dt.weekday
	dataset = dataset[dataset['Year'] > 2009]
	dataset = dataset[dataset['Year'] < 2018]

	return dataset

new_df = addData(df)

new_df['Weekday'] = new_df['Weekday'].astype(str)
new_df['Weekday'] = new_df['Weekday'].replace('0','Monday')
new_df['Weekday'] = new_df['Weekday'].replace('1','Tuesday')
new_df['Weekday'] = new_df['Weekday'].replace('2','Wednesday')
new_df['Weekday'] = new_df['Weekday'].replace('3','Thursday')
new_df['Weekday'] = new_df['Weekday'].replace('4','Friday')
new_df['Weekday'] = new_df['Weekday'].replace('5','Saturday')
new_df['Weekday'] = new_df['Weekday'].replace('6','Sunday')


Category = new_df.groupby(['category'], as_index=False)[['ID']].count()
Category = Category.sort_values(by='ID', ascending=0)

# Entire dataset with no groupings
new_df.to_csv('allData.csv', encoding='utf-8')
