from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    """Render the main HTML page."""
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_recipe():
    """Generate a recipe based on provided ingredients."""
    data = request.get_json()
    ingredients = data.get("ingredients", "")
    
    # Prepare the prompt for the Phi3.5 model
    prompt = f"Create a recipe using the following ingredients: {ingredients}."
    command = f"ollama run phi3.5 '{prompt}'"
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    recipe = result.stdout.strip()

    return jsonify({"recipe": recipe})

if __name__ == '__main__':
    app.run(debug=True)
