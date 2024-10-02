from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Set the path for the received files folder
RECEIVED_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads', 'received_files')
os.makedirs(RECEIVED_FOLDER, exist_ok=True)

# Dictionary to store code-file mappings
file_storage = {}

@app.route('/send', methods=['POST'])
def send_file_route():
    if 'file' not in request.files or 'code' not in request.form:
        return jsonify({'error': 'File or code not provided'}), 400

    file = request.files['file']
    code = request.form['code']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to the uploads directory
    file_path = os.path.join(RECEIVED_FOLDER, file.filename)
    file.save(file_path)

    file_storage[code] = file_path

    return jsonify({'message': 'File sent successfully!'}), 200

@app.route('/receive', methods=['POST'])
def receive_and_send_file():
    try:
        if 'code' not in request.form:
            return jsonify({'error': 'Code not provided'}), 400

        code = request.form['code']
        file_path = get_file_path_from_code(code)

        if file_path:
            filename = os.path.basename(file_path)
            return send_file(file_path, download_name=filename, as_attachment=True)
        else:
            return jsonify({'error': 'Invalid code or file not found'}), 404

    except Exception as e:
        print(f"Exception occurred: {str(e)}")  # Debugging line
        return jsonify({'error': str(e)}), 500


def get_file_path_from_code(code):
    if code in file_storage:
        return file_storage[code]
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)