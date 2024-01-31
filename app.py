"""Flask app for Cupcakes"""
from models import db, connect_db, Cupcake
from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_test'
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)


def serialize_cupcake(cupcake):
    return ({'id': cupcake.id,
             'flavor': cupcake.flavor,
             'size': cupcake.size,
             'rating': cupcake.rating,
             'image': cupcake.image})


@app.route('/')
def home_page():
    return render_template('home.html/')


@app.route('/api/cupcakes')
def api_list_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcake_list = [serialize_cupcake(cupcake) for cupcake in cupcakes]
    return jsonify({'cupcakes': cupcake_list})


@app.route('/api/cupcakes', methods=["POST"])
def api_make_cupcake():
    cupcake = Cupcake()
    print('request.json: ', request.json)
    print('flavor: ', request.json['flavor'])
    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    if ('image' in request.json):
        cupcake.image = request.json['image']
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify({'cupcake': serialize_cupcake(cupcake)}), 201)


@app.route('/api/cupcakes/<int:id>')
def api_get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify({'cupcake': serialize_cupcake(cupcake)})


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def api_patch_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    cupcake.image = request.json['image']
    db.session.add(cupcake)
    db.session.commit()
    return jsonify({'cupcake': serialize_cupcake(cupcake)})


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def api_remove_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    print('here I am in delete')
    print('deleting ', cupcake.flavor, ' cupcake')
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({'message': "Deleted"})
