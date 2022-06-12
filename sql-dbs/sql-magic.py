#Jupyter notebooks allow to use magic commands.

#Cell magics - start with %% and apply to the entire cell.
#Line magics - start with % and apply to a particular line in a cell.

#Automatically queries and fetches results:
%sql SELECT * FROM tablename

#Using Python variables
country = 'Canada'
%sql SELECT * FROM tablename WHERE country = :country
