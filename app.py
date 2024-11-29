
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de Excel
df = pd.read_excel('nombre_de_tu_archivo.xlsx')

# Descripción del proyecto
st.title('Análisis de Países')
st.write('Este proyecto utiliza datos de países de un archivo Excel.')

# Mostrar datos
if st.checkbox('Mostrar Datos'):
    st.write(df)

# Estadísticas
st.write('Estadísticas Descriptivas:')
st.write(df.describe())

# Filtrar por Región
region = st.selectbox('Selecciona la Región', df['Region_geografica'].unique())
df_filtrado = df[df['Region_geografica'] == region]
st.write(df_filtrado)

# Crear gráfico interactivo
st.subheader('Gráfico de Países Más Poblados')
df_ordenado = df.sort_values(by='Poblacion_total', ascending=False).head(10)
fig, ax = plt.subplots()
ax.bar(df_ordenado['nombre_pais'], df_ordenado['Poblacion_total'])
plt.xticks(rotation=45)
plt.xlabel('País')
plt.ylabel('Población Total')
plt.title('Top 10 Países Más Poblados')
st.pyplot(fig)

# Crear archivo descargable
st.download_button(label="Descargar Datos Filtrados", data=df_filtrado.to_csv(index=False), file_name='datos_filtrados.csv', mime='text/csv')
