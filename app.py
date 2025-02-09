from flask import Flask
from freelance.config import Config
from freelance.models import db, login_manager
from freelance.routes import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and login manager
db.init_app(app)
login_manager.init_app(app)

# Register blueprints
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)
