# Import Blueprints
from connections.db_connection import db
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Initialize App and Configurations
app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
