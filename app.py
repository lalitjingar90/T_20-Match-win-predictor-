import streamlit as st
import joblib
import pandas as pd

# Load the model
clf = joblib.load("clf.joblib")

Teams = ['South Africa', 'Ireland', 'Australia', 'Pakistan', 'Sri Lanka',
       'Afghanistan', 'Zimbabwe', 'West Indies', 'Scotland',
       'Netherlands', 'New Zealand', 'England', 'United Arab Emirates',
       'Bangladesh', 'India', 'Nepal', 'Papua New Guinea', 'Hong Kong',
       'Oman', 'Namibia', 'United States of America', 'Kenya', 'Canada',
       'Austria', 'Denmark']

Venues = ['SuperSport Park', "Lord's", 'Bellerive Oval',
       'Al Amerat Cricket Ground Oman Cricket (Ministry Turf 1)',
       'Pallekele International Cricket Stadium', 'R Premadasa Stadium',
       'The Village', 'Sharjah Cricket Stadium',
       'Shere Bangla National Stadium',
       'Dubai International Cricket Stadium',
       'Civil Service Cricket Club', 'Grange Cricket Club Ground',
       'Sydney Cricket Ground', 'Hagley Oval', 'The Rose Bowl',
       'Coolidge Cricket Ground', 'ICC Academy',
       'Saurashtra Cricket Association Stadium',
       'Rajiv Gandhi International Cricket Stadium', 'Wankhede Stadium',
       'Al Amerat Cricket Ground Oman Cricket (Ministry Turf 2)',
       'Beausejour Stadium', 'Arun Jaitley Stadium', 'Kensington Oval',
       'Manuka Oval', 'OUTsurance Oval', 'Sophia Gardens',
       'Zayed Cricket Stadium', 'Adelaide Oval',
       'Vidarbha Cricket Association Stadium', 'Trent Bridge',
       'Sheikh Abu Naser Stadium', 'Newlands',
       'JSCA International Stadium Complex', 'Old Trafford',
       'Greenfield International Stadium', 'Holkar Cricket Stadium',
       'MA Chidambaram Stadium', 'Providence Stadium',
       'Mission Road Ground', 'Harare Sports Club',
       'Sheikh Zayed Stadium', 'National Stadium', 'Arnos Vale Ground',
       'New Wanderers Stadium', 'Eden Park', 'County Ground',
       'Tribhuvan University International Cricket Ground',
       'M.Chinnaswamy Stadium', 'Riverside Ground',
       'Western Australia Cricket Association Ground', 'VRA Ground',
       'Kingsmead', 'Eden Gardens', 'McLean Park',
       'National Cricket Stadium', 'Kennington Oval', 'Seddon Park',
       'Rawalpindi Cricket Stadium', 'Khan Shaheb Osman Ali Stadium',
       'GMHBA Stadium', "St George's Park", 'ICC Academy Ground No 2',
       'Mahinda Rajapaksa International Cricket Stadium', 'Warner Park',
       'Punjab Cricket Association Stadium', 'Sylhet Stadium',
       'Melbourne Cricket Ground', 'The Wanderers Stadium',
       'Maharashtra Cricket Association Stadium',
       'Rajiv Gandhi International Stadium', "Queen's Park Oval",
       'Punjab Cricket Association IS Bindra Stadium', 'Westpac Stadium',
       'Central Broward Regional Park Stadium Turf Ground',
       'M Chinnaswamy Stadium', 'Hazelaarweg', 'Castle Avenue',
       'Gaddafi Stadium', 'Wanderers Cricket Ground', 'Stadium Australia',
       'Windsor Park', 'Bready Cricket Club', 'Sportpark Westvliet',
       'Perth Stadium', 'Senwes Park', 'Gymkhana Club Ground',
       'Zahur Ahmed Chowdhury Stadium', 'ICC Global Cricket Academy',
       'Mombasa Sports Club Ground', 'Green Park',
       'Subrata Roy Sahara Stadium', 'Bay Oval', 'Boland Park',
       'Edgbaston', 'Himachal Pradesh Cricket Association Stadium',
       'Indian Association Ground', 'Narendra Modi Stadium',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
       'R.Premadasa Stadium', 'Brisbane Cricket Ground', 'Buffalo Park',
       'Carrara Oval', 'Sawai Mansingh Stadium',
       'Greater Noida Sports Complex Ground', 'Malahide', 'Sabina Park',
       'Barabati Stadium', 'Headingley', 'P Sara Oval',
       'Tony Ireland Stadium', 'Sir Vivian Richards Stadium',
       'Goldenacre', 'Queens Sports Club',
       'Sylhet International Cricket Stadium',
       'Darren Sammy National Cricket Stadium', 'Grange Cricket Club',
       'Tolerance Oval', 'Simonds Stadium', 'Bulawayo Athletic Club',
       'Sportpark Het Schootsveld', 'Feroz Shah Kotla',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'AMI Stadium', 'Terdthai Cricket Ground', 'Moses Mabhida Stadium',
       'Mangaung Oval', 'Sardar Patel Stadium', 'John Davies Oval',
       'University Oval', 'Jade Stadium', 'White Hill Field',
       'Brian Lara Stadium', 'Clontarf Cricket Club Ground',
       'Brabourne Stadium', 'Sky Stadium', 'Maple Leaf North-West Ground',
       'Barsapara Cricket Stadium', 'Saxton Oval',
       'De Beers Diamond Oval']

clf = pickle.load(open("clf.pkl","rb"))
st.title('Match Win Predictor')

col1, col2=st.columns(2)

with col1:
    Batting_Team = st.selectbox("Select the Batting Team",Teams)
with col2:
    Bowling_Team =  st.selectbox("Select the Bowling Team",Teams)


Venue = st.selectbox('Select Match Venue', Venues) 

Target =  st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input("Score")
with col4:
    Overs = st.number_input("Overs completed")
with col5:
    Wickets = st.number_input("Wickets Fallen")

import pandas as pd

if st.button("Predict Probability"):
    Run_Remaining = Target - score
    Balls_left = 120-(Overs*6)
    Wickets = 10-Wickets
    CRR = score/Overs
    RRR = (Run_Remaining*6)/Balls_left

    input_df = pd.DataFrame({'Batting Side':[Batting_Team],"Bowling Side":[Bowling_Team],'Venue': [Venue],"Required Runs":[Run_Remaining],"Balls Remaining":[Balls_left],"Wickets Left":[Wickets],
                  "Target Score":[Target],"CR":[CRR],"RR":[RRR]})

    result = clf.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.text(Batting_Team + " " + str(round(win*100)) +"%")
    st.text(Bowling_Team + " " + str(round(loss*100)) +"%")
