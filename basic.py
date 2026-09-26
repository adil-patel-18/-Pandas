#                                                                🐼 Pandas Day 1 — Basics

#1. Pandas import karke `pd` alias banao.
import pandas as pd

#2. `[10, 20, 30, 40, 50]` ko Pandas Series mein convert karo.
list=[10,20,30,40,50]
df=pd.Series(list)

#3. Series ko print karo.
print(df)

#4. Dictionary se DataFrame banao:
data = {
       "Name": ["Adil", "Rahul", "Aman"],
       "Age": [19, 20, 21],
       "City": ["Latur", "Pune", "Mumbai"]
   }
df=pd.DataFrame(data)

#5. DataFrame print karo.
print(df)

#6. First 2 rows `head()` se print karo.
print(df.head(2))

#7. Last 2 rows `tail()` se print karo.
print(df.tail(2))

#8. DataFrame ka `shape` print karo.
print(df.shape)

#9. Column names print karo.
print(df.columns)

#10. Data types `dtypes` se print karo.
print(df.dtypes)

#11. DataFrame ki basic information `info()` se print karo.
print(df.info())

#12. Statistical information `describe()` se print karo.
print(df.describe())

#13. DataFrame ka index print karo.
print(df.index)

#14. `Age` column ka data type find karo.
print(df['Age'].dtypes)

#15. DataFrame mein kitni rows aur columns hain, find karo.
print(df.shape)

#                                           🐼 Pandas Day 2 — Data Selection & Filtering

data = {
    "Name": ["Adil", "Rahul", "Aman", "Sneha", "Priya"],
    "Age": [19, 20, 21, 22, 20],
    "City": ["Latur", "Pune", "Mumbai", "Pune", "Latur"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)

# Q16–Q20 — Column Selection
#16. Sirf `Name` column select karo.
print(df['Name'])

#17. Sirf `Marks` column select karo.
print(df['Marks'])

#18. `Name` aur `City` columns select karo.
print(df[['Name','City']])

#19. `Name`, `Age` aur `Marks` columns select karo.
print(df[['Name','Age','Marks']])

#20. `City` aur `Marks` columns select karo.
print(df[['City','Marks']])

# Q21–Q25 — Row Selection

#21. First row `iloc` se select karo.
print(df.iloc(0))

#22. Third row `iloc` se select karo.
print(df.iloc(2))

#23. First 3 rows `iloc` se select karo.
print(df.iloc[0:3])

#24. Last 2 rows `iloc` se select karo.
print(df.iloc[-2:])

#25. First 2 rows aur first 2 columns `iloc` se select karo.
print(df.iloc[0:2,0:2])

# Q26–Q30 — Filtering

#26. `Age > 20` wale students select karo.
print(df['Age'] > 20)

#27. `Marks > 80` wale students select karo.
print(df['Marks'] > 80)

#28. `Marks >= 75` wale students select karo.
print(df['Marks'] >= 75)

#29. `Age == 20` wale students select karo.
print(df['Age'] == 20)

#30. Sirf `Pune` city ke students select karo.
print(df['City']=='Pune')

# Q31–Q35 — `&` and `|`

#31. `City == "Latur"` **AND** `Marks > 75`.
print(df[(df['City']=='Latur') & (df['Marks'] > 75)])

#32. `Age > 19` **AND** `Marks >= 75`.
print(df[(df['Age'] > 19) & (df['marks']>=75)])

#33. `City == "Pune"` **OR** `City == "Latur"`.
print(df[(df['City']=='Pune') | (df['City']=='Latur')])

#34. `Age == 20` **OR** `Marks > 85`.
print(df[(df['Age'] > 20) & (df['marks']>=85)])

#35. `Age > 20` **AND** `City == "Pune"`.
print(df[(df['Age'] > 20) & (df['City']=='Pune')])

# Q36–Q40 — `loc`, sorting & analysis
#36. `loc` se `Name` aur `Marks` columns select karo.
print(df.loc[:,['Name','Marks']])

#37. `loc` se first 3 rows select karo.
print(df.loc[0:2])

#38. `Marks` ko ascending order mein sort karo.
print(df['marks'].sort_values(ascending=True))

#39. `Marks` ko descending order mein sort karo.
print(df['marks'].sort_values(ascending=False))

#40. Sabse highest marks wale student ki **complete row** find karo.
print(df.loc[df['Marks'].idxmax()])

# 🔥 Challenge Questions

#41. `Name` aur `Marks` ko marks ke descending order mein display karo.
print(df[['Name','Marks']].sort_values(ascending=False))

#42. `Age > 20` wale students ke sirf `Name` aur `City` display karo.
print(df['Age'] > 20 [['Name','City']])

#43. `Pune` ke students mein highest marks kis ke hain, find karo.
print(df.loc[df[df['City'] == 'Pune']['Marks'].idxmax()])

#44. `Marks >= 75` wale students ko marks descending order mein display karo.
print(df[df['Marks'] >= 75].sort_values('Marks', ascending=False))

#45. `Age > 19` **AND** `Marks > 70` wale students ke `Name`, `City`, `Marks` display karo.
print(df.loc[
    (df['Age'] > 19) & (df['Marks'] > 70),
    ['Name', 'City', 'Marks']
])
