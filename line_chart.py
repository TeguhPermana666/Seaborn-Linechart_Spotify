#setup the notebook
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load data
file_name="Visualisasi_data\spotify.csv"
data_spotify=pd.read_csv(file_name,index_col='Date',parse_dates=True)
print(data_spotify.head())

# Set the width and height of the figure
plt.figure(figsize=(14,6))#width and height

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

#plot data
v_data=sns.lineplot(data=data_spotify)
#sns_lineplot()=>digunakan untuk membuat sebuah chart(line chart)
#data=data_spotify=>data yang digunakan utnuk melakukan sebuah visualisasi data.
plt.show()

#plot data berdasarkan subnet column tertentu
print(list(data_spotify.columns))

plt.figure(figsize=(14,6))
#plot data column Despacito
v_column_data=sns.lineplot(data=data_spotify['Despacito'],label='Despacito')
#plot data Shape of You
v_column_data=sns.lineplot(data=data_spotify['Shape of You'],label='Shape of You')
plt.xlabel('Date')
plt.ylabel('Streamed')
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
plt.show()