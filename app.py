# import streamlit as st 
# import pandas as pd
# import pickle

# teams = ['Sunrisers Hyderabad',
#  'Mumbai Indians',
#  'Royal Challengers Bangalore',
#  'Kolkata Knight Riders',
#  'Kings XI Punjab',
#  'Chennai Super Kings',
#  'Rajasthan Royals',
#  'Delhi Capitals']

# cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
#        'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
#        'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#        'Sharjah', 'Mohali', 'Bengaluru']

# st.title("IPL Winner Probability Predictiopn")
# model = pickle.load(open('model.pkl', 'rb'))

# col1, col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Select the batting team', sorted(teams))

# with col2:
#     bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# city = st.selectbox('select host city', sorted(cities))

# target = st.number_input('Target')

# col3, col4, col5 = st.columns(3)

# with col3:
#     score = st.number_input('Score')

# with col4:
#     overs = st.number_input('Over completed')

# with col5:
#     wicket = st.number_input('Wicket outs')

# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs*6)
#     wicket = 10 - wicket
#     crr = score/overs
#     rrr = (runs_left*6)/balls_left

#     input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wicket':[wicket],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

#     result = model.predict_proba(input_df)

#     loss = result[0][0]
#     win = result[0][1]

#     st.header(batting_team + " - " + str(round(win*100))+"%")
#     st.header(bowling_team + " - " + str(round(loss*100))+"%")


#     # st.header("hdjfgh")




# # Run your applicataion
# # streamlit run app.py


import streamlit as st
import pandas as pd
import pickle

# Set page configuration
st.set_page_config(page_title="IPL Winner Predictor", page_icon="🏏", layout="centered")


st.markdown(f"""
    <style>
       

        /* Overlay for Readability */
        .stApp {{
            background: rgba(0, 0, 0, 0.6);
            padding: 10px;
            border-radius: 10px;
        }}

        /* Title and Headers */
        .stTitle, .stHeader {{
            color: white !important;
            text-align: center;
        }}

        /* Select Boxes & Number Inputs */
        .stSelectbox, .stNumber_input label {{
            color: white !important;
        }}

        /* Prediction Button */
        .stButton > button {{
            background-color: #28A745;  /* Green */
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }}
        
        .stButton > button:hover {{
            background-color: #218838;  /* Darker Green */
        }}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏏 IPL Winner Probability Prediction")

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Teams and cities data
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# Input Section
st.markdown("### 🏟 Match Details")

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

city = st.selectbox('Select the host city', sorted(cities))
target = st.number_input('🎯 Target', min_value=1, step=1)

# Match Statistics
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('🏏 Score', min_value=0, step=1)
with col4:
    overs = st.number_input('⏳ Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('❌ Wickets Fallen', min_value=0, max_value=10, step=1)

# Prediction Button
if st.button('📊 Predict Probability'):
    if overs == 0:  # Avoid division by zero
        st.warning("Overs cannot be 0! Please enter a valid number of overs.")
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],
            'runs_left': [runs_left], 'balls_left': [balls_left], 'wicket': [wickets_left],
            'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]
        })

        result = model.predict_proba(input_df)

        win = result[0][1] * 100
        loss = result[0][0] * 100

        # Display Results
        st.subheader(f"🏏 **{batting_team} Winning Probability:** {round(win, 2)}%")
        st.subheader(f"🏏 **{bowling_team} Winning Probability:** {round(loss, 2)}%")
