import joblib
import pandas as pd
from sklearn import metrics
from sklearn import preprocessing
import datetime
import sys
import time
import opendatasets
import os


def download_test_data_set():
    if not os.path.exists(os.path.join("fraud-detection", "fraudTest.csv")):
        slow_print("Downloading test data set")
        opendatasets.download("https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTest.csv", force=True)

def select_features(df: pd.DataFrame, features: list[str])->pd.DataFrame:
    copy = df.copy()
    for feat in df.columns:
        if feat not in features:
            copy = copy.drop(feat, axis=1)
    return copy

def display_confusion_matrix(confusion_matrix: list[list[int]], non_fraud, fraud):
    nonfraud_count = len(non_fraud)
    fraud_count = len(fraud)
    print(confusion_matrix)
    print("\nPredictions non-fraud  fraud\n")
    true_positive_non_fraud = round(confusion_matrix[0][0]/nonfraud_count*100, 2)
    false_positive_non_fraud = round(confusion_matrix[0][1]/nonfraud_count*100, 2)
    true_positive_fraud = round(confusion_matrix[1][0]/fraud_count*100, 2)
    false_positive_fraud = round(confusion_matrix[1][1]/fraud_count*100, 2)
    print(f"Non fraud   {true_positive_non_fraud}%     {false_positive_non_fraud}%\n")
    print(f"Fraud       {true_positive_fraud}%     {false_positive_fraud}%")

def process_features(df: pd.DataFrame)->pd.DataFrame:
    new_df = df.drop(columns=["Unnamed: 0", "cc_num", "city", "street", "state", "zip", "trans_num"], axis=1)
    #Generate age and drop dob
    current_year = datetime.datetime.now().year
    new_df["age"]= new_df["dob"].apply(lambda x: current_year - int(x.split("-")[0]))
    new_df = new_df.drop(columns=["dob"], axis=1)
    #Remove the weird fraud_ thing that comes before a merchants name and rename merchant to merch_name
    new_df["merchant"] = new_df["merchant"].apply(lambda x: x.split("fraud_")[1]) 
    new_df = new_df.rename(columns={"merchant":"merch_name"})
    #Combine first and last name into full name then drop the them
    new_df["full_name"] = new_df["first"]+" "+new_df["last"] 
    new_df = new_df.drop(columns=["first", "last"], axis=1)
    #Drop unix time
    new_df = new_df.drop(columns=["unix_time"], axis=1)
    datetime_format = "%Y-%m-%d %H:%M:%S"
    new_df["dow"] = new_df["trans_date_trans_time"].apply(lambda x: datetime.datetime.strptime(x, datetime_format).weekday())
    new_df["dom"] = new_df["trans_date_trans_time"].apply(lambda x: int(x.split("-")[2].split(" ")[0]))
    new_df["month"] = new_df["trans_date_trans_time"].apply(lambda x: int(x.split("-")[1]))
    new_df["year"] = new_df["trans_date_trans_time"].apply(lambda x: int(x.split("-")[0]))
    def process_time(time:str)->float:
        times = time.split(" ")[1].split(":")
        time_float = float(times[0])+float(times[1])/60
        return time_float

    new_df["time"] = new_df["trans_date_trans_time"].apply(process_time)
    new_df.drop(columns=["trans_date_trans_time"], axis=1)
    new_df["time_interval"] = pd.cut(new_df["time"], bins=12).astype(str)
    new_df["amt_interval"] = pd.cut(new_df["amt"], bins=6).astype(str)
    new_df["age_interval"] = pd.cut(new_df["age"], bins=6).astype(str)
    new_df["city_pop_interval"] = pd.cut(new_df["city_pop"], bins=6).astype(str)
    new_column_order = ["full_name", "gender", "age", "age_interval", "job", "lat", "long", "city_pop", "city_pop_interval", "merch_name", "merch_lat", "merch_long", "amt", "amt_interval", "category", "time", "time_interval", "dow", "dom", "month", "year", "is_fraud"]
    return new_df.reindex(columns=new_column_order)
    

def label_encode(df: pd.DataFrame, cat_features: list[str])->pd.DataFrame:
    encoder = preprocessing.LabelEncoder()
    df_copy = df.copy()
    for feat in cat_features:
        df_copy[feat] = encoder.fit_transform(df_copy[feat])
    return df_copy


def slow_print(text, delay_time=0.01): 
    for character in text:      
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(delay_time)
    sys.stdout.write("\n")

slow_print("Loading model")
model, features, target_class = joblib.load("model.pkl")
slow_print("Loading data set")
download_test_data_set()
data_set = pd.read_csv(os.path.join("fraud-detection", "fraudTest.csv"))


y = data_set[target_class]
x = data_set.drop(target_class, axis=1)
non_fraud = y[y==0]
fraud = y[y==1]


cat_features = ["full_name", "gender", "job", "merch_name", "category", "time_interval", "age_interval", "amt_interval", "city_pop_interval"]
slow_print("Performing feature selection and extraction")
x = process_features(x)
slow_print("Performing label encoding")
x = label_encode(x, cat_features)
slow_print("Performing final feature selection")
x = select_features(x, features)

# instance = 69
# predictiion = model.predict([x.loc[instance]])

# if predictiion == 1 and predictiion == [y.loc[instance]]:
#     slow_print(f"Correctly flagged instance {instance} as FRAUD")

# elif predictiion == 0 and predictiion == y[instance]:
#     slow_print(f"Correctly flagged instance {instance} as NON-FRAUD")

# else:
#     slow_print("Incorrect classification")

slow_print("Generating confusion matrix\n")
display_confusion_matrix(metrics.confusion_matrix(y, model.predict(x)), non_fraud, fraud)