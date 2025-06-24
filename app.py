import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase URL and Key must be set in .env file")

supabase: Client = create_client(supabase_url, supabase_key)

@app.route('/')
def home():
    return "Hello, World! Backend is running."

if __name__ == '__main__':
    app.run(debug=True)
