
# 🐼 Pandas Day 2 — Data Selection Practice
import pandas as pd

data = {
    "Name": ["Adil", "Rahul", "Aman", "Sneha", "Priya"],
    "Age": [19, 20, 21, 22, 20],
    "City": ["Latur", "Pune", "Mumbai", "Pune", "Latur"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)
print(df)


# Questions
'''
#Q1. Sirf `Name` column print karo.
print(df['Name'])

#Q2. Sirf `Marks` column print karo.
print(df['Marks'])

#Q3. `Name` aur `City` columns print karo.
print(df[['Name','City']])

#Q4.** `Name`, `Age` aur `Marks` columns print karo.
print(df[['Name','Age','Marks']])

#Q5.** DataFrame ki first row select karo.
print(df.iloc[0])

#Q6.** DataFrame ki third row select karo using `iloc`.
print(df.iloc[2])

#Q7.** First 3 rows select karo using `iloc`.
print(df.iloc[0:3])

#Q8.** `Age` 20 se greater students ko filter karo.
print(df[df['Age'] > 20])

#Q9.** `Marks` 80 se greater students ko filter karo.
print(df[df['Marks'] > 80])

#Q10.** Sirf **Pune** city ke students ko filter karo.
print(df[df['City'] == 'Pune'])

#Q11.** `Marks >= 75` wale students ko select karo.
print(df[df['Marks'] >= 75])

#Q12.** `Age == 20` wale students ko select karo.
print(df[df['Age']==20])

#Q13.** `City == "Latur"` **AND** `Marks > 75` wale students select karo.
print(df[(df['City']=='Latur') & (df['Marks']>75)])
'''
#Q14.** `City == "Pune"` **OR** `City == "Latur"` wale students select karo.
print(df[(df['City']=='Pune') | (df['City']=='Latur')])

#Q15.** `loc` ka use karke `Name` aur `Marks` columns select karo.
print(df.loc[:,['Name','Marks']])

#Q16.** `iloc` ka use karke first 2 rows aur first 2 columns select karo.
print(df.iloc[0:2,0:2])
#Q17.** Jis student ke marks **highest** hain uska data find karo.
print(df.loc[df['Marks'].idxmax()])
#Q18.** `Marks` ko descending order mein sort karo.
print(df['Marks'].sort_values(ascending=False))

#Q19.** Sirf `Name` aur `Marks` columns ko `Marks` ke basis par descending order mein sort karo.
print(df[['Name', 'Marks']].sort_values(by='Marks', ascending=False))

#Q20.** `Age` 20 se greater **AND** `Marks` 75 se greater students find karo.
print(df[(df['Age'] > 20) & (df['Marks'] > 75)])
