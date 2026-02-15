from flask import Flask
from supabase import create_client

#to read env data
import os
from dotenv import load_dotenv

app = Flask("__name__") #flask object

load_dotenv() #loading the info from env file into the os

supabase_url=os.getenv("SUPABASE_URL")
supabase_key=os.getenv("SUPABASE_KEY")


supabase=create_client(supabase_url, supabase_key)

@app.route('/')
def home():
   response = supabase.table('Customers').select('*').execute()
   return response.data

@app.route('/count')
def count():
    response = supabase.table('Customers').select("*", count="exact").execute()
    return str(response.count)

@app.route('/usa')
def usa():
    response = supabase.table('Customers').select('first_name').filter('usa')


if __name__ == "__main__":
    app.run(debug=True)
