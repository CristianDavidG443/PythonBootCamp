import pandas as pd 
df = pd.read_csv('cinema.csv')
#print(df)  # Mostrar las primeras filas del DataFrame
print(df['Age'])
Columnas_a_imprimir = ["Ticket_ID","Age","Ticket_Price"]  # Mostrar la columna 'Title'
df_selec = df[Columnas_a_imprimir]  # Seleccionar las columnas a imprimir
print(df_selec)