import pandas as pd

data = {
    "Name": ["Adil", "Rahul", "Aman", "Sneha", "Priya"],
    "Age": [19, 20, 21, 22, 20],
    "City": ["Latur", "Pune", "Mumbai", "Pune", "Latur"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)

print(df)

#                                              🐼 Day 3 — 20 Practice Questions

#Q1. DataFrame mein Gender naam ka new column add karo:
#["Male", "Male", "Male", "Female", "Female"]
df['Gender']=["Male", "Male", "Male", "Female", "Female"]
print(df)

#Q2. Country naam ka new column add karo aur sabhi students ke liye "India" set karo.
df['Country']=["India","India","India","India","India"]
print(df)

#Q3. Age se NextAge naam ka new column banao jo Age + 1 ho.
df['NextAge']=df['Age']+1
print(df)

#Q4. Marks se Percentage naam ka column banao. Marks 100 mein se hain, isliye percentage same marks ke equal hoga.
df[' Percentage']=df['Marks']/100*100
print(df)

#Q5. Marks mein sabhi students ke marks 5 increase karo.
df['Marks']=df['Marks']+5
print(df)

#Q6. Sirf "Adil" ke marks ko 95 karo.
#df.loc[df['Name']=='Adil','Marks']=95
#print(df)

#Q7. "Rahul" ki city "Pune" se "Mumbai" karo.
df.loc[df['Name']=='Rahul','City']='Mumbai'
print(df)

#Q8. Age column ko update karke sabhi students ki age mein 1 add karo.
df['Age']=df['Age']+1
print(df)

#Q9. Gender column delete karo.
df.drop('Gender',axis=1,inplace=True)
print(df)

#Q10. Country column delete karo.
df.drop('Country',axis=1,inplace=True)
print(df)

#Q11. City aur Age dono columns delete karo.
df.drop(['City','Age'],axis=1,inplace=True)
print(df)

#Q12. Marks column ko rename karke Score karo.
df=df.rename(columns={'Marks':'Score'})
print(df)

#Q13. Name ko StudentName aur NextAge ko StudentAge rename karo.
df=df.rename(columns={"Name":"StudentName","NextAge":" StudentAge"})
print(df)

#Q14. City column ko rename karke Location karo.
df.rename(columns={'City':'Location'})
print(df)

#Q15. Grade column banao:
#Marks >= 80 → "A"
#Marks >= 70 → "B"
#Marks < 70  → "C"
import numpy as np
df['Grade']=np.select(
   [
        df['Score'] >= 80,
        df['Score']>=70,
        df['Score']<70
   ],
   [
    'A',
    'B',
    'C'
   ]
)
print(df)

#Q16. Passed naam ka column banao:
#Marks >= 40 → "Yes"
#Marks < 40  → "No"
import numpy as np
df['Result']=np.select(
    [
        df['Score'] >= 40,
        df['Score'] < 40
    ],
    [
        'Yes',
        'No'
    ]
)
print(df)

#Q17. AgeGroup naam ka column banao:
#Age >= 21 → "Adult"
#Age < 21  → "Young"
df['AgeGroup'] = np.where(
    df['Age'] >= 21,
    'Adult',
    'Young'
)

print(df)
#Q18. Country column ko second position par "India" value ke saath insert karo.
df.insert(1, 'Country', 'India')
print(df)
#Q19. DataFrame ka column order ye karo:
#Name, City, Age, Marks
df = df[['Name', 'City', 'Age', 'Marks']]
print(df)


#Q20. 🔥 Challenge: Ek Result column banao:
#Marks >= 75 → "Excellent"
#Marks >= 50 → "Good"
#Marks < 50  → "Fail"
df['Result'] = np.select(
    [
        df['Marks'] >= 75,
        df['Marks'] >= 50
    ],
    [
        'Excellent',
        'Good'
    ],
    default='Fail'
)

print(df)

