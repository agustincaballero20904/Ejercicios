from flask import Flask, redirect, render_template, request, url_for, session
import datetime
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config.from_pyfile("config.py")

from models import db
from models import Productos, ItemsPedidos, Pedidos, Usuarios

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            return redirect(url_for('Menu'))
        else:
            return redirect(url_for('VerPedidos'))
    else:
        if request.method == 'POST':
            if request.form['DNI'] and request.form['Contrasenia']:
                error = None
                dni = request.form['DNI']
                usuario_actual = Usuarios.query.filter_by(DNI=dni).first()
                if usuario_actual == None:
                    return render_template('error.html', error='DNI o Contraseña invalida')
                else:
                    if(hashlib.md5(bytes(request.form['Contrasenia'], encoding='utf-8')).hexdigest() == usuario_actual.Clave):
                        session['DNI'] = usuario_actual.DNI
                        session['Tipo'] = usuario_actual.Tipo
                        if usuario_actual.Tipo == 'Mozo':
                            return redirect(url_for('Menu'))
                        else:
                            return redirect(url_for('VerPedidos'))
                    else:
                        return render_template('error.html', error='DNI o Contraseña invalida')
        else:
            return render_template('login.html')

@app.route("/Menu")
def Menu():
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            return render_template('Menu.html')
        else:
            return redirect(url_for('VerPedidos'))
    else:
        return render_template('Error.html', error='No se inicio sesión')


@app.route("/Registropedidos", methods=['POST', 'GET'])
def Registropedidos():
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            if request.method == 'POST':
                valores = list(dict(request.form).keys())
                if 'NumPedido' in valores:
                    pedido = Pedidos.query.filter_by(NumPedido=request.form['NumPedido']).first()
                    if request.form['Observaciones'] != pedido.Observacion:
                        pedido.Observacion = request.form['Observaciones']
                if 'Mesa' in valores:
                    nummesa = int(request.form['Mesa'])
                    pedido = Pedidos(Fecha=datetime.date.today(), Total=0.0, Cobrado=False, Observacion='', DNIMozo=session.get('DNI'), Mesa=nummesa)
                    db.session.add(pedido)
                    db.session.commit()
                    return render_template('registropedido.html', products=Productos.query.all(),Pedido=pedido)
                elif 'Finalizar' in valores:
                    items = list(pedido.Item)
                    if len(items) == 0:
                        return render_template('registropedido.html', products=Productos.query.all(),Pedido=pedido,error='No se selecciono ningun elemento de la lista')
                    else:
                        return redirect(url_for('Menu'))
                else:
                    numprod = valores[1]
                    prod = Productos.query.filter_by(NumProducto=numprod).first()
                    item = ItemsPedidos(NumPedido=pedido.NumPedido, NumProducto=prod.NumProducto, Precio=prod.PrecioUnitario,
                            Estado='Pendiente')
                    pedido.Total += int(prod.PrecioUnitario)
                    db.session.add(item)
                    db.session.commit()
                    return render_template('registropedido.html', products=Productos.query.all(),Pedido=pedido)
            else:
                return render_template('registropedido.html', Mesaoc=True)
        else:
            return redirect(url_for('VerPedidos'))
    else:
        return render_template('Error.html', error='No se inicio sesión')



@app.route("/VerPedidos")
def VerPedidos():
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            Fecha = datetime.date.today()
            pedidos = Pedidos.query.filter_by(Fecha=Fecha, Cobrado=0).all()
            return render_template('pedidovig.html', pedidos=pedidos, productos = Productos.query.all())
        else:
            pedidos = Pedidos.query.all()
            pendientes = []
            for pedido in pedidos:
                i = 0
                band = False
                items = ItemsPedidos.query.filter_by(NumPedido=pedido.NumPedido).all()
                long = len(items)
                while i < long and not band:
                    if items[i].Estado == "Pendiente":
                        band = True
                        pendientes.append(pedido)
                    i += 1
            return render_template('pedidopend.html',pedidos=pendientes, productos = Productos.query.all())
    else:
        return render_template('Error.html', error='No se inicio sesión')


@app.route("/CobrarPedido/<int:pedido>", methods=['POST', 'GET'])
def CobrarPedido(pedido):
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            pedido = Pedidos.query.filter_by(NumPedido=pedido).first()
            if pedido is None:
                return redirect(url_for('VerPedidos'))
            else:
                if request.method == 'POST':
                    pedido.Cobrado = True
                    db.session.commit()
                    return redirect(url_for('VerPedidos'))
                else:
                    return render_template('cobrarpedido.html', pedido=pedido, productos = Productos.query.all())
        else:
            return redirect(url_for('VerPedidos'))
    else:
        return render_template('Error.html', error='No se inicio sesión')


@app.route("/Listo/<int:pedido>/<int:item>", methods=['POST', 'GET'])
def Listo(pedido, item):
    if 'DNI' in session:
        if session.get('Tipo') == 'Mozo':
            return render_template('Menu.html')
        else:
            itembusc = ItemsPedidos.query.filter_by(NumItem=item).first()
            if request.method == 'POST':
                itembusc.Estado = "Listo"
                db.session.commit()
                return redirect(url_for('VerPedidos'))
            else:
                prods = Productos.query.all()
                return render_template('Marcar.html', pedido=pedido, productos=prods[itembusc.NumProducto-1])
    else:
        return render_template('Error.html', error='No se inicio sesión')

@app.route("/Cerrarsesion")
def Cerrarsesion():
    if 'DNI' in session:
        session.pop('DNI')
        session.pop('Tipo')
        return redirect(url_for('inicio'))
    else:
        return render_template("Error.html", error="No se inicio sesión.")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
