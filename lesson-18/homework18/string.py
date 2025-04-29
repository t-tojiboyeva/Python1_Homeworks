Find all questions that were created before 2014
Find all questions with a score more than 50
Find all questions with a score between 50 and 100
Find all questions answered by Scott Boston
Find all questions answered by the following 5 users
Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
Find all questions that are not answered by Scott Boston

import pandas as pd

df = pd.read_csv(r'D:\csv files\tackoverflow_qa.csv')
df.head()

# Make sure the 'creationdate' column is in datetime format
df['creationdate'] = pd.to_datetime(df['creationdate'])

# Filter rows where the creation date is before 2014
before_2014 = df[df['creationdate'] < '2014-01-01']

# Display the result
print(before_2014)

score1=df[df['score']>50]
print(score1)

between_score=df[(df['score']>50) & (df['score']<100)]
print(between_score)
#Find all questions answered by Scott Boston

answered_by=df[df['ans_name']=='Scott Boston']
print(answered_by)
#Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

df['creationdate']=pd.to_datetime(df['creationdate'])
changed=df[
    (df['creationdate'] >=pd.Timestamp('2014-03-01')) &
    (df['creationdate'] <=pd.Timestamp('2014-10-31')) &
    (df['ans_name'] =='unutbu') &
    (df['score']<5)
]
print(changed)
#Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

greater_view=df[
    ((df['score']>=5) & (df['score']<=10) ) |
    (df['viewcount']> 10000)
]
print(greater_view)
df
#Find all questions that are not answered by Scott Boston

#Find all questions answered by Scott Boston

answered_by=df[df['ans_name']!='Scott Boston']
print(answered_by)
Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
import pandas as pd

df = pd.read_csv(r'D:\csv files\titanic.csv')
df.head()

female_class1_20_30 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Age'].between(20, 30))]
print(female_class1_20_30)
fare_over_100 = df[df['Fare'] > 100]
fare_over_100
survived_alone = df[(df['Survived'] == 1) & (df['SibSp'] == 0) & (df['Parch'] == 0)]
survived_alone
embarked_c_fare_50 = df[(df['Embarked'] == 'C') & (df['Fare'] > 50)]
embarked_c_fare_50
df
selected_passengers = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]
 
selected_passengers
young_survivors=df[(df['Age']<=15)&(df['Survived']==0)]
young_survivors
high_fare_with_cabin=df[(df['Cabin'].notnull())&(df['Fare']>200)]
high_fare_with_cabin
odd_passenger_id=df[df['PassengerId']%2 !=0]
odd_passenger_id
unique_tickets=df[df['Ticket'].duplicated(keep=False)==False]
unique_tickets
miss_class1=df[df['Name'].str.contains('Miss')&(df['Pclass']==1)&(df['Sex']=='female')]
miss_class1
