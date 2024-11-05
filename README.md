# Project Dashboard for GitHub Projects

Welcome to my Project Dashboard repository! This project is designed to streamline project management by centralizing recent commits, next-step notes, and project links into a single, accessible interface. Built with Flask, the dashboard is intended to simplify tracking progress and plans across multiple GitHub repositories.

# Features

**Commit Tracking**: Displays recent commits for each project repository, providing a quick overview of recent updates.

**Project Navigation**: Contains direct links to individual project pages for easy access.

**Next-Step Notes**: Editable and savable note sections for each project, allowing for planning and documentation of upcoming tasks.

**Support for Multiple Projects**: Designed with placeholders for future projects, allowing for easy expansion of the dashboard.

# Project Structure

```
project_dashboard/
│
├── templates/
│   └── dashboard.html           # HTML template for the dashboard interface
│
├── app.py                       # Flask app for rendering the dashboard and handling requests
├── requirements.txt             # List of project dependencies
└── README.md                    # Project documentation
```
# Getting Started

**Prerequisites**

```
java
Copy code
Python 3.8+
Flask
Git for version control
```

# Installation

**Clone the Repository**

```
git clone https://github.com/SamFonss/project-dashboard.git
cd project-dashboard
```

**Create a Virtual Environment**

```
python3 -m venv venv
source venv/bin/activate
```

**Install Dependencies**

```
pip install -r requirements.txt
```

**Set Up Environment Variables**

Store your GitHub token in an environment variable to securely access commit data:

```
export GITHUB_TOKEN=your_token_here
```

**Run the Application**
Start the Dashboard

```
python3 app.py
```

Navigate to http://localhost:8001 to access the dashboard, where you can view recent commits, manage next-step notes, and navigate to project-specific pages.

# Usage

**Commit Viewing**

View recent commits for each project repository under each project section.

**Next-Step Notes**

Add notes in the designated sections. Notes are saved on change and persist on page reload.

**Project Links**

Quickly access individual project pages through direct links on the dashboard.

**Contributions**

Contributions are welcome! If you would like to contribute, please open an issue or submit a pull request.

# License

MIT License

# Contact

For questions or collaboration, please reach out via GitHub Issues or email at samfonss@gmail.com.






