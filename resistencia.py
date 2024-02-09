from flask import Flask,request,render_template
import math
import formResistencia

app=Flask(__name__)

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

