from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        # Add other configuration variables as needed
    )

    # Register blueprints
    from .routes import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app