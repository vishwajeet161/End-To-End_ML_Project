import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://vishu:vishu123@cluster0.xvifmrx.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
DATA_FILE_PATH = "D:\End-To-End_ML_Project\End-To-End_ML_Project\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"ROWS and COLUMNS: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
