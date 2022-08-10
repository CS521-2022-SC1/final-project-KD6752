<h1 align="center">Final Project: Data Analysis with Python</h1>

## Instructions

[instructions.pdf](instructions.pdf)

## Topic

Predicting Housing Prices (Linear Regression)
comparing with random forest and gradient boosting models

## Description
In this project we basically trying to use Machine Learning to predict house sale price.
we used three models namely Linear regression, random forest regression and gradient boosting.
the data we have is a raw data, we had to do preprocessing before analyzing the data. we dropped 
few columns  that has high number of NaN values that has no effect on determining sale price.We 
also used dropna method to drop NaN values.To deal with outliers, we used 3sd threshold value. we 
got rid of data that are outside 3sd from mean.

## Project Requirements/technology used

there are several technology/application we need to complete this project
beside Python,Jupytor notebook and Git/Github, we also use ML module i.e.
linear regressor,random forest regressor, and gradient boosting. we have 
also used numpy,scipy,pandas,matplotlib which all are the extension of
python modules.

##Use of project
For predicting price of house,we need to have attributes availble, for example
we need to have value of overall quality of hous, gross living area, garage size
external quality of huse, kithchen quality  and we can put these value to as a
X_test in following equations
predictions = model.predict(X_test)
where model can be linear, random forest or gradient boosting.

##Credits/Appreciation

two people were involved in this project those are the authors listed bottom of
this file. we also like to appreciate guide from our preffesor Alan Burstein and
our TA,Yingshi Huang.

## Datasets

[House Prediction Data.csv](https://github.com/bursteinalan/Data-Sets/tree/master/Housing)

## Tech Stack

- Python
- Jupyter
- Git/GitHub

## Authors

[Kokil Dhakal](https://github.com/KD6752)

[Dan Hoogasian](https://github.com/)  
