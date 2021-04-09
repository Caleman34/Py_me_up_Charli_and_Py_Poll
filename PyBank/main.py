
#import pandas for data frames
import pandas as pd

# Save path to data set in variable
PyBank_Data = "Resources/PyBank_Data.csv"

# Use Pandas to read data file and show first 5 rows of data
PyBank_Data_df = pd.read_csv(PyBank_Data)
PyBank_Data_df.head()




