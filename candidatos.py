import pandas as pd
import matplotlib.pyplot as plt


def recopilar_datos():
    
    datos = {
        'candidatos':['Claudia Sheibaum','Bertha Xochitl Gálvez', 'Jorge Álvarez Maynez'],
        'votos':[60,15,5]
    }
    #print(datos)
    #print("--------------------")
    df = pd.DataFrame(datos)
    #print(df)
    return df,datos 

def analisis_datos(df):
    #se realizan los métodos estadisticos para describir el comportamiento de tus datos
    print(df.describe())

def presentar_datos(df):
    x=df['candidatos']
    y=df['votos']
    print(x)
    print(y)
    plt.figure(figsize=(10,6))
    plt.bar(x,y, color='purple')
    plt.show()
      
     
    
if __name__ == '__main__':
    df,datos=recopilar_datos()
    #print(df)
    #print("-----")
    #print(datos)
    analisis_datos(df)
    presentar_datos(df)