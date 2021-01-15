from flask import Flask, render_template, request, url_for, redirect, session, flash, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
#from flask_cors import CORS
from models import *
#from config import *
app=Flask(__name__)
# app.config.from_object(config)
#db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\user\\anaconda3\\envs\\dataweb.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def inicio():
    return render_template('principal.html')

@app.route('/vista_prin')
def vista_prin():
    return render_template('principal.html')

@app.route('/form_part')
def form_part():
    eventos=evento.query.all()
    return render_template('inscripcion.html',eventos=eventos)

@app.route('/add_inscripcion',methods=['POST','GET'])
def add_inscripcion():
    if(request.method=='POST'):
        lista=request.form
        dato = participante(dni=lista['DNI'],nombre=lista['name'],apellido_p=lista['Ap'],
            apellido_m=lista['Am'],categoria=lista['op'],email=lista['email'],evento=lista['evento_id'])
        db.session.add(dato)
        db.session.commit()
    return render_template('principal.html')


#login
@app.route('/admi_login')
def admi_login():
    return render_template('logout.html')

@app.route('/ventana_admin',methods=['POST','GET'])
def ventana_admin():
    if(request.method=='GET'):
        return render_template("login.html")
    if(request.method=='POST' and request.form):
        username=request.form['username']
        password=request.form['password']
        dato = User(username=username,password=password)
        db.session.add(dato)
        db.session.commit()
        return render_template("login.html")
    return "ya no"
#usuario
@app.route('/administrador', methods=['POST','GET'])
def administrador():
    if(request.method=='POST'):
        data_ing=request.form
        if(User.query.filter_by(username=data_ing['username'],password=data_ing['password']).all()):
            eventos=evento.query.all()
            nombre="Todos los Eventos"
            return render_template('ventanadmin.html', eventos=eventos,nombre=nombre)
        else:
            return render_template("login.html")
    else:
        return"no puede acceder"
@app.route('/add_evento', methods=['POST','GET'])
def add_evento():
    if(request.method=='POST' and request.form):
        nom=request.form['name']
        ub=request.form['ubicacion']
        fec=request.form['fecha']
        h=request.form['hora']
        mon=float(request.form['monto'])
        data=evento(nombre=nom,ubicacion=ub,fecha=fec,hora=h,monto=mon)
        db.session.add(data)
        db.session.commit()
    eventos=evento.query.all()
    return render_template('ventanadmin.html', eventos=eventos)

@app.route('/editar_evento/<id>',methods = ['POST', 'GET'])
def editar_evento(id):
    event = evento.query.get(int(id))
    if event is None:
        return '<h1>no existe error!</h1>'
    e=request.form
    act_data=evento.query.get(id)
    act_data.nombre=e['name']
    act_data.ubicacion=e['ubicacion']
    act_data.fecha=e['fecha']
    act_data.hora=e['hora']
    act_data.monto=e['monto']
    db.session.commit()
    eventos=evento.query.all()
    return render_template('ventanadmin.html', eventos=eventos)
@app.route('/delete_event/<id>', methods=['POST','GET'])
def delete_event(id):
    e = evento.query.get(int(id))
    db.session.delete(e) 
    db.session.commit()
    eventos=evento.query.all()
    return render_template('ventanadmin.html', eventos=eventos)
@app.route('/search_name',methods=['POST','GET'])
def search_name():
    name=request.form.get('nombre')
    eventos=evento.query.filter_by(nombre=name).all()
    return render_template('ventanadmin.html', eventos=eventos)

@app.route('/search_fecha',methods=['POST','GET'])
def search_fecha():
    fecha=request.form.get('fecha')
    eventos=evento.query.filter_by(fecha=fecha).all()
    return render_template('ventanadmin.html', eventos=eventos)

@app.route('/search_ubicacion',methods=['POST','GET'])
def search_ubicacion():
    ubicacion=request.form.get('lugar')
    eventos=evento.query.filter_by(ubicacion=ubicacion).all()
    return render_template('ventanadmin.html', eventos=eventos)

@app.route('/search_prt_evnt',methods=['POST','GET'])
def search_prt_evnt():
    id_e=request.form.get("id")
    part=participante.query.filter_by(evento=int(id_e)).all()
    cantidad=participante.query.filter_by(evento=int(id_e)).count()
    return render_template('ver_inscritos.html',part=part,id_e=id_e,cantidad=cantidad)

@app.route('/views_categoria',methods=['POST','GET'])
def views_categoria():
    id_e=request.form.get('ide')
    part=participante.query.filter_by(evento=int(id_e)).all()
    total=participante.query.filter_by(evento=int(id_e)).count()
    can1=participante.query.filter_by(categoria='Estudiante',evento=int(id_e)).count()
    can2=participante.query.filter_by(categoria='Profesional',evento=int(id_e)).count()
    can3=participante.query.filter_by(categoria='Colaborador',evento=int(id_e)).count()
    evento.query.with_entities(func.sum(evento.monto).label('monto')).filter(evento.id ==int(id_e))
    return render_template('categoria.html',part=part,id_e=id_e,total=total,can1=can1,can2=can2,can3=can3)

#views
@app.route('/aniadir_evento')
def aniadir_evento():
    return render_template('añadir_evento.html')
@app.route('/go_edit_event/<id>')
def go_edit_event(id):
    data=evento.query.get(int(id))
    return render_template('editar_evento.html',data=data)

@app.route('/mostrar_evento')
def mostrar_evento():
    eventos=evento.query.all()
    return render_template('ventanadmin.html', eventos=eventos)

@app.route('/mostrar_participantes')
def mostrar_participantes():
    part=participante.query.all()
    return render_template('participantes.html',part=part)

@app.route('/vista_contact')
def vista_contact():
    return render_template("contacto.html")

@app.route('/vista_info')
def vista_info():
    return render_template("info.html")

@app.route('/volver', methods=['POST','GET'])
def volver():
    return render_template("ventanadmin.html")



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)