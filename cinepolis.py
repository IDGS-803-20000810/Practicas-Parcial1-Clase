from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/cinepolis")
def index():
    return render_template("cinepolis.html",nombre="",pagar=0,valido=True)

@app.route("/procesar",methods=["GET","POST"])
def resOpBas():
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



if __name__=="__main__":
    app.run(debug=True)