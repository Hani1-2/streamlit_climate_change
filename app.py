import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy 

# read csv
df = pd.read_csv('Temperature_change_Data.csv')
# Page setting
st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Row A
a1, a2, a3 = st.columns(3)
# a1.image(Image.open('pic2.png'), width=200)
a1.metric("Average Production", "Carbon dioxide (metric Ton)", "102.242 Ton")
a2.title('Climate Change Dashboard')
a3.metric("Average Change", "Temperature Change", "0.48% per year")

# Row B
plot = st.container()
plot2 = st.container()
c1, c2, c3 = st.columns((4,1,5))
with c1:
    st.subheader('Comparison of Temperature Change in Different Countries')
    st.text('*  Climate change is a change in the statistical distribution of weather patterns when that change lasts for an extended period of time (i.e., decades to millions of years).')


    # year_cross_tab_1 = pd.crosstab(data['sentiments'], data['issue'][:20])
    # print(year_cross_tab_1)
    comp_dist = df['Country Name'].str.strip("'").value_counts()[0:10]
    fig1 = {
        "data": [
    {
      "values": comp_dist.values,
      "labels": comp_dist.index
      ,
      "domain": {"column": 0},
      "name": "Temperature Change",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    ],
    "layout": {
        "title":"Contries with the most Temperature Change",
        "grid": {"rows": 1, "columns": 1},
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Temperature Change",
                "x": 0.5,
                "y": 0.5
            }
        ]
    }
}
    fig1 = go.Figure(data = fig1)
    st.write(fig1)

with c3:
    st.subheader('Temperature Change in Top 10 Countries ')
    st.markdown('We visualize the temperature change of top 10 countries')

    country_temp_change = {}
    uniquecountry = df["Country Name"].unique()
    for i in range(len(uniquecountry)):
        countrywiseDataset = df.groupby('Country Name')
        dataset1 = countrywiseDataset.get_group(uniquecountry[i])
        dataset1.sort_values(by=["tem_change"])

        dataset1 = dataset1[dataset1.tem_change == dataset1.tem_change.max()]
        country_name = numpy.array(dataset1['Country Name'])[0]
        temp_change = numpy.array(dataset1['tem_change'])[0]
        country_temp_change[country_name] = temp_change

    top_country_temp_change = sorted(country_temp_change.items(), key=lambda x: x[1], reverse=True)
    print('length of top_country_temp_change', len(top_country_temp_change))
    country_with_lowest_temp_change = sorted(country_temp_change.items(), key=lambda x: x[1], reverse=False)
        # print(len(top_country_temp_change))
    country = []
    temp = []
    for i in range(10):
            country.append(top_country_temp_change[i][0])
            temp.append(top_country_temp_change[i][1])
    print(country)
    print(temp)
    fig2 = px.bar(x=country, y=temp, color=temp, labels={'x':'Country', 'y':'Highest Temperature Change'})
    st.write(fig2)





# Row C
c6,c5, c4 = st.columns([4,1,4])
with c6:
    st.subheader('Lowest Temperature Change in Different Countries')
    st.markdown('We visualize the temperature change of different countries with slowest rate')
    country_1= []
    temp_1 = []
    for i in range(10):
            country_1.append(country_with_lowest_temp_change[i][0])
            temp_1.append(country_with_lowest_temp_change[i][1])
    print(country_1)
    print(temp_1)
    fig3 = px.bar(x=country_1, y=temp_1, color=temp, labels={'x':'Country', 'y':'Lowest Temperature Change'})
    st.write(fig3)


# Year wise temperature change
with c4:
    st.subheader('Year wise Temperature Change')
    st.markdown('We visualize the temperature change year wise in different countries')
    # ddatef. = pd.to_datetime(df.year, format='%Y')
    print(df.head())
    year = pd.unique(df.year)
    df1 = df.loc[df["Country Name"] == 'Albania']
    df2 = df.loc[df["Country Name"] == 'Greenland']
    df3 = df.loc[df["Country Name"] == 'Canada']
    df = pd.concat([df1,df2,df3])  
    fig4 = px.line(data_frame = df, x = 'year', y = 'tem_change', color=df['Country Name'] ,labels={'x':'Year', 'y':'Temperature Change'})
    st.write(fig4)

# Row D
d1,d3 , d2 = st.columns([4,1,4])
with d1:
    data = pd.read_csv('climate_change_dataset.csv')
    st.subheader('Year wise Production of Carbon dioxide (metric Ton)')
    st.markdown('We visualize the production of carbon change year wise in different countries')
    # ddatef. = pd.to_datetime(df.year, format='%Y')
    print(df.head())
    Year = pd.unique(data.Year)
    df1 = data.loc[data["Country Name"] == 'Albania']
    df2 = data.loc[data["Country Name"] == 'Greenland']
    df3 = data.loc[data["Country Name"] == 'Canada']
    df_2 = pd.concat([df1,df2,df3])  
    fig5 = px.line(data_frame = df_2, x = 'Year', y = 'Carbon dioxide (metric Ton)', color=df_2['Country Name'] ,labels={'x':'Year', 'y':'Carbon dioxide (metric Ton)'})
    st.write(fig5)


with d2:
    data = pd.read_csv('climate_change_dataset.csv')
    st.subheader('Year wise Production of GDP per capita (current US$)')
    st.markdown('We visualize the increase of GDP year wise in different countries')
    # ddatef. = pd.to_datetime(df.year, format='%Y')
    print(df.head())
    Year = pd.unique(data.Year)
    df1 = data.loc[data["Country Name"] == 'Albania']
    df2 = data.loc[data["Country Name"] == 'Greenland']
    df3 = data.loc[data["Country Name"] == 'Canada']
    df_3 = pd.concat([df1,df2,df3])  
    fig5 = px.line(data_frame = df_3, x = 'Year', y = 'GDP per capita (current US$)', color=df_3['Country Name'] ,labels={'x':'Year', 'y':'GDP per capita (current US$)'})
    st.write(fig5)
