from flask import Flask, render_template_string, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sample data for plants and their sunlight needs
plants_data = {
    'Snake Plant': {'sunlight': 'Low to Medium', 'description': 'Thrives in indirect sunlight and is very low-maintenance.'},
    'Spider Plant': {'sunlight': 'Medium to Bright', 'description': 'Grows well in bright, indirect light, but can tolerate lower light levels.'},
    'Aloe Vera': {'sunlight': 'Bright to Full Sun', 'description': 'Prefers bright, sunny spots, ideal for a south-facing window.'},
    'Peace Lily': {'sunlight': 'Low to Medium', 'description': 'Prefers low to medium light, perfect for shaded areas.'},
    'Fiddle Leaf Fig': {'sunlight': 'Bright, Indirect', 'description': 'Thrives in bright, indirect light, avoid direct sunlight to prevent leaf burn.'},
}

# HTML template
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indoor Plant Placement Tool</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5 text-center">Indoor Plant Placement Tool</h1>
        <form action="/" method="POST" class="mt-4">
            <div class="form-group">
                <label for="window-orientation">Select Your Window Orientation:</label>
                <select class="form-control" id="window-orientation" name="window_orientation" required>
                    <option value="North">North</option>
                    <option value="East">East</option>
                    <option value="South">South</option>
                    <option value="West">West</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Get Plant Suggestions</button>
        </form>

        {% if suggestions %}
        <div class="mt-4">
            <h2>Plant Suggestions for {{ window_orientation }}-Facing Windows</h2>
            <div class="row">
                {% for plant, data in suggestions.items() %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">{{ plant }}</h5>
                            <p class="card-text"><strong>Sunlight:</strong> {{ data.sunlight }}</p>
                            <p class="card-text">{{ data.description }}</p>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

# Function to get plant suggestions based on window orientation
def get_plant_suggestions(orientation):
    if orientation == 'North':
        return {k: v for k, v in plants_data.items() if 'Low' in v['sunlight']}
    elif orientation == 'East' or orientation == 'West':
        return {k: v for k, v in plants_data.items() if 'Medium' in v['sunlight'] or 'Bright' in v['sunlight']}
    elif orientation == 'South':
        return {k: v for k, v in plants_data.items() if 'Bright' in v['sunlight'] or 'Full Sun' in v['sunlight']}
    return {}

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = None
    window_orientation = None

    if request.method == 'POST':
        window_orientation = request.form['window_orientation']
        suggestions = get_plant_suggestions(window_orientation)

    return render_template_string(html_template, suggestions=suggestions, window_orientation=window_orientation)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
