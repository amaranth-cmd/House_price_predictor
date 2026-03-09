# House_price_predictor
This is a repository containing files on a LinearRegression model trained on housing prices to predict price of houses depending on certain features. There's also a streamlit app enclosed, which when it's link is used will require characteristics of the house in question to give predictions. 

Found at this link:
https://housepricepredictor-qrox3hjclx6wcph8ppyy8j.streamlit.app/

# DATA SET USED
The data data set used is a Housing.csv included in the repository. 

# EDA Workflow
The EDA went through the usual steps such as viewing the data through .info(), which tells us things like data types, missing values if any how many, so as to know what steps of feature engineering to take which was the next step. 
Then the choosing of the model, training, predictions then evaluation. 

# Model Saving
joblib wa used as the library for this.

# Folder make up
housing_project/
│
├── housing_model.pkl
├── app.py
├── housing.csv
├── requirements.txt
└── README.md

every step led to having the files shown above. Including the web app to be launched through streamlit.

# Author
Amaranth Madise
