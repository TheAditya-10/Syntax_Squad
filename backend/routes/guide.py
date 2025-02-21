from flask import Blueprint, request, jsonify, render_template
from PIL import Image
import base64
from io import BytesIO
import google.generativeai as genai
import markdown # type: ignore

info_routes = Blueprint("info_routes", __name__)
genai.configure(api_key="AIzaSyAw1LA3YKWq3004W7yL8VukAChUdoq-OMo")
model = genai.GenerativeModel("gemini-1.5-flash")

@info_routes.route('/guider', methods=['GET', 'POST'])
def get_info():
    if request.method == 'GET':
        return render_template("guider.html")  
    data = request.json
    place_name = data.get("place")

    if not place_name:
        return jsonify({"error": "Place name is required"}), 400

    # AI-Powered Response
    try:
        prompt = f"Provide a concise summary (3-4 sentences) of the historical facts, fun facts, significance, and importance of {place_name}. Keep the response under 100 words. Do not include any unnecessary details."
        raw_response = model.generate_content(prompt).text
        response = markdown.markdown(raw_response)
    except Exception as e:
        return jsonify({"error": f"Gemini API Error: {str(e)}"}), 500

    return jsonify({"info": response})

# Handle image-based queries
@info_routes.route('/get_info_from_image', methods=['POST'])
def get_info_from_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = request.files['image']
    img = Image.open(image)
    
    # Convert Image to Base64
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # AI-Powered Image Analysis
    response = model.generate_content(["Describe the historical and cultural significance of the monument in this image in 3-4 sentences. Do not include any unnecessary details.", img_base64]).text

    return jsonify({"info": response})
