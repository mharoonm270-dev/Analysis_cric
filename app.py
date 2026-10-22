import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

#st.page_config(layout="wide")
st.title("cricket Analysis Dashboard")


df=pd.read_csv("cleanedfile.csv")

select = option_menu(
    menu_title=None,
    options=["Home","Player analysis","Country insights","Comparison","Data explorer","About project"],

    orientation="horizontal",
    icons=["house","person","globe","bar-chart","table"] 

)
#this is home page
if select=="Home":
    st.title("Cric Analysis Intro.")

    col1,col2,col3,col4,col5=st.columns(5)
    col1.metric("Total Player",df["Player"].nunique())
    col2.metric("Total countries",df["country"].nunique())
   # col3.metric("Total Matches",df["Matches"].sum())
    col4.metric("Total runs",df["Runs"].sum())
    col5.metric("Total sixes",df["6s"].sum())

    st.dataframe(df.head(5))

#this is for player Analysis     
elif select=="Player Analysis":
    st.title("Cricket Player Analysis")

    Player = st.selectbox("select Player",df["Player"])

    pdata= df[df["Player"]==Player]

    df2=pdata[["Matches","Inns","6s","4s","100","50","Average"]]
    #st.datafram(df2)
    df2=df2.T.reset_index()
    st.datafram(df2)
    fig=px.bar(df2,x="index",y=df2.columns[1],color="index")

    st.plotly_chart(fig)

elif select=="Country Insights":
    
    
        st.title("Country Insights")
        country_runs=df.groupby("countrt")["Runs"].sum().reset_index()

        fig = px.pie(country_runs,names="country",values="Runs")
        st.plotly_chart(fig)
  
        st.title("country wise player insights")
        country_sel=st,selectbox("select country",df["country"].unique())
        c_df=df[df["country"]==countrt_sel]

    fig_run = px.pie(c_df,names="Player",values="Runs")
    st.plotly_chart(fig_run,use_container_width=True)


elif select=="Comparison":
    st.title("Player Comparison")

    Players=st.multiselect("compare Player",df["Player"])
    compare=df[df["Player"].isin(Players)]
    fig=px.scatter(compare,x="Strike_rate",y="Average",size="Runs",color="country")
    st.plotly_chart(fig)

elif select=="Data Explorer":
    st.title("Deta Explorer")

elif select=="About project":
    st.title("About project")          