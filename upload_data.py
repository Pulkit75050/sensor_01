from pymongo.mongo_client import MongoClient 
import pandas as pd
import json

# url
uri = "mongodb+srv://Pulkit123456:7505082898@cluster0.mgisu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create new client
client = MongoClient(uri)

# create database
DATABASE_NAME = "PWSKILLS"
COLLECTION_NAME="WAFERFAULT"

df = pd.read_csv("C:\Users\pulki\Downloads\sensor project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

json_record= list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)