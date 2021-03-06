# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:45:38 2022

@author: ADMIN
"""
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

st.markdown('<p style ="text-align: center; color:Green; font-size: 40px;font-family:serif;" > EMPLOYEE PERFORMANCE CALCULATING APP </p>',unsafe_allow_html=True)    
st.write("Calculated employee performance rating along with employee details")

emp_perf_model_path = open("GB_pkl_filename.pkl","rb")
emp_perf_model=pickle.load(emp_perf_model_path)

from openpyxl import load_workbook
wb = load_workbook('p_67.xlsx')
ws = wb.active
df = ws.values
columns = next(df)[0:]
dz = pd.DataFrame(df, columns=columns)

def main():
    cd = dz
    labelencoder = LabelEncoder()
    cd["Gender"]= labelencoder.fit_transform(cd["Gender"])
    cd["MaritalStatus"]= labelencoder.fit_transform(cd["MaritalStatus"])
    cd["EducationBackground"]= labelencoder.fit_transform(cd["EducationBackground"])
    cd['EmpDepartment'] = labelencoder.fit_transform(cd['EmpDepartment'])
    cd['EmpJobRole'] = labelencoder.fit_transform(cd['EmpJobRole'])
    cd['BusinessTravelFrequency']= labelencoder.fit_transform(cd['BusinessTravelFrequency'])
    cd['Attrition'] = labelencoder.fit_transform(cd['Attrition'])
    cd['Willingtowfh_wfo'] = labelencoder.fit_transform(cd['Willingtowfh_wfo'])

    #Data prepration for normalization
    cd_n = cd.iloc[:,[7,8,9,10,11,12,13,14,15,16,17,18,20,22,23,24,25,26]] 
    cd_r = cd.iloc[:,[1,2,3,4,5,6,19,21]]

    # Normalization
    def norm_func(i):
    	x = (i-i.min())	/(i.max()-i.min())
    	return(x)

    cd_norm = norm_func(cd_n)
    cd_norm.describe()

    cdl = pd.concat([cd_norm,cd_r], axis =1)

    predicted_values = emp_perf_model.predict(cdl)
    predicted_values = pd.DataFrame(predicted_values)
    predicted_values.columns = ['Empperformanceratinginwfh']
    predicted_values = predicted_values.round(1)
    y = cd.iloc[:,[0,4]]
    x = cd.iloc[:,[28,29]]
    op = pd.concat([y,predicted_values,x],axis=1)
    op = op.iloc[:,[1,0,2,3,4]]
    op['EmpDepartment'] = op['EmpDepartment'].replace(0,'Data Science')
    op['EmpDepartment'] = op['EmpDepartment'].replace(1,'Development')
    op['EmpDepartment'] = op['EmpDepartment'].replace(2,'Finance')
    op['EmpDepartment'] = op['EmpDepartment'].replace(3,'Human Resources')
    op['EmpDepartment'] = op['EmpDepartment'].replace(4,'Research & Development')
    op['EmpDepartment'] = op['EmpDepartment'].replace(5,'Sales')
    op = op.sort_values(by='EmpNumber',ascending = True)
    return(op)

z = main()
hide_table_row_index = """
            <style>
            .row_heading.level0{display:none}
            .blank{display:none}
            </style>
            """
st.markdown(hide_table_row_index,unsafe_allow_html=True)  
dp = st.sidebar.multiselect("Department",options = z['EmpDepartment'].unique(),default =z['EmpDepartment'].unique())
v = z.query("EmpDepartment == @dp")
st.write(v)

st.write("To get performance rating of individual employee enter employee number") 
g = st.text_input('EmpNumber')
h = z.query("EmpNumber==@g")
st.write(h)
