# Employee-Performance-Estimator-Using-Regression-model
# Project goal and introduction

Project related to Employee performance prediction. This app predict performance of employee considering different features when working from home. By evaluating employees performance, we can suggest them to take a appropriate action and make changes in their strategies for individual and  organization growth.
Scope of this project is to motivate, enhance employees skills set both psychological and technical so that they can  increase their productivity and perform effectively towards organization goals.

# About data
Data is pulled from the SQL database where employee data is stored. It has 5100 records and 28 fields.7 numerical and 21 categorical features
Target variable - Performance Rating. It is a continuous

# Model building
As output variable is continuous, regression models are trained and Gradient boost model with 96% accuracy is selected for model building

Deployment
Streamlit framework is used for app building. Using features performance is predicted and is displayed with other employee details. Department filter is added to filter employees based on deparment. We can also get prediction along with employee details for individual employee.

App Link:https://employee02.herokuapp.com/
