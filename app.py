from flask import Flask
from flask_jwt_extended import JWTManager
from auth.auth import auth_blueprint
from machine.machine_controller import machine_blueprint
from flask import Flask, send_from_directory


app = Flask(__name__)
app.config.from_pyfile('config.py')
jwt = JWTManager(app)


# Route สำหรับหน้าแรก
@app.route('/')
def index():
    # ส่งคืนไฟล์ index.html
    return send_from_directory('static', 'index.html')

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(machine_blueprint, url_prefix="/machine")

if __name__ == "__main__":
    app.run(debug=True)
