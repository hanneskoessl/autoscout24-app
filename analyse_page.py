import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    df = pd.read_csv('autoscout24.csv')
    df = df.drop_duplicates().reset_index()

    st.header("Datenüberblick")

    df['year'] = df['year'].astype(str)
    cols = st.multiselect("Wähle die Spalten aus, die angezeigt werden sollen:", 
                          df.columns.tolist(), 
                          default=["mileage", "make", "model", "fuel", "gear", "offerType", "price", "hp", "year"]
                          )
    st.dataframe(df[cols])
    df['year'] = df['year'].astype(int)

    st.write(f"Anzahl der Autos: {df.shape[0]}")
    st.write(f"Zulassung ältestes Auto: {df.year.min()}")
    st.write(f"Zulassung neuestes Auto: {df.year.max()}")

    make_count = df.make.value_counts().reset_index()

    f = px.bar(make_count, 
               x='make', 
               y='count', 
               title="Häufigkeit der Automarken")
    f.update_yaxes(title="Automarke"); f.update_xaxes(title="Anzahl der Autos")
    st.plotly_chart(f)

    st.write(f"**Durchschnittlicher Preis der Autos der fünf häufigsten Hersteller:**")
    allowed_makes = df.make.value_counts()[0:5].index
    mean_price = df.groupby("make").price.mean().reset_index()
    mean_price['price'] = mean_price['price'].round(0).astype(int)
    mean_price = mean_price[mean_price["make"].isin(allowed_makes)]
    mean_price = mean_price.rename(columns={"make": "Marke", "price": "Durchschnittspreis"})

    mean_price['Durchschnittspreis'] = mean_price['Durchschnittspreis'].apply(lambda x: f"{x} €")

    st.markdown(mean_price.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    f = px.scatter(df, 
                   x='hp', 
                   y = 'price', 
                   title="Zusammenhang zwischen Preis und Leistung in verschiedenen Angebotskategorien", 
                   color="offerType", 
                   hover_name="make", 
                   hover_data={'model': True, 'fuel': True, 'gear': True, 'year': True})
    f.update_yaxes(title="Preis in €"); f.update_xaxes(title="Leistung in PS")
    st.plotly_chart(f)

    f = px.scatter(df, 
                   x='mileage', 
                   y = 'price', 
                   title="Zusammenhang zwischen Kilometerstand und Preis in verschiedenen Angebotskategorien", 
                   color="offerType", 
                   hover_name="make", 
                   hover_data={'model': True, 'fuel': True, 'gear': True, 'year': True})
    f.update_yaxes(title="Preis in €"); f.update_xaxes(title="Kilometerstand in km")
    st.plotly_chart(f)

    years = df['year'].unique()
    years.sort()
    tickvals = years

    f = px.box(df, 
               x='year', 
               y = 'price', 
               title="Zusammenhang zwischen Zulassungsjahr und Preis", 
               #color="offerType", 
               hover_name="make", 
               hover_data={'model': True, 'fuel': True, 'gear': True, 'year': True})
    f.update_yaxes(title="Preis in €"); f.update_xaxes(title="Zulassungsjahr")
    
    initial_x_range = [2010, 2022]
    initial_y_range = [0, 70000]  # Beispielwerte für den Bereich der y-Achse
 
    f.update_xaxes(tickvals=tickvals, range=initial_x_range, dtick=1)
    f.update_yaxes(range=initial_y_range)
    f.update_xaxes(range=initial_x_range)
    f.update_yaxes(range=initial_y_range)
    st.plotly_chart(f)

    f = px.box(df, 
               x='year', 
               y = 'mileage', 
               title="Zusammenhang zwischen Zulassungsjahr und Kilometerstand", 
               #color="offerType", 
               hover_name="make", 
               hover_data={'model': True, 'fuel': True, 'gear': True, 'year': True})
    f.update_yaxes(title="Kilometerstand in km"); f.update_xaxes(title="Zulassungsjahr")
    
    initial_x_range = [2010, 2022]
    initial_y_range = [0, 300000]  # Beispielwerte für den Bereich der y-Achse

    f.update_xaxes(tickvals=tickvals, range=initial_x_range, dtick=1)
    f.update_yaxes(range=initial_y_range)
    f.update_xaxes(range=initial_x_range)
    f.update_yaxes(range=initial_y_range)
    st.plotly_chart(f)

    f = px.box(df, 
               x='year', 
               y = 'hp', 
               title="Zusammenhang zwischen Zulassungsjahr und Leistung", 
               #color="offerType", 
               hover_name="make", 
               hover_data={'model': True, 'fuel': True, 'gear': True, 'year': True})
    f.update_yaxes(title="Leistung in PS"); f.update_xaxes(title="Zulassungsjahr")
    
    initial_x_range = [2010, 2022]
    initial_y_range = [0, 350]  # Beispielwerte für den Bereich der y-Achse

    
    f.update_xaxes(tickvals=tickvals, range=initial_x_range, dtick=1)
    f.update_yaxes(range=initial_y_range)
    f.update_xaxes(range=initial_x_range)
    f.update_yaxes(range=initial_y_range)
    st.plotly_chart(f)