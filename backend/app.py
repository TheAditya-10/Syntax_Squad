import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # type: ignore
from models.database import db

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend")
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Adi!1%40T@localhost/syntax_squad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

from routes.guide import info_routes  
app.register_blueprint(info_routes)  
from routes.plan import plan_routes
app.register_blueprint(plan_routes)
from routes.travel import travel_routes
app.register_blueprint(travel_routes)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)