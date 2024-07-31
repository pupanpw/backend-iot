from flask import Flask, request, jsonify, make_response
from config.config import DB_URL
from model.users import User, IotDevice, db
# from controller.iot import IoTDetail
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/test', methods=['GET'])
def test():
    # result = IoTDetail.test()
    return make_response(jsonify({'message': "result", }), 200)


@app.route('/iot-pw', methods=['GET'])
def get_iotdevice():
    try:
        data = IotDevice.query.all()
        return make_response(jsonify([iot_data.json() for iot_data in data]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)


@app.route('/iot-pw', methods=['POST'])
def iotData():
    try:
        data = request.get_json()
        new_data = IotDevice(device=data['device'], device_no=data['device_no'], status=data['status'], isActive=data['isActive'],
                             event=data['event'], created_by=data['created_by'],)
        db.session.add(new_data)
        db.session.commit()
        return make_response(jsonify({'message': "msg"}), 201)
    except Exception as e:
        return make_response(jsonify({'message': 'error creating iot', 'error': str(e)}), 500)
