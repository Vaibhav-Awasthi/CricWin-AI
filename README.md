# CricWin-AI : IPL Winning Team Prediction using Machine Learning

## Overview
This project predicts the probability of an IPL team winning a match based on real match data from **2009 to 2019**. The dataset is sourced from **Kaggle** and has been fine-tuned using machine learning algorithms to achieve an **accuracy above 90%**. The project features a **Streamlit-based web application** for interactive predictions.

## Features
- **High Accuracy**: The model is trained and fine-tuned for over **90% accuracy**.
- **User-Friendly Web App**: Built with **Streamlit** for easy user interaction.
- **Real IPL Data**: Uses **official IPL match data (2009-2019)**.
- **Probability Prediction**: Provides a **winning probability** for both teams.
- **Fully Automated Pipeline**: Preprocessing, training, and prediction handled efficiently.

## Technologies Used
- **Python** 🐍
- **Scikit-learn** (ML Model)
- **Pandas & NumPy** (Data Processing)
- **Streamlit** (Web Deployment)
- **Pickle** (Model Serialization)

## Installation Guide
### 1 Clone the Repository
```bash
git clone https://github.com/Vaibhav-Awasthi/CricWin-AI.git
cd CricWin-AI
```
### 2 Create a Virtual Environment
```
python -m venv venv
```
### 3 Activate the virtual environment:
```
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
```
### 4 Install Dependencies
```
pip install -r requirements.txt
```
### 5 Run the Web Application
```
streamlit run app.py
```

## Dataset

- **The dataset contains IPL match data from 2009 to 2019.**

- **Includes match details like teams, venue, target, score, wickets, and overs.**

- **Preprocessed and fine-tuned to remove inconsistencies.**

## Model Details

- **Uses OneHot Encoding for categorical variables.**

- **Features Logistic Regression and other fine-tuned ML models.**

- **Achieves 90%+ accuracy using hyperparameter tuning.**

 ## Contributing

- **Feel free to fork this repository, create a new branch, and submit a pull request if you have suggestions for improvement!**




