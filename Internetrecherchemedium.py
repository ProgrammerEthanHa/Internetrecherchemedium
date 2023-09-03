import streamlit as st
import pandas as pd
import altair as alt

st.header("Internet ist Recherche-Medium Nummer 1")
st.subheader("Wer sich über ein Thema näher informieren möchte, sucht bzw. achtet auf Berichte/liest Berichte - Internet")

source = pd.DataFrame({
        'Anteil (%)': [37, 55, 64],
        'Jahr': ['2004', '2009', '2014']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Jahr:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Ab 14 Jahre; Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: IfD Allensbach")