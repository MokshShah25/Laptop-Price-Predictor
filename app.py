import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open("pipe.pkl","rb"))
df = pickle.load(open("df.pkl","rb"))
st.title("Laptop Price Predictor")

brand = st.selectbox("Brand",df["Company"].unique())
Type = st.selectbox("Type",df["TypeName"].unique())
Ram = st.selectbox("RAM",sorted(df["Ram"].unique()))
Weight = st.number_input(
    "Weight (kg): ",
    min_value=0.5,
    max_value=5.0,
    value=2.0
)
touchscreen = st.selectbox("TouchScreen",["YES","NO"])
ips = st.selectbox("IPS",["YES","NO"])
screen_size = st.number_input("Screen Size: ", min_value=10.0, max_value=20.0, value=15.6)

resolution = st.selectbox("Screen Resolution",['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox("CPU",df["Cpu_brand"].unique())
hdd = st.selectbox("HDD(in GB)",sorted(df["HDD"].unique()))
ssd = st.selectbox("SSD(in GB)",sorted(df["SSD"].unique()))
gpu = st.selectbox("GPU",df["Gpu_brand"].unique())
os = st.selectbox("OS",df["OS"].unique())

if st.button("Predict Price"):
    if touchscreen == "YES":
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "YES":
        ips = 1
    else:
        ips = 0
        
    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])
    ppi = ((x_res**2) + (y_res**2))**0.5/screen_size

    query = pd.DataFrame([{
    "Company": brand,
    "TypeName": Type,
    "Ram": Ram,
    "Weight": Weight,
    "TouchScreen": touchscreen,
    "Ips": ips,
    "ppi": ppi,
    "Cpu_brand": cpu,
    "HDD": hdd,
    "SSD": ssd,
    "Gpu_brand": gpu,
    "OS": os
    }])
    prediction = pipe.predict(query)[0]

    price = np.exp(prediction)

    st.success(f"Predicted Price: ₹{price:,.0f}")