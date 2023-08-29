# Introduction
NyakaMwizi is a machine learning model built to detect potentially fraudulent transactions

The [dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection) used contains 1.3M instances and 23 features

# Table of Contents
1. [How to test out the model](#how-to-test-out-the-model)
2. [Visual Insights](#visual-insights)
3. [Final Model Performance](#final-model-performance)

# How to test out the model
Ensure you have [Python](https://www.python.org/downloads/) (version 3.11 or newer) and [Git](https://github.com/git-guides/install-git) installed. For Linux users you also have to create a [Python virtual environment](https://docs.python.org/3/library/venv.html), the same is recommended for Mac and Windows, but you don't have to.

Run the following commands

```
git clone https://github.com/SenZmaKi/NyakaMwizi
cd NyakaMwizi
pip install -r requirements.txt
python test_model.py
```

# Visual Insights
These are insights I gained as I was exploring the data-set with graphs and computations

They are in order of hierachy

## Time
- The time bracket under which the most fraudulent transactions occured is between 10:00PM and 4:00AM 
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/1d198a07-ccdd-4138-a6aa-726a6a1d6da3)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/148ff0dc-f4ea-4294-a99e-bec7eade7585)


## Amount 
- Contrary to what you'd expect, most fraudulent transactions didn't involve exorbitant amounts of money
- Instead they involved both reasonably large amounts of money e.g 30k and average amounts of money 
 ### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/a37111ac-d221-4bf9-863c-2acbe7e28129)
 ### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/06ff7e9d-20da-4669-9b01-d9ce122e5db7)

## Categories
- Certain transaction categories appeared to be way more fraudulent, to be specific category 4 and 11
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/7decc256-912e-4e6d-9c13-3787fd9d3ae5)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/97f56110-c157-4768-8b0d-6e728924fb11)


## Age 
- The age brackets that involved the most fraudulent transactions is 30 to 70
- But the same can be said for non-fraudulent transactions so this insight may be a misinterpretation
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/9a9d3ca1-d409-4ca1-82d5-6de3931e8c0a)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/a98dcfa1-73c8-426a-9f86-a082dd250029)


## Longitude and latitude
- Some areas on the scatter matrix seemed to experience more fraudulent transactions
### Scatter matrix for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/28441a92-6faa-4f24-a8f6-d031d134912f)
### Scatter matrix for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/30d97fa0-6b3f-41da-9e60-29fb40dd031c)


## Job 
- Specific jobs experienced more fraudulent transactions e.g, job 300
- But this behaviour is inline with what is observed with non-fraudulent transactions so it may also be another misinterpretation
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/548952af-74da-44f0-ad4e-8b757d1bf021)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/94f1c0e4-ea95-4882-adf7-fda46686b0b6)

# Final Model Performance
- [Model](https://github.com/SenZmaKi/NyakaMwizi/blob/master/model.pkl): DecisionTreeClassifier
- Precision: 82.88%
- Recall: 17.12%
