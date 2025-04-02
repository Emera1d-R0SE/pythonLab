import pandas as pd
import numpy as np
# Create a DataFrame from a date_range()
dates = pd.date_range("20130101", periods=6)
df_2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(dates)
print(df_2)



#program2
import pandas as pd
import numpy as np
# Create a DataFrame from a dictionary
data = {
"Name": ["Ram", "Robert", "Rahim"],
"Age": [25, 30, 35],
"City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)
print(df)
print("--------")
# Access a column
print("Access a column\n",df["Name"],"\n")
# Accessing a row by label
print("Accessing a row by label\n", df.loc[0], "\n")
# Access a row by index
print("Access a row by index\n", df.iloc[1], "\n")
# Access a specific cell
print("# Access a specific cell\n",df.at[0, "Age"],"\n") # Corrected line
# Slicing
print("Slicing",df[1:3]) # Slicing rows


#program3
import pandas as pd
import numpy as np
population_dict = {
"California": 38332521,
"Texas": 26448193,
"Florida": 19552860,
"Illinois": 12882135,
}
population = pd.Series(population_dict)
print(population_dict, type(population_dict))
print(population, type(population))


#program4
import pandas as pd
import numpy as np
data = {"A": [1, 2, np.nan, 4], "B": [5, np.nan, 7, 8], "C": [9, 10, 11, np.
↪nan]}
df = pd.DataFrame(data)
print(df)
# Drop rows with missing values
df.dropna(inplace=True) # Modify df directly
print(df) # Print the modified DataFrame
