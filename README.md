<h1 align="center">Final Project: Data Analysis with Python</h1>

## Instructions

[instructions.pdf](instructions.pdf)

## Topic

Predicting Housing Prices (Linear Regression)
comparing with random forest and gradient boosting models

## Description
In this project we basically trying to use Machine Learning to predict house sale price.
we used three models namely Linear regression, random forest regression and gradient boosting.
the data we have is a raw data, we had to do pre-processing before analyzing the data. we dropped 
few columns  that has high number of NaN values that has no effect on determining sale price.We 
also used dropna method to drop NaN values.To deal with outliers, we used 3sd threshold value. we 
got rid of data that were outside 3sd from mean.

## Project Requirements/technology used

There are several technology/application we need to complete this project.
We use Python,Jupytor notebook, Git/Github and ML module i.e.
linear regressor,random forest regressor, and gradient boosting.We  
also use numpy,scipy,pandas,matplotlib modules which all are python modules and
important ones.

## Steps used to get results:

### Getting data sets
we get our data from github url mentioned here.
[House Prediction Data.csv](https://github.com/bursteinalan/Data-Sets/tree/master/Housing)

### Cleaning Data:
There were 81 columns including index, we dropped columns indexed 0,3,6,57,72,73,74 that have high number of null values and also not significant effect on our target attributes, 'SalePrice'. After that using pandas, we converted categorical data to numerical data. Also, we dropped  rows that have at least one NaN value. Finally, we removed outliers outside 3sd from mean using pandas.We have 1350 by 74 dimension data frame in the end.

### Finding highely correlated attributes(columns):
We use following script to find the highly correlated columns with 'SalePrice',where df_filtered is cleaned data frame.

correl_dict = dict()
for column in df_filtered.columns[:-1]:
    correl_dict[column] = sp.linregress(df_filtered[column], df_filtered['SalePrice']).rvalue
correl_df = pd.DataFrame.from_dict(correl_dict, orient='index', columns=['Correl coef'])

There were  six columns those are highly correlated with 'SalePrice' column.We took those columns as our
feature attributes. Those are 'OverallQual','ExterQual', 'GrLivArea',,KitchenQual','GarageCars', and
'GarageArea'. Finally, we have data set of 1350 by 7 size for fitting our models.

### dividing data into train and test set:
We use following SKlearn sript to split our data set
X=df_filtered.drop(['SalePrice'],axis=1)
y=df_filtered['SalePrice']

X_train,X_test,y_train,y_test,=train_test_split(X,y,test_size=0.30,random_state=10)
X_train.shape,X_test.shape

We chose 30% of our total data for testing and 70% for training the models, we also give some flexibility with randomness(random_state=10) of choosing data for test and train from original 
data set.

### fitting different models and finding errors and aacuracy:
We use three different regressor models namely 'Linear Regression', 'Random Forest' and
'Gradient Boosting' using SKLearn, which is basically to import the model and fit in our data
set. While fitting models, we found that there is a little  more residual error produced by
Linear regression and hence has a bit less accurate(~80%) than  random forest(~82%) and gradient boosting(~82%) models, both of which have little less error and higher accuracy in fitting model. 


## Use of project:
For predicting price of house,we need to have attributes available, for example
we need to have value of overall quality of house, gross living area, garage size
external quality of house and kitchen quality  and we can put these value to as a
X_test in following equations
predictions = model.predict(X_test)
where model can be linear, random forest or gradient boosting.

## Credits/Appreciation:

two people were involved in this project those are the authors listed at bottom of
this file. we are also like to appreciate guidance from our professor Alan Burstein and
TA Yingshi Huang.


## Tech Stack

- Python
- Jupyter
- Git/GitHub

## Authors

[Kokil Dhakal](https://github.com/KD6752)

[Dan Hoogasian](https://github.com/)  
