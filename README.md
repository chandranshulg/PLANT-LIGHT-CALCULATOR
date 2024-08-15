# Indoor Light Calculator

This is a Flask web application that helps users determine the best indoor plants for their space based on the orientation of their windows.

## Features

- Select the orientation of your window (North, East, South, or West).
- Get plant suggestions based on the sunlight needs of various indoor plants.
- Displays plant name, sunlight requirements, and a brief description.


  ## Usage

1. **Run the Flask app:**

   ```bash
   python app.py

2. **Open your web browser and go to:**
     http://127.0.0.1:5000/

## Technologies Used

**Flask**: A lightweight WSGI web application framework in Python.

**Bootstrap**: For styling the web page.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Inspired by the need for optimal plant care based on light conditions.
Plant information was taken from various gardening resources.


## Project Structure

```plaintext
plant-sunlight-project/
│
├── app.py                     # Main Flask application file
├── static/
│   ├── css/
│   │   └── styles.css         # Custom CSS styles
│   └── images/                # Directory for plant images and other static files
│
├── templates/
│   └── index.html             # HTML template for the web application
│
├── data/
│   └── plants.json            # JSON file containing plant data and sunlight requirements
│
└── README.md                  # Documentation file (this file)

