import pandas as pd

col_names = ["Subject", "spam"]
df = pd.read_csv("emails.csv", skiprows = 1, names = col_names)

#No missing values 
#print(df.isnull().sum())

df.drop_duplicates(inplace = True)

#Standardizing text by converting to lower cases
df["Subject"] = df['Subject'].str.lower()


#Removing the "Subject: " prefix from the beginning of each email
df["Subject"] = df["Subject"].str.replace(r'^subject:\s*', '', regex=True)

#Removing any instances of "re:" or "fw: or 'fwd:" etc in each emails
df['Subject'] = df['Subject'].str.replace(
    r'(?i)^(?:\s*(?:re|fw|fwd)\s*:\s*)+',
    '',
    regex=True
)

df.to_csv('emails_w1998cleaned.csv', index=False)


df_2 = pd.read_csv("spam_ham_dataset.csv")
df_2 = df_2.drop(df_2.columns[[0,1]], axis =1)
df_2.columns = col_names



df_2["Subject"] = df_2['Subject'].str.lower()
df_2["Subject"] = df_2["Subject"].str.replace(r'^subject:\s*', '', regex=True)
df_2['Subject'] = df_2['Subject'].str.replace(r'(?i)^(?:\s*(?:re|fw|fwd)\s*:\s*)+','',
    regex=True
)

df_2.to_csv("venkateshcleaneddataset.csv")

#Concatenating the datasets on top of each other 

combined_df = pd.concat([df,df_2], ignore_index=True)

combined_df.to_csv("combined_cleaned_dataset.csv", index = False)

#considerations: some emails were forwarded and contains the content from the previous messages, not sure if we should keep it else i can find a way to clean it 