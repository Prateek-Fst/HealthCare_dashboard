from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        name = request.form['name']
        age = request.form['age']
        file = request.files['file']
        
        if not file:
            return jsonify({'message': 'No file uploaded'}), 400
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return jsonify({'message': f'Hello {name}, your file has been uploaded successfully!'})
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
