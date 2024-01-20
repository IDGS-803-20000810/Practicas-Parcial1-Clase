
class Piramide:
    #declaracion de propiedades de clase
    niveles=0
        
    #declaracion de constructo
    def __init__(self,n):
        self.niveles=int(n)
    
    #declaracion de métodos de clase
    
    def printPiramide(self):
        
        for i in range(1,(self.niveles+1)):
            for j in range(i):
                print("*",end=" ")
            print("\n")
                
#Por indentacion se queda afuera de la clase
def main():
    n=input("Inserte un valor n: ")
    
    obj = Piramide(n)
    obj.printPiramide()
    
if __name__ == "__main__":
    main()
