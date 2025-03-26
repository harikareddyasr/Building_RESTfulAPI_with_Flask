from flask import Blueprint, jsonify
from app.models import Item

public = Blueprint('public', __name__)

@public.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])
