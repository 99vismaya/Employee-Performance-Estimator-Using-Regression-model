# Employee-Performance-Estimator-Using-Regression-model
# Project goal and introduction

Project related to Employee performance prediction. This app predict performance of employee considering different features when working from home. By evaluating employees performance, we can suggest them to take a appropriate action and make changes in their strategies for individual and  organization growth.
Scope of this project is to motivate, enhance employees skills set both psychological and technical so that they can  increase their productivity and perform effectively towards organization goals.

# About data
Data is pulled from the SQL database where employee data is stored. It has 5100 records and 28 fields.7 numerical and 21 categorical features
Target variable - Performance Rating. It is a continuous

# Model building
As output variable is continuous, regression models are trained. Decision tree, Random forest, Ada Boost, Gradient Boost, XGboost, Multinomial Regression are some models trained and Gradient boost model with RMSE 0.01 and R2 score 0.99 is selected for model building

Deployment
Streamlit framework is used for app building.Cloud deployment is done in Streamlit cloud deployment platform. Using features performance is predicted and is displayed with other employee details. Department filter is added to filter employees based on deparment. We can also get prediction along with employee details for individual employee.

App Link:https://99vismaya-employee-performance-estimator-using-regre-app-lcn0hy.streamlit.app/

# App

![Streamlit - Google Chrome 12-01-2023 11_08_08](https://user-images.githubusercontent.com/106010576/211986604-c8430522-4c38-49d5-8069-7d8f95dc9eee.png)

