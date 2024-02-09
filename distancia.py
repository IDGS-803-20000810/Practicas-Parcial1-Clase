from flask import Flask, request, render_template
import formDistancia
import math 
app=Flask(__name__)

@app.route("/distancia",methods=["GET","POST"])
def distancia():
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

if __name__=="__main__":
    app.run(debug=True)