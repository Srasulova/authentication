from app import app
from models import db, User

# Create the Flask application context
with app.app_context():
    # Drop existing tables (if any) and create new ones
    db.drop_all()
    db.create_all()

    # Create sample Cupcake instances
    user1 = User(
        flavor="cherry",
        size="large",
        rating=5,
    )

    user2 = User(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    # Add Cupcakes to the database session and commit changes
    db.session.add_all([user1, user2])
    db.session.commit()
