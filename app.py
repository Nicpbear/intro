import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo reaizar backend y frontend")
image = Image.open("cr7.jpeg")

st.image(image, caption="Interfaces multimodales")


texto ) st.text_input("Oe")
st.write("Que más")

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva","Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditivo":
    st.write("La audición es fundamental para tu interfaz")
