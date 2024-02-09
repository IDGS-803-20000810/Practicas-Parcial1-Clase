from flask import Flask, request, render_template
import formDistancia
import formResistencia
import math 


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/formOpBas")
def formOpBas():
    return render_template("formularioOpBas.html")

@app.route("/resOpBas",methods=["GET","POST"])
def resOpBas():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion=request.form.get("radioOp")
        
        if str(operacion)=="Suma":
            res = int(num1)+int(num2)
        elif str(operacion)=="Resta":
            res = int(num1)-int(num2)
        elif str(operacion)=="Multiplicacion":
            res = int(num1)*int(num2)
        elif str(operacion)=="Division":
            res = int(num1)/int(num2)
            
        return "<h1>El resultado es {}</h1>".format(str(res))
        
    return 

@app.route("/distancia",methods=["GET","POST"])
def calculaar():
    dist_form = formDistancia.DistanciaForm(request.form)    
    distancia = ""
    
    if request.method == "POST":
        x1=int(dist_form.x1.data)
        x2=int(dist_form.x2.data)
        y1=int(dist_form.y1.data)
        y2=int(dist_form.y2.data)

        predist = (x2-x1)**2 + (y2-y1)**2
        
        distancia = math.sqrt(predist) 
    
        
    return render_template("distancia.html",form=dist_form,distancia=distancia)
    
@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html",nombre="",pagar=0,valido=True)

@app.route("/procesar",methods=["GET","POST"])
def procesar():
    if request.method == "POST":
        
        nom=request.form.get("nombre")
        cantComp=int(request.form.get("cantComp"))
        tarjeta=request.form.get("tarjeta")
        cantBol=int(request.form.get("cantBol"))
        valido = True
        
        pagar = 12.0 * cantBol
        
        if cantComp>5:
            pagar = pagar*0.75
        elif (cantComp<=5) and (cantComp>=3):
            pagar = pagar*0.90
            
        if tarjeta == "Si":
            parar = pagar*0.90
        
        if cantBol > cantComp * 7:
            valido = False
        
        return render_template("cinepolis.html",nombre=nom,pagar=pagar,valido=valido)
        
    return 

@app.route("/resistencia",methods=["GET","POST"])
def res():

    colores = {
        0: 'Negro',
        1: 'Cafe',
        2: 'Rojo',
        3: 'Naranja',
        4: 'Amarillo',
        5: 'Verde', 
        6: 'Azul',
        7: 'Violeta',
        8: 'Gris',
        9: 'Blanco',
    }
    
    nombre1 = ""
    nombre2 = ""
    nombre3 = ""
    tolerancia = 0
    resistencia = 0
    maxRes = 0
    minRes = 0
    
    resistencia_form = formResistencia.FormResistencia(request.form)
    
    if request.method == 'POST':
        color1 = int(resistencia_form.color1.data)
        color2 = int(resistencia_form.color2.data)
        color3 = int(resistencia_form.color3.data)
        
        tolerancia = int(resistencia_form.tolerancia.data)
        
        nombre1 = colores[color1]
        nombre2 = colores[color2]
        nombre3 = colores[color3]
        
        valor = str(color1) + str(color2)
        resistencia = int(valor)
        
        multiplicador = int(color3)
        
        if multiplicador!=0:
            for i in range(0,(multiplicador)):
                resistencia = resistencia*10
                
        Ptolerancia = resistencia * (tolerancia / 100)
        maxRes = resistencia - Ptolerancia
        minRes = resistencia + Ptolerancia

    return render_template("resistencia.html", form=resistencia_form, color1=nombre1, color2=nombre2, color3=nombre3, tolerancia=tolerancia, resistencia=resistencia , maxRes=maxRes,minRes=minRes)



if __name__=="__main__":
    app.run(debug=True)