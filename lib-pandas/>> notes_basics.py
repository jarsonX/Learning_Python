# PANDAS
# Useful functions for basic operations and pre-processing

#By default, pandas won't print the entire DF to console. This can be changed.
#Just keep in mind this is not always a good idea.
pandas.set_option("display.max_rows", None, "display.max_columns", None) 

import pandas
____________________________________________________________________________________________________
LOADING AND SAVING DATA
# data_1 = pandas.read_csv('data.csv')		keyword parameter header is True by default,
# data_2 = pandas.read_json('data.json')	can be changed to 'None' which will cause
# data_3 = pandas.read_pickle('data.bin')	headers to be displayed as integers (col nums)

# data.to_csv('data.csv')
# data.to_json('data.json')
# data.to_pickle('data.bin')

____________________________________________________________________________________________________
CREATING SERIES & DATAFRAMES
ser_2 = pandas.Series([2,8,3,250,10,25,16,1,-8])

simple_df = pandas.DataFrame([1,2,3,4])

dictionary = {'Name': ['Ala', 'Mala', 'Koczisa', 'Oraza', 'Piesa'], \
              'ID': ['1234', '22892', '33456', '78223', '48244'], \
                  'Money': [2500, 3400, 1000, 6700, 4330]}

my_df = pandas.DataFrame(dictionary)


Easy way to create a df:

my_df_2 = pandas.DataFrame()		#empty df
my_df_2['Column_1'] = my_list
and so on...

____________________________________________________________________________________________________
DATATYPES

data['col1'] = data['col1'].astype(float)

____________________________________________________________________________________________________
CLEANING
sorted_order = ser_2.argsort()  	#returns sorted order of indices
ser_2[sorted_order] 			#col_2 in sorted order
ser_2[ser_2.argsort()]  		#one line

ser_1.hasnans  				#checks if there are any NaN values
ser_2.all()  				#checks if all objects have a value assigned
ser_2.isnull()  			#check nulls

ser_2.interpolate()  			#fills NaNs with averages
ser_2.fillna()  			#fills with 0s

____________________________________________________________________________________________________
TRANSFORMING
ser_2.abs()  				#absolute values
ser_1.append(ser_2)  			#appends col_1 to the end of col_2
ser_4 = ser_1.add(ser_2)  		#adds series .add(seriesX, fill_value=N)
ser_4 = ser_1.sub(ser_2)  		#subtracts series

#other operations: .mul, .div, .mod, .pow
#we can add, sub etc. series to itself

list_1_to_list = list_1.tolist()  		#converts to list
list_1_to_array = list_1.array  		#converts to numpy's array
my_df.columns = ['Col1', 'Col2', 'Col3']  	#sets column headers
my_df.T  					#transpose (switch rows and cols)
my_df.apply(add,axis=1)  			#apply function to each row

#apply function to each row using lambda
my_df['new_col'] = df.apply(lambda row : row[0]+row[1]+row[2], axis=1)

#discretization
my_df['Column'] = pd.cut(my_df['Column'], 2, labels = ['Yes', 'No'])

or qcut

____________________________________________________________________________________________________
BASIC EXPLORING

my_df.info()  #top and last 30 rows 
my_df.describe()
my_df.describe(inlcude='all')  #includes non-numeric

my_df.at[0, 'Money']  			#retrieve a value
my_df.loc[0, 'Money']  			#like above ('0' is actually a row's title, not index)
my_df.iloc[0,2]  			#like above but by indices
my_df.shape  				#tuple of ints indicating the size of df
my_df.ndim  				#number of dimensions
my_df.size 				#number of attributes*elements (cols*rows)
my_df.head(2)  				#first 2 (default = 5)
my_df.tail(2)  				#last 2 (defaul = 5)
ser_1.index  				#range of values
ser_1.dtypes  				#checks type
ser_1.size  				#counts objects
ser_1.count()  				#counts objects, ignoring missing values
ser_1.name  				#column name
ser_1.unique()  			#only unique values
ser_2.get(5)  				#returns value of given index
ser_2.argmax()  			#returns index with max value
ser_2.argmin()  			#returns index with min value
ser_2.max()  				#returns max value
ser_2.min()  				#returns min value
ser_2.lt(5)  				#checks if all values are less than 5
					#gt = greater than, le = less or equal, ge = greater or equal
ser_5 = my_df['Name']  			#retrieve column as a Series

____________________________________________________________________________________________________
MINING

ser_1.corr(ser_2)  			#correlation between ser_1 and ser_2
ser_1.corr(ser_1)  			#autocorrelation
ser_1.autocorr(lag = 5)  		#autocorrelation with shifted self
ser_1.sum()
ser_1.mean()
ser_1.median()
ser_1.std()  				#denominator N-1 by default
ser_1.std(ddof = 2)
