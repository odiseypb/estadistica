def media(datos):
    #Suma todos los valores y se divide por la cantidad de valores
    poblacion = len(datos)
    suma_valor=0
    for valor in datos:
        suma_valor = suma_valor+valor
    #print(suma_valor)
    media = suma_valor/poblacion
    print(media)

def moda(datos):
    #valor que más se repite
     cantidadVecesAparece = lista.count(numero)
    if cantidadVecesAparece > variableCantidad :
        variableCantidad = cantidadVecesAparece
        variableModa = numero
    val_repite=datos[0]
    num_veces_valor = datos.count(valor)
 
    for valor in datos:
               
        if num_veces_valor > val_repite:
            val_repite = valor
    print(f"La moda es {val_repite}")
            
if __name__== '__main__':
    datos = [3,7,5,9,1,4,8,6,3,10]
    media(datos)
    moda(datos)
    
    
    
    