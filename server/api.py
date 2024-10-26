from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


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
    if 'file' not in request.files or 'code' not in request.form:
        return jsonify({'error': 'File or code not provided'}), 400

    file = request.files['file']
    code = request.form['code']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(RECEIVED_FOLDER, file.filename)
    file.save(file_path)

    # Save code and file path
    file_storage[code] = file_path
    logging.info(f"Received file with code: {code}")  # Logging instead of print
    logging.info(f"Current file storage: {file_storage}")  # Check storage state

    return jsonify({'message': 'File sent successfully!'}), 200

@app.route('/receive', methods=['POST'])
@app.route('/receive', methods=['POST'])
def receive_and_send_file():
    try:
        code = request.form.get('code')
        logging.info(f"Attempting to receive file with code: {code}")
        file_path = get_file_path_from_code(code)

        if file_path:
            logging.info(f"File found for code {code}: {file_path}")
            filename = os.path.basename(file_path)
            return send_file(file_path, download_name=filename, as_attachment=True)
        else:
            logging.warning(f"No file found for code: {code}")
            return jsonify({'error': 'Invalid code or file not found'}), 404
    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
