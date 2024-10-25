from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all origins

# Set the path for the received files folder
RECEIVED_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads', 'received_files')
os.makedirs(RECEIVED_FOLDER, exist_ok=True)

# Dictionary to store code-file mappings
file_storage = {}

def get_file_path_from_code(code):
    """Retrieve the file path associated with the given code."""
    return file_storage.get(code)

@app.route('/send', methods=['POST'])
def send_file_route():
    """Handle file upload and store the associated code."""
    if 'file' not in request.files or 'code' not in request.form:
        return jsonify({'error': 'File or code not provided'}), 400

    file = request.files['file']
    code = request.form['code']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to the received files directory
    file_path = os.path.join(RECEIVED_FOLDER, file.filename)
    file.save(file_path)

    # Store the file path associated with the code
    file_storage[code] = file_path
    print(f"Received file with code: {code}")  # Log the received file code
    print(f"Current file storage: {file_storage}")  # Log current file storage

    return jsonify({'message': 'File sent successfully!'}), 200

@app.route('/receive', methods=['POST'])
def receive_and_send_file():
    """Send the requested file back to the client based on the provided code."""
    try:
        code = request.form.get('code')
        print(f"Attempting to receive file with code: {code}")  # Log the code being processed
        file_path = get_file_path_from_code(code)

        if file_path:
            print(f"File found for code {code}: {file_path}")  # Log if the file is found
            filename = os.path.basename(file_path)
            return send_file(file_path, download_name=filename, as_attachment=True)
        else:
            print(f"No file found for code: {code}")  # Log if no file found
            return jsonify({'error': 'Invalid code or file not found'}), 404
    except Exception as e:
        print(f"Exception occurred: {str(e)}")  # Log exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
