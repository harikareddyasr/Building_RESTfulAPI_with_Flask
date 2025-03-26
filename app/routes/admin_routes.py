from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models import User, Item
from flask_jwt_extended import create_access_token, jwt_required
import os

admin = Blueprint('admin', __name__)

@admin.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered'}), 201

@admin.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.username)
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@admin.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    return jsonify({'message': 'Welcome Admin'}), 200

@admin.route('/item', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    item = Item(name=data['name'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item created'}), 201

@admin.route('/item/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)
    item.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Item updated'}), 200

@admin.route('/item/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'}), 200

@admin.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if allowed_file(file.filename):
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded'}), 201
    return jsonify({'error': 'Invalid file type'}), 400

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'pdf'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
