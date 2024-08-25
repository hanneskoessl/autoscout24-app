import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

def app():
    
    df = pd.read_csv('autoscout24.csv')
    df = df.drop_duplicates().reset_index()
    df = df.dropna()

    df = df.drop(["model", "gear", "offerType", "year"], axis=1)

    allowed_makes = df.make.value_counts()[0:10].index
    df = df[df['make'].isin(allowed_makes)]  

    df_dummies = pd.get_dummies(df, drop_first=True).drop("index", axis=1)
    
    X = df_dummies.drop('price', axis=1)
    y = df_dummies['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    rf = RandomForestRegressor(n_estimators=12, random_state=1) 
    rf.fit(X_train, y_train)
    
    y_pred = rf.predict(X_test) 
    score = r2_score(y_test.values, y_pred)
    mse = mean_squared_error(y_test.values, y_pred)

    mileage = st.number_input("Kilometerstand", min_value=0, value=70000)
    hp = st.number_input("Leistung in PS", min_value=0, value=116)
    make = st.selectbox('Welche Marke?', df.make.value_counts().index)
    fuel = st.selectbox('Welcher Treibstoff?', df.fuel.value_counts().index[0:4])
    
    new_data = {
        'mileage': mileage,
        'hp': hp,
        'make': make,
        'fuel': fuel,
    }
    
    st.write("Auswahl:")
    new_df = pd.DataFrame(new_data, index=[0])
    new_df_copy = new_df.copy() 
    st.dataframe(new_df_copy)
    
    new_dummies = pd.get_dummies(new_df)
    
    data_pred = pd.DataFrame(X_train[0:1]).reset_index(drop=True)
    
    for col in X_train.columns:
        if col not in new_dummies.columns:
            data_pred[0:1][col] = False
        else:
            data_pred.loc[0,col] = new_dummies[col][0]
    
    y_pred = rf.predict(data_pred) 
    st.write(f"Preisvorhersage: {round(y_pred[0])}€")
    st.write(f"R2-Score: {round(score,2)}")
    st.write(f"MSE: {round(mse)}")

 