#FIRST PROJECT
# Project Name ....Basic Customer Data Analysis 

# step 1..... Import libraries
import pandas as pd
import matplotlib.pyplot as plt


# step 2..... Data create
data={"Customer Id": [1,2,3,4,5],
      "Name":["A","B","C","D","E"],
      "Age":[22,23,24,27,29],
      "Gender":["Female","Male","Female","Male","Female"],
      "Purchase Amount":[250,300,430,150,350]
      }
# step 3..... Converd to Datafarme      
df=pd.DataFrame(data)

# step 4 .... Data explore
print("Customer Data:")
print(df)

# step 4.... Calculate the Averge purchase Amount 
average_purchase=df["Purchase Amount"].mean()
print(f"\nAverage Purchase Amount : {average_purchase}")

# step 5.... Calculate the sum Genderwise purchase amount 
gender_purchase=df.groupby("Gender")["Purchase Amount"].sum()
print("\nTotal Purchase by Gender:")
print(gender_purchase)

# step 6....visulaization
# age vs purchase
plt.figure(figsize=(5,8))  #(width,hight)
plt.bar(df['Age'],df["Purchase Amount"],color="r")
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()
