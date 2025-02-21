import os
from flask import request, jsonify, Blueprint, render_template
from models.database import db, TravelHistory
from datetime import datetime
import google.generativeai as genai

# Configure Gemini AI model
genai.configure(api_key="AIzaSyAw1LA3YKWq3004W7yL8VukAChUdoq-OMo")
model = genai.GenerativeModel("gemini-1.5-flash")

plan_routes = Blueprint("plan_routes", __name__)

@plan_routes.route("/planner", methods=["GET", "POST"])
def plan_trip():
    """Generate a list of budget-friendly travel destinations based on user input."""
    if request.method == 'GET':
        return render_template("planner.html")
    data = request.json
    days = data.get("days")
    mood = data.get("mood")
    budget = data.get("budget")

    if not days or not mood or not budget:
        return jsonify({"error": "All fields are required"}), 400

    prompt = (
        f"Suggest 4-5 budget-friendly travel destinations in India "
        f"for a {mood} trip within {budget} INR for {days} days. "
        "Provide only: Place Name, City, Average Budget (INR). Do not incluce any unnecessary details."
    )
    
    response = model.generate_content(prompt)
    suggested_places = response.text if response.text else "No recommendations available."

    return jsonify({"suggested_places": suggested_places})


@plan_routes.route("/generate_trip_plan", methods=["POST"])
def generate_trip_plan():
    """Generate a detailed trip itinerary for the selected place."""
    data = request.json
    selected_place = data.get("selected_place")

    if not selected_place:
        return jsonify({"error": "Please select a destination"}), 400

    prompt = (
        f"Create a detailed but to the point travel plan for {selected_place}. "
        "Include:\n"
        "- Food suggestions (4-5 items)\n"
        "- A full-day itinerary for each day (activities, best timings)\n"
        "- Hotels/dormitories (budget-friendly)\n"
        "- Local travel options (bus, auto, rental)\n"
        "- Top vlogs (3 links) with spoiler warning."
        "Do not include any unnecessary details."
    )

    response = model.generate_content(prompt)
    
    trip_plan = response.text if response.text else "Trip plan could not be generated."

    return jsonify({"trip_plan": trip_plan})


@plan_routes.route("/confirm_trip", methods=["POST"])
def confirm_trip():
    """Save confirmed trip details in the database."""
    data = request.json
    email = data.get("email")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    place_visited = data.get("place_visited")
    budget_per_person = data.get("budget_per_person")
    companions = data.get("companions")

    if not all([email, start_date, end_date, place_visited, budget_per_person]):
        return jsonify({"error": "Missing required fields"}), 400

    # Convert string dates to Python date objects
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    # Store in database
    new_trip = TravelHistory(
        email=email,
        start_date=start_date,
        end_date=end_date,
        place_visited=place_visited,
        budget_per_person=budget_per_person,
        companions=companions
    )
    
    db.session.add(new_trip)
    db.session.commit()
    
    return jsonify({"message": "Trip confirmed successfully!"}), 200


@plan_routes.route("/trip_history", methods=["GET"])
def trip_history():
    """Retrieve past trip details from the database."""
    trips = TravelHistory.query.all()
    trip_data = [
        {
            "email": trip.email,
            "start_date": trip.start_date.strftime("%Y-%m-%d"),
            "end_date": trip.end_date.strftime("%Y-%m-%d"),
            "place_visited": trip.place_visited,
            "budget_per_person": trip.budget_per_person,
            "companions": trip.companions
        }
        for trip in trips
    ]
    return jsonify({"trip_history": trip_data})


@plan_routes.route("/view_trip/<int:trip_id>", methods=["GET"])
def view_trip(trip_id):
    """Fetch and display details of a specific trip."""
    trip = TravelHistory.query.get(trip_id)
    if not trip:
        return jsonify({"error": "Trip not found"}), 404

    trip_data = {
        "email": trip.email,
        "start_date": trip.start_date.strftime("%Y-%m-%d"),
        "end_date": trip.end_date.strftime("%Y-%m-%d"),
        "place_visited": trip.place_visited,
        "budget_per_person": trip.budget_per_person,
        "companions": trip.companions
    }
    
    return render_template("trip_details.html", trip=trip_data)


@plan_routes.route("/cancel_trip/<int:trip_id>", methods=["DELETE"])
def cancel_trip(trip_id):
    """Delete a trip from the database."""
    trip = TravelHistory.query.get(trip_id)
    if not trip:
        return jsonify({"error": "Trip not found"}), 404

    db.session.delete(trip)
    db.session.commit()

    return jsonify({"message": "Trip canceled successfully!"}), 200
