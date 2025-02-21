from flask import Blueprint, request, jsonify, render_template
import random

travel_routes = Blueprint('travel_routes', __name__)

def check_pantry_availability(train_number):
    return random.choice([True, False])  

@travel_routes.route('/traveller', methods=['GET'])
def traveller():
    return render_template('traveller.html')

@travel_routes.route('/coach_position', methods=['GET', 'POST'])
def coach_position():
    if request.method == 'GET': 
        return render_template('coach_position.html')
    data = request.form if request.method == 'POST' else request.args
    train_number = data.get('train_number', "12345")
    coach_id = data.get('coach_id', "1")

    if not train_number or not coach_id:
        return jsonify({"error": "Missing train number or coach ID"}), 400

    position = int(coach_id) * 5  # Simplified logic for minimal setup
    return jsonify({
        "train_number": train_number,
        "coach_id": coach_id,
        "predicted_position": f"Near Pillar {position}"
    })

@travel_routes.route('/food_avaliability', methods=['GET', 'POST'])
def food_availability():
    if request.method == 'GET': 
        return render_template('food_avaliability.html')
    data = request.form if request.method == 'POST' else request.args
    train_number = data.get('train_number', "12345")
    if not train_number:
        return jsonify({"error": "Train number is required"}), 400

    pantry_available = check_pantry_availability(train_number)
    return jsonify({"message": "Pantry car is available." if pantry_available else "No pantry car. Check nearby shops."})
