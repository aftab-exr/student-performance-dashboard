import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Overview", "Performance Drivers", "Equity & Context"]
)


df = pd.read_csv(r"..\data\StudentPerformanceFactors.csv")

# ---- FILTER ----
if page == "Overview":

    st.title("📊 Student Performance Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students", df.shape[0])

    with col2:
        st.metric("Average Exam Score", round(df["Exam_Score"].mean(), 2))

    with col3:
        st.metric("Average Attendance", round(df["Attendance"].mean(), 2))

    st.subheader("Dataset Preview")
    st.write(df.head())
elif page == "Performance Drivers":

    st.title("🔍 What Drives Performance?")

    st.subheader("Attendance vs Exam Score")
    fig1, ax1 = plt.subplots()
    ax1.scatter(df["Attendance"], df["Exam_Score"])
    ax1.set_xlabel("Attendance")
    ax1.set_ylabel("Exam Score")
    st.pyplot(fig1)

    st.subheader("Hours Studied vs Exam Score")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["Hours_Studied"], df["Exam_Score"])
    ax2.set_xlabel("Hours Studied")
    ax2.set_ylabel("Exam Score")
    st.pyplot(fig2)
elif page == "Equity & Context":

    st.title("⚖️ Equity & Context Analysis")

    st.subheader("Average Score by Family Income")
    fig3, ax3 = plt.subplots()
    df.groupby("Family_Income")["Exam_Score"].mean().plot(kind="bar", ax=ax3)
    ax3.set_ylabel("Average Exam Score")
    st.pyplot(fig3)

    st.subheader("Average Score by School Type")
    fig4, ax4 = plt.subplots()
    df.groupby("School_Type")["Exam_Score"].mean().plot(kind="bar", ax=ax4)
    ax4.set_ylabel("Average Exam Score")
    st.pyplot(fig4)
