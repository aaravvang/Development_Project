from flask import Flask, request, render_template, redirect

from supabase import create_client

#to read env data
import os
from dotenv import load_dotenv
import random

app = Flask("__name__") #flask object

load_dotenv() #loading the info from env file into the os

supabase_url=os.getenv("SUPABASE_URL")
supabase_key=os.getenv("SUPABASE_KEY")


supabase=create_client(supabase_url, supabase_key)

@app.route('/')
def home():
    response = supabase.table('Tasks').select('*').execute()
    
    return render_template("tasks.html", data=response.data)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description')
    
    response = supabase.table('Tasks').insert({
        "task_name": task_name,
        "task_description": task_description,
        "status": "Pending"
    }).execute()
    
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    task_id = int(request.form.get('task_id'))
    new_status = request.form.get('status')
    new_description = request.form.get('task_description')
    
    update_data = {}
    if new_status:
        update_data['status'] = new_status
    if new_description:
        update_data['task_description'] = new_description
    
    response = supabase.table('Tasks').update(update_data).eq("task_id", task_id).execute()
    
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    task_id = int(request.form.get('task_id'))
    response = supabase.table('Tasks').delete().eq("task_id", task_id).execute()
    
    return redirect('/')


if(__name__ == "__main__"):
    app.run(debug=True)