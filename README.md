**🏏 T20 Match Win Predictor**

This project predicts the win probability of the chasing team in international T20 matches using ball-by-ball data from 2006–2023.
It analyzes the evolving match situation — runs required, balls remaining, wickets left, and run rates — to model the likelihood of a win.

📘 **Overview**

Cricket’s unpredictable nature makes win prediction a fascinating machine learning problem.
By using real match data, this notebook explores how different game states influence outcomes and builds a predictive framework to estimate win chances at any moment during a chase.

🗂️ **Dataset Details**

Source: Ball-by-ball data from international T20 matches (2006–2023)

**Files Used:**

matches → Match-level data (Match ID, Venue, Winner, Bat First, Bat Second, Target Score)

deliveries → Ball-by-ball data (Runs, Balls Remaining, Required Runs, Current Score, etc.)

Filtered Teams: Active international teams and T20 World Cup 2024 participants only.

Focus: Second innings (chasing side only).

⚙️ **Data Processing Steps**

**Data Cleaning**

Removed null values and irrelevant columns

Standardized team names

Filtered out non-international and incomplete matches

**Feature Engineering**

Current Score – total runs scored so far

Wickets Left – wickets remaining for the batting team

Required Runs – runs needed to win

Balls Remaining – deliveries left in the innings

Required Run Rate (RR) = (Required Runs / Balls Remaining) × 6

Current Run Rate (CR) = (Current Score / Balls Bowled) × 6

**Dataset Refinement**

Kept only second-innings data (useful for win probability modeling)

Removed unnecessary columns like Player Out and Method

🧠 **Modeling**

While the notebook primarily focuses on data preprocessing and feature creation, it is designed to feed into a machine learning model that can predict the probability of winning.
Typical algorithms suited for this problem include:

Logistic Regression

Random Forest

XGBoost


📊 **Key Features Summary**
Feature	Description
Current Score	Total runs scored so far
Wickets Left	Remaining wickets (10 - fallen wickets)
Required Runs	Runs needed to win
Balls Remaining	Deliveries left in the innings
RR	Required run rate
CR	Current run rate
🧩 Tools & Libraries
Category	Libraries Used
Data Analysis	pandas, numpy
Visualization	matplotlib, seaborn (if used later)
ML (extendable)	scikit-learn, xgboost

📈 **Future Improvements**

Add machine learning models for probability prediction

Integrate live or recent match data for real-time analysis

Create an interactive dashboard using Streamlit

Perform feature importance analysis and model evaluation

👨‍💻 **Author**

Lalit Jingar
📧 lalitjingar90@gmail.com
🌐 https://www.linkedin.com/in/lalit-jingar/
⭐ If you like this project, consider giving it a star!




