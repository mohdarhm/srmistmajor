import numpy as np 
import pandas as pd
from sqlalchemy import create_engine
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler

# Define your MySQL database connection details
connection_string = 'mysql+pymysql://root:arhum123@localhost/mp_django'

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Define your SQL query
sql_query = "SELECT * FROM mainapp_surveyresponse"

# Read data from the database into a DataFrame
df = pd.read_sql(sql_query, engine)

# print(df.describe())
# print(df.shape)
# print(df.info())

def display_missing_data(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    print(missing_data.head(20))
    



def preprocess_dataframe(df):
    # Define feature columns to keep
    feature_cols = ['age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere']
    
    # Drop columns not in feature_cols
    cols_to_drop = [col for col in df.columns if col not in feature_cols]
    df = df.drop(cols_to_drop, axis=1)
    
    # Define default values for missing data
    defaultInt = 0
    defaultString = 'NaN'
    defaultFloat = 0.0

    # Create lists by data type
    intFeatures = ['age']
    stringFeatures = ['gender', 'family_history', 'work_interfere', 'benefits', 'care_options', 'anonymity', 'leave']
    floatFeatures = []

    # Clean the NaN's
    for feature in df:
        if feature in intFeatures:
            df[feature] = df[feature].fillna(defaultInt)
        elif feature in stringFeatures:
            df[feature] = df[feature].fillna(defaultString)
        elif feature in floatFeatures:
            df[feature] = df[feature].fillna(defaultFloat)
        else:
            pass
        
    # Standardize gender values
    male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "Cis Male", "cis male"]
    trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]           
    female_str = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]

    for (row, col) in df.iterrows():
        if str.lower(col.gender) in male_str:
            df['gender'].replace(to_replace=col.gender, value='male', inplace=True)
        elif str.lower(col.gender) in female_str:
            df['gender'].replace(to_replace=col.gender, value='female', inplace=True)
        elif str.lower(col.gender) in trans_str:
            df['gender'].replace(to_replace=col.gender, value='trans', inplace=True)

    # Remove unwanted values
    stk_list = ['A little about you', 'p']
    df = df[~df['gender'].isin(stk_list)]

    # Complete missing age with median and adjust out-of-range values
    df['age'].fillna(df['age'].median(), inplace=True)
    df.loc[df['age'] < 18, 'age'] = df['age'].median()
    df.loc[df['age'] > 120, 'age'] = df['age'].median()
    
    # Encode categorical variables
    labelDict = {}
    for feature in stringFeatures:
        le = LabelEncoder()
        df[feature] = le.fit_transform(df[feature])
        labelDict['label_' + feature] = dict(zip(le.classes_, le.transform(le.classes_)))
    
    # Normalize Age using Min-Max scaling
    scaler = MinMaxScaler()
    df['age'] = scaler.fit_transform(df[['Age']])
    
    return df, labelDict
    

preprocess_dataframe(df)
df.head(1)
