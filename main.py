import streamlit as st

st.title("我的專屬 BMI 計算機")

# 建立網頁輸入框
height_cm = st.number_input("請輸入身高 (公分)", min_value=1.0, max_value=250.0)
weight = st.number_input("請輸入體重 (公斤)", min_value=1.0, max_value=300.0)

# 將身高轉換為公尺進行計算
height_m = height_cm / 100
bmi = weight / (height_m * height_m)

# 顯示結果
st.write(f"### 您的 BMI 指數為：{bmi:.1f}")

# 加上簡單的判斷
if bmi < 18.5:
    st.info("您的體重過輕，要多吃點喔！")
elif 18.5 <= bmi < 24:
    st.success("太棒了！您的體重在正常範圍內。")
else:
    st.warning("您的體重稍重，記得多運動喔！")