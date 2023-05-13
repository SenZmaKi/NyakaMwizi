# Introduction
NyakaMwizi is a machine learning model built to detect potentially fraudulent transactions

The [dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection) used contains 1.3M instances and 23 features

# Visual insights
These are insights gained from exploring the data with graphs and computing percentages

They are in order of hierachy

## Time
- The time bracket under which the most fraudulent transactions occured is between 10:00PM and 4:00AM 
- *Binning the times into time intervals may prove to improve model performance (Implemented)*
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/1d198a07-ccdd-4138-a6aa-726a6a1d6da3)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/148ff0dc-f4ea-4294-a99e-bec7eade7585)


## Amount 
- Contrary to what you'd expect, most fraudulent transactions didn't involve exorbitant amounts of money
- Instead they involved both reasonable large amounts of money e.g instead of 200k, 30k and commonly spent amounts of money 
 ### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/a37111ac-d221-4bf9-863c-2acbe7e28129)
 ### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/06ff7e9d-20da-4669-9b01-d9ce122e5db7)

## Categories
- Certain transaction categories appeared to be fraudulent way more, to be specific category 4 and 11
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/7decc256-912e-4e6d-9c13-3787fd9d3ae5)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/97f56110-c157-4768-8b0d-6e728924fb11)


## Age 
- The age brackets that involved the most fraudulent transactions is 30 to 70
- But the same can be said for non-frauduelnt transactions so this insight may be a misinterpretation
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/9a9d3ca1-d409-4ca1-82d5-6de3931e8c0a)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/a98dcfa1-73c8-426a-9f86-a082dd250029)


## Longitude and latitude
- Some areas on the scatter matrix seemed to experience fraudulent transactions way more
### Scatter matrix for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/28441a92-6faa-4f24-a8f6-d031d134912f)
### Scatter matrix for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/30d97fa0-6b3f-41da-9e60-29fb40dd031c)


## Job 
- Specific jobs experienced fraud a little bit more, for example job 300
- But this behaviour is inline with what is observed with non fraudulent transactions so it may also be another misinterpretation
### Graph for frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/548952af-74da-44f0-ad4e-8b757d1bf021)
### Graph for non frauds
![image](https://github.com/SenZmaKi/NyakaMwizi/assets/90490506/94f1c0e4-ea95-4882-adf7-fda46686b0b6)
