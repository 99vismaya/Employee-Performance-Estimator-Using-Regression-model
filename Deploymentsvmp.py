# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:22:26 2022

@author: ADMIN
"""

echo "# streamlit-to-heroku-tutorial" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/your_username/your_repo_name.git
git push -u origin master

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

st.write("""
# Crop Recomendation
""")

crop_recommendation_model_path = 'C:/Users/ADMIN/SVMP_pkl_filename'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

month = st.selectbox("Select Month",['Select one','Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec'])

def main():
    s = pd.read_excel("C:/Users/ADMIN/Downloads/month_wise_medak_3.xlsx")
    labelencoder = LabelEncoder()

    labelencoder.fit(["0","yes","no"])
    a = labelencoder.transform(s['irrigation'])
    a = pd.DataFrame(a)
    a.columns = ["irrigation"]

    labelencoder.fit(['0', 'flower', 'fruit','grains','oil_seeds', 'other_commercial_crop','vegetable'])
    ct = labelencoder.transform(s['crop_type'])
    ct = pd.DataFrame(ct)
    ct.columns = ["crop_type"]

    labelencoder.fit(['0','clay','clay loam','deep black','deep loam','fertile loam','light loamy','loamy soil', 'red sandy loam','rich loam','sandy loam', 'sandy soil'])
    st = labelencoder.transform(s['Soil_type'])
    st = pd.DataFrame(st)
    st.columns = ["Soil_type"]

    labelencoder.fit(['0','one_sow_few_harvests' ,'one_sow_many_harvests','one_sow_one_harvest'])
    sh = labelencoder.transform(s['sow_and_harvest'])
    sh = pd.DataFrame(sh)
    sh.columns = ["sow_and_harvest"]

    labelencoder.fit(['0', 'intermediate_term', 'long_term','short_term'])
    ctr = labelencoder.transform(s['crop_term'])
    ctr = pd.DataFrame(ctr)
    ctr.columns = ["crop_term"]

    cdl = pd.concat([s, a, ct, st, sh, ctr], axis =1)
    cd_m = cdl.iloc[ : , [2,3,5,6,7,8,9,10,13,14,15,17,18,19,20,22,23,24,27,28,29,30,31]]
    cd_r = cdl.iloc[:600,[2]]
    z = cd_m.groupby(['month','Crop']).mean()
    y = z.values.tolist()
    x = pd.DataFrame(y)
    x = x.rename(columns={0:"crop_sown",1:"rainfall(mm)",2:"temp_avg(°C)",3:"humidity_avg(%)",4:"wind_speed_avg(Kmph)",5:"mrp(rs/kg)",6:"duration_in_months",7:"cost_of_cultivation_rs_per_ac",8:"Yield(kg/ac)",9:"avg_pH",10:"N(kg/ha)",11:"P(kg/ha)",12:"K(kg/ha)",13:"gross_profit(rs/ac)",14:"net_profit(rs/ac)",15:"ROI(%)",16:"irrigation",17:"crop_type",18:"Soil_type",19:"sow_and_harvest",20:"crop_term"})
    cd_r = sorted(cd_r['month'])
    x['month'] = cd_r

    cd_norm =(z-z.min())/(z.max()-z.min())
    predicted_values = crop_recommendation_model.predict(cd_norm)
    x["Crop"] = predicted_values
    x = x.iloc[:,[21,22,17,0,1,2,3,4,5,6,7,8,18,9,10,11,12,16,13,14,15,19,20]]
    x['irrigation'] = x['irrigation'].replace(1,'no')
    x['irrigation'] = x['irrigation'].replace(2,'yes')
    x['crop_type'] = x['crop_type'].replace(1,'flower')
    x['crop_type'] = x['crop_type'].replace(2,'fruit')
    x['crop_type'] = x['crop_type'].replace(3,'grains')
    x['crop_type'] = x['crop_type'].replace(4,'oil_seeds')
    x['crop_type'] = x['crop_type'].replace(5,'other_commercial_crop')
    x['crop_type'] = x['crop_type'].replace(6,'vegetable')
    x['Soil_type'] = x['Soil_type'].replace(1,'clay')
    x['Soil_type'] = x['Soil_type'].replace(2,'clay loam')
    x['Soil_type'] = x['Soil_type'].replace(3,'deep black')
    x['Soil_type'] = x['Soil_type'].replace(4,'deep loam')
    x['Soil_type'] = x['Soil_type'].replace(5,'fertile loam')
    x['Soil_type'] = x['Soil_type'].replace(6,'light loamy')
    x['Soil_type'] = x['Soil_type'].replace(7,'loamy soil')
    x['Soil_type'] = x['Soil_type'].replace(8,'red sandy loam')
    x['Soil_type'] = x['Soil_type'].replace(9,'rich loam')
    x['Soil_type'] = x['Soil_type'].replace(10,'sandy loam')
    x['Soil_type'] = x['Soil_type'].replace(11,'sandy soil')
    x['sow_and_harvest'] = x['sow_and_harvest'].replace(1,'one_sow_few_harvests')
    x['sow_and_harvest'] = x['sow_and_harvest'].replace(2,'one_sow_many_harvests')
    x['sow_and_harvest'] = x['sow_and_harvest'].replace(3,'one_sow_one_harvest')
    x['crop_term'] = x['crop_term'].replace(1,'intermediate_term')
    x['crop_term'] = x['crop_term'].replace(2,'long_term')
    x['crop_term'] = x['crop_term'].replace(3,'short_term')
    x = x.round()
    idx = x.loc[x['month'] == month]
    idx = idx.iloc[:,[1,2,21,22,9,10,11,12,19,20]]
    idx = idx.sort_values(by='ROI(%)',ascending = False)
    return(idx)

z = main()
v = z.head(10)
hide_table_row_index = """
            <style>
            .row_heading.level0{display:none}
            .blank{display:none}
            </style>
            """
st.markdown(hide_table_row_index,unsafe_allow_html=True)  

st.sidebar.header("Filters")
ct = st.sidebar.multiselect("Crop type",options = z['crop_type'].unique(),default =z['crop_type'].unique())
soil = st.sidebar.multiselect("Soil type",options = z['Soil_type'].unique(),default =z['Soil_type'].unique())
cp = st.sidebar.multiselect("Crop term",options = z['crop_term'].unique(),default =z['crop_term'].unique())
cd = st.sidebar.multiselect("Crop duration",options = z['duration_in_months'].unique(),default =z['duration_in_months'].unique())
cc = st.sidebar.multiselect("Cost of cultivation",options = z['cost_of_cultivation_rs_per_ac'].unique(),default =z['cost_of_cultivation_rs_per_ac'].unique())
m = v.query("crop_type == @ct & Soil_type == @soil & crop_term == @cp & duration_in_months == @cd & cost_of_cultivation_rs_per_ac == @cc ")
st.write(m)

a = v.melt("Crop",value_vars=["cost_of_cultivation_rs_per_ac","net_profit(rs/ac)"])

import altair as alt

chart = alt.Chart(a).mark_line().encode(
    x = alt.X('Crop:N'),
    y = alt.Y('value:Q'),
    color ='variable'
)

st.subheader('Plot of Crop vs Profit and Cost of cultivation')
st.altair_chart(chart,use_container_width = True)
