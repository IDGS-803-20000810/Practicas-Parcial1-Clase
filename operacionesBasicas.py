from flask import Flask, request, render_template

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



if __name__=="__main__":
    app.run(debug=True)