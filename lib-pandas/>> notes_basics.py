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
# data 4 = pandas.read_sql_query(QUERY, conn)	assuming the have a connection established with
#						sqlite3					

# data.to_csv('data.csv')			keyword parameter index is True by default,
# data.to_json('data.json')			can be changed to False which will cause index
# data.to_pickle('data.bin')			index column not to be saved

____________________________________________________________________________________________________
CREATING SERIES & DATAFRAMES
ser_2 = pandas.Series([2,8,3,250,10,25,16,1,-8])

simple_df = pandas.DataFrame([1,2,3,4])

dictionary = {'Name': ['Ala', 'Mala', 'Koczisa', 'Oraza', 'Piesa'], \
              'ID': ['1234', '22892', '33456', '78223', '48244'], \
                  'Money': [2500, 3400, 1000, 6700, 4330]}

my_df = pandas.DataFrame(dictionary)

series.to_frame()  #converts Series to DataFrame

#Easy way to create a df:

my_df_2 = pandas.DataFrame()		#empty df
my_df_2['Column_1'] = my_list
and so on...

____________________________________________________________________________________________________
DATATYPES

data['col1'] = data['col1'].astype(float)	
data['col1'] = data['col1'].astype('int64')	

____________________________________________________________________________________________________
CLEANING
sorted_order = ser_2.argsort()  	#returns sorted order of indices
ser_2[sorted_order] 			#col_2 in sorted order
ser_2[ser_2.argsort()]  		#one line

data = data.replace('?', np.NaN)	#useful because dropna() can remove only NaNs

data.dropna()
data.dropna(subset=["ser_2"], axis=0, inplace=True)  #axis=0 drops rows, axis=1 drops cols

data.reset_index(drop=True, inplace=True)  #indices should be resetted after dropping any rows

ser_1.hasnans  				#checks if there are any NaN values
ser_2.all()  				#checks if all objects have a value assigned
ser_2.isnull()  			#check nulls

ser_2.interpolate()  			#fills NaNs with averages
ser_2.fillna()  			#fills with 0s

#Complex missing values check - example 1
missing_data = df.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 

#Complex missing values check - example 2
for col in missing_data.columns:
	
    sum_missings = df[col].isna().sum()
    
	if  sum_missings > 0:
        print(sum_missings, '\t', str(col))

____________________________________________________________________________________________________
TRANSFORMING
ser_2.abs()  				#absolute values
ser_1.append(ser_2)  			#appends col_1 to the end of col_2
ser_4 = ser_1.add(ser_2)  		#adds series .add(seriesX, fill_value=N)
ser_4 = ser_1.sub(ser_2)  		#subtracts series

#other operations: .mul, .div, .mod, .pow
#we can add, sub etc. series to itself

#simple operations (that apply to each row in a series/col) can be done like this:
ser_2 = ser_2 + 1

list_1_to_list = list_1.tolist()  			#converts to list
list_1_to_array = list_1.array  			#converts to numpy's array
my_df.columns = ['Col1', 'Col2', 'Col3']  		#sets column headers
my_df.rename(columns={"old": "new"}, inplace=True)
my_df.T  						#transpose (switch rows and cols)
my_df.apply(add,axis=1)  				#apply function to each row

#apply function to each row using lambda
my_df['new_col'] = df.apply(lambda row : row[0]+row[1]+row[2], axis=1)

#discretization
my_df['Column'] = pd.cut(my_df['Column'], 2, labels = ['Yes', 'No'])  #or qcut

#discretization with pandas and numpy
bins = numpy.linspace(min(df['price']), max(df['price']), 4)  #array that contains 4 equally spaced
							      #numbers over the specified interval
							      #of price
group_names = ['Low', 'Mid', 'High']
df['price-binned'] = pandas.cut(df['price'], bins, labels = group_names, include_lowest = True)

#turning categorical variables into quantitative variables

pd.get_dummies(df['fuel'])

#  Car	|  Fuel  | gas | diesel |
# ------------------------------
#   A   |  gas   |  1  |   0    |
#   B   | diesel |  0  |   1    |
#   C   |  gas   |  1  |   0    |
#   D   |  gas   |  1  |   0    |

____________________________________________________________________________________________________
BASIC EXPLORING

my_df.info()  #summary of a DataFrame
my_df.describe()  #ignores NaNs
my_df.describe(inlcude='all')  #includes non-numeric
my_df.columns  #headers

my_df.value_counts()  #summarizes categorical data
my_df.value_counts()['Specific value']
my_df['Series'].value_counts().to_frame()  #summarizes categorical data and converts to DataFrame

my_df.at[0, 'Money']  			#retrieve a value
my_df.loc[0, 'Money']  			#like above ('0' is actually a row's title, not index)
my_df.iloc[0,2]  			#like above but by indices
my_df.shape  				#tuple of ints indicating the size of df
my_df.ndim  				#number of dimensions
my_df.size 				#number of attributes*elements (cols*rows)
my_df.head(2)  				#first 2 (default = 5)
my_df.tail(2)  				#last 2 (defaul = 5)
my_df.dtypes  				#checks types of all columns
my_df.column.dtype			#checks the type of a single column
ser_1.index  				#range of values
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

#Setting quartiles
Q1 = df['Series'].quantile(0.25)
Q3 = df['Series'].quantile(0.75)
IQR = Q3 - Q1

#Finding outliers
df['Series'] < (Q1 - 1.5*IQR)	#it is assumed that low extreme is 1.5 times lower than 1Q
df['Series'] > (Q3 + 1.5*IQR)	#similarily, upper extreme is 1.5 times higher than 3Q
				#outliers are even lower/higher than extremes

____________________________________________________________________________________________________
MINING

#Note: corr in pandas is Pearson correlation method by default.

data.corr()					#correlation between all relevant variables (table form)
data.corr[['ser_1', 'ser_2', 'ser_N']].corr()	#correlation between choosen variables (table form) 		
ser_1.corr('ser_2')  				#correlation between ser_1 and ser_2
ser_1.corr('ser_1')  				#autocorrelation
ser_1.autocorr(lag = 5)  			#autocorrelation with shifted self
ser_1.sum()
ser_1.mean()
ser_1.median()
ser_1.std()  				#denominator N-1 by default
ser_1.std(ddof = 2)

#Groupby
data.groupby()  #group variables by categorical variables

df_test = df[['drive-wheels', 'body-style', 'price']]
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
	      

#  	|  drive-wheels  | body-style    | avg price |
# ----------------------------------------------------
#   0   |  4wd   	 |  convertible  |   x       |
#   1   |  4wd   	 |  sedan  	 |   x       |
#   2   |  fwd   	 |  convertible  |   x       |
#   3   |  rwd   	 |  convertible  |   x	     |	      

#To obtain the values of the particular group from the above:
group_4wd.get_group('4wd')['price']

#Pivot
df_pivot = df.grp.pivot(index = 'drive-wheels', columns = 'body-style')

#Filtering

#Example 1
df[df['Gender'] == 'Woman'].ConvertedComp.median()

#Example 2
mean_I_coll_1 = round(df[df['Group'] == 'I']['Colloquium_1'].mean(),2)
