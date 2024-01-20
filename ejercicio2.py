
class ListaNumeros:
    #declaracion de propiedades de clase
    numero=0
    lista=[]
        
    #declaracion de constructo
    def __init__(self,n):
        self.numero=int(n)
    
    #declaracion de métodos de clase
    
    def cargarNumeros(self):
        for i in range(1,(self.numero+1)):
            num = int(input("Selecciona el numero en la posicion {}:".format(i)))
            self.lista.append(num)
            
    def printEstadisticas(self):
        pares = []
        impares = []
        repetidos = {}
        self.lista.sort()
        
        for num in self.lista:
            if num%2 == 0:
                pares.append(num)
            else:
                impares.append(num)
            
        for num in self.lista:
            if num in repetidos:
                repetidos[num] += 1
            else:
                repetidos[num] = 1
                
        print("*******RESULTADOS*******")
        print("Lista ordenada : {} ".format(self.lista))        
        print("Numeros pares: {}".format(pares))
        print("Numeros impares: {}".format(impares))
        print("Repetidos: ")
        for key in repetidos.keys():
            if repetidos[key] > 1:
                print("- El numero {} se repite {} veces".format(key,repetidos[key]))

#Por indentacion se queda afuera de la clase
def main():
    n=input("Cuantos numeros quieres insertar?: ")
    
    obj = ListaNumeros(n)
    obj.cargarNumeros()
    obj.printEstadisticas()
    
if __name__ == "__main__":
    main()
