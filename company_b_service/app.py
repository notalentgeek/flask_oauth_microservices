from controllers.controller import company_b_bp
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Initialize App and Configurations
app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(company_b_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
