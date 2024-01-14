from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate/area/circle', methods=['POST'])
def calculate_area_circle():
    data = request.get_json()
    radius = data.get('radius')
    area = 3.14 * radius ** 2
    return jsonify({'result': area})

@app.route('/calculate/area/rectangle', methods=['POST'])
def calculate_area_rectangle():
    data = request.get_json()
    length = data.get('length')
    width = data.get('width')
    area = length * width
    return jsonify({'result': area})

@app.route('/calculate/weight', methods=['POST'])
def calculate_weight():
    data = request.get_json()
    mass = data.get('mass')
    gravity = 9.81
    weight = mass * gravity
    return jsonify({'result': weight})

@app.route('/calculate/density', methods=['POST'])
def calculate_density():
    data = request.get_json()
    mass = data.get('mass')
    volume = data.get('volume')
    density = mass / volume
    return jsonify({'result': density})

if __name__ == "__main__":
    app.run(debug=True)
