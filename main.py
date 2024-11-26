import pandas as pd

df = pd.read_csv(r'C:\Users\rishi\OneDrive\Desktop\Python Files\sqlbi\Air_Quality.csv')

def safe_convert_to_datetime(date_value):
    try:
        # Try to convert the date to datetime, if it fails it will return NaT
        return pd.to_datetime(date_value, errors='coerce', dayfirst=False)
    except Exception as e:
        # If conversion fails, return the original value
        return date_value
df['Date'] = df['Start_Date'].apply(safe_convert_to_datetime)
df.to_csv('cleaned_air_quality2.csv', index=False)
# checked for any null values
#print(df.isnull().sum())
# removed any unnecessary columns
df.drop('Geo Join ID', axis = 1, inplace = True)
df.drop(["Measure", "Message"], axis = 1, inplace = True)

df_cleaned = df.dropna()
df = df_cleaned
#print(df_cleaned.isnull().sum())

df['Geo Type Name'] = df['Geo Type Name'].astype('category')
df['Measure Info'] = df['Measure Info'].astype('category')
df.to_csv('clean_air_quality2.csv', index=False)
print(df.columns)