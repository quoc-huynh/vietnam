import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px
import seaborn as sns


us_df = pd.read_csv('us.csv')
vietnam_df = pd.read_csv('viet.csv')
aus_df = pd.read_csv('AUSTRALIA.csv')
korea_df = pd.read_csv('KOREA (SOUTH).csv')
laos_df = pd.read_csv('LAOS.csv')




st.set_page_config(page_title = "Vietnam At War", layout =  "wide")
st.title("Interactive Vietnam")

st.title("Operations By Country Info")
st.write("This interactive map showcases a random sample of operations by country. Unfortunately, the database was just too big to display all operations and will only display 2000 radnomly chosen points.")


st.subheader("US")
mission_lat_lon = us_df[['TGTLATDD_DDD_WGS84', 'TGTLONDDD_DDD_WGS84']].drop_duplicates().dropna()
mission_lat_lon = mission_lat_lon.rename(columns={"TGTLATDD_DDD_WGS84": "latitude", "TGTLONDDD_DDD_WGS84" : "longitude"})
us_mission_lat_lon = mission_lat_lon[pd.notnull(mission_lat_lon['latitude'])]
st.map(us_mission_lat_lon)   

st.subheader("South Vietnam")
mission_lat_lon = vietnam_df[['TGTLATDD_DDD_WGS84', 'TGTLONDDD_DDD_WGS84']].drop_duplicates().dropna()
mission_lat_lon = mission_lat_lon.rename(columns={"TGTLATDD_DDD_WGS84": "latitude", "TGTLONDDD_DDD_WGS84" : "longitude"})
vietnam_mission_lat_lon = mission_lat_lon[pd.notnull(mission_lat_lon['latitude'])]
st.map(vietnam_mission_lat_lon)   

st.subheader("Laos")
mission_lat_lon = laos_df[['TGTLATDD_DDD_WGS84', 'TGTLONDDD_DDD_WGS84']].drop_duplicates().dropna()
mission_lat_lon = mission_lat_lon.rename(columns={"TGTLATDD_DDD_WGS84": "latitude", "TGTLONDDD_DDD_WGS84" : "longitude"})
laos_mission_lat_lon = mission_lat_lon[pd.notnull(mission_lat_lon['latitude'])]
st.map(laos_mission_lat_lon)   

st.subheader("Korea")
st.write("No Data Was Found For Korea")

st.subheader("Australia")
mission_lat_lon = aus_df[['TGTLATDD_DDD_WGS84', 'TGTLONDDD_DDD_WGS84']].drop_duplicates().dropna()
mission_lat_lon = mission_lat_lon.rename(columns={"TGTLATDD_DDD_WGS84": "latitude", "TGTLONDDD_DDD_WGS84" : "longitude"})
aus_mission_lat_lon = mission_lat_lon[pd.notnull(mission_lat_lon['latitude'])]
st.map(aus_mission_lat_lon)
