#                                 🐼 Pandas — Day 1 Practice

#Q1. Pandas import karke pd naam ka alias banao.
import pandas as pd

#Q2. Ye list Pandas Series mein convert karo:
list=[10, 20, 30, 40, 50]
print(pd.Series(list))

#Q3. Ye dictionary se DataFrame banao:
data = {
    "Name": ["Adil", "Rahul", "Aman"],
    "Age": [19, 20, 21],
    "City": ["Latur", "Pune", "Mumbai"]
}

#Q4. DataFrame ko print karo.
df=pd.DataFrame(data)
print(df)

#Q5. DataFrame ki first 2 rows head() se print karo.
print(df.head(2))

#Q6. Last 2 rows tail() se print karo.
print(df.tail(2))

#Q7. DataFrame ka shape print karo.
print(df.shape)

#Q8. DataFrame ke columns ke names print karo.
print(df.columns)

#Q9. DataFrame ke data types (dtypes) print karo.
print(df.dtypes)

#Q10. DataFrame ki basic statistical information describe() se print karo.
print(df.describe())