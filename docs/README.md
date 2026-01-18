# Student Performance Dashboard

This project analyzes student performance using Python and Streamlit to understand the key factors influencing exam scores.

## 📁 Dataset
- 6,607 students  
- 20 features  
- Includes study habits, attendance, socio-economic factors, and exam scores  

## 🛠️ Tools Used
- Python  
- Pandas  
- Matplotlib  
- Streamlit  
- Jupyter Notebook  

## 📊 What the Dashboard Shows

### Page 1 — Overview
- Total students  
- Average exam score  
- Average attendance  
- Dataset preview  

### Page 2 — Performance Drivers
- Attendance vs Exam Score  
- Hours Studied vs Exam Score  

### Page 3 — Equity & Context
- Average score by Family Income  
- Average score by School Type  

## ▶️ How to Run the Project

1. Create and activate a virtual environment:
-python -m venv venv
-source venv/Scripts/activate

2. Install dependencies:
-pip install -r requirements.txt

3. Run the dashboard:
-streamlit run dashboard/app.py

## Live Link 
-> https://aaftab-student-performance.streamlit.app/