from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "sh897terdw4we688"

@app.route('/')         
def datos_sesion():    
    if "visit" not in session:
        session['visit'] = 0
        print("La llave 'key_name' NO existe ")
    else:
        session['visit'] += 1
        print("La llave existe!")
    return render_template("index.html")


@app.route('/destroy_session', methods = ['GET', 'POST'])
def destroy_cache():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('reset') == 'Reset':
            #session.clear()
            print("Se ha limpiado la cache")
            session.pop('visit', None)
        elif request.form.get('add_two_more') == 'Add two visits!':
            session["visit"] += 1
            print("Se han añadido 2 visitas más desde el boton")
        else:
            pass
    elif request.method == 'GET':
        print("¡No post call back!")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)    
