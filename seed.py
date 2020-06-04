"""Seed file to make sample data for users db."""
from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
harry = User(first_name='Harry', last_name='Teplow',
             image_url='https://chaitunesacappella.files.wordpress.com/2015/01/10293733_10202869677997835_7526054888527045343_o_fotor-e1421263322654.jpg?w=300')
marco = User(first_name='Marco', last_name='van Vemden', image_url='https://pbs.twimg.com/profile_images/1221320094304727042/kNYkiXa9_400x400.jpg')

# Add new objects to session, so they'll persist
db.session.add(harry)
db.session.add(marco)

# Commit--otherwise, this never gets saved!
db.session.commit()
