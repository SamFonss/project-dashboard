from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Retrieves GitHub credentials
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  
GITHUB_USERNAME = "SamFonss"

# Gets commits from GitHub API
def get_commits(repo):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}/commits'
    response = requests.get(url, headers=headers)
    commits = response.json() if response.status_code == 200 else []
    return commits

# Endpoint to save notes
@app.route('/save_notes', methods=['POST'])
def save_notes():
    
    notes_dir = "notes"
    
    # Ensure the directory exists
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    notes = request.form.get('notes')
    project_index = request.form.get('project')  # Project index from the form
    
    # Saves notes to a file
    filename = os.path.join(notes_dir, f'project_{project_index}_notes.txt')
    with open(filename, 'w') as file:
        file.write(notes)
    
    return '', 204  # No content response

# Loads notes from a file
def load_notes(project_index):
    
    notes_dir = "notes"
   
    filename = os.path.join(notes_dir, f'project_{project_index}_notes.txt')
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    return ""

@app.route('/')
def dashboard():
    repo = "music-streaming-project"  
    commits = get_commits(repo)
    
    # Loads notes for each project
    project_notes = {
        0: load_notes(0),
        1: load_notes(1),  
        2: load_notes(2)   
    }
    return render_template('dashboard.html', commits=commits, project_notes=project_notes)



if __name__ == '__main__':
    app.run(port=8001)



