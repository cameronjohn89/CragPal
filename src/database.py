from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
db = SQLAlchemy()


def initialize_database(app):
    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
