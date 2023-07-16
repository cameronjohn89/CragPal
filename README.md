# Crag Pal

Crag Pal is a web application that allows climbers to search for climbing crags, log their climbs, and manage their climbing progress. Users can search for crags by location, log climbs on specific routes, and keep track of their climbing achievements.

## Features

- Search for climbing crags by location
- Log climbs on specific routes
- View detailed information about crags and routes
- Track personal climbing progress
- Manage user profile and preferences

## Technologies Used

- Python
- Flask
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository: `git clone https://github.com/your-username/crag-pal.git`
2. Navigate to the project directory: `cd crag-pal`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database (PostgreSQL) and update the database configuration in `config.py`
5. Run the application: `python cragpal.py`
6. Access the application in your browser at `http://localhost:5000`

## Usage

- Visit the homepage to search for climbing crags and browse available routes.
- Create an account or log in to start logging your climbs.
- Select a route and log your climb by providing the necessary details.
- View your logged climbs and track your climbing progress.

## API Endpoints

- `/crags` - GET: Retrieve a list of all crags
- `/crags/<crag_id>` - GET: Retrieve details of a specific crag
- `/routes` - GET: Retrieve a list of all routes
- `/routes/<route_id>` - GET: Retrieve details of a specific route
- `/routes` - POST: Create a new climbing route
- `/routes/<route_id>/climbs` - POST: Log a climb on a route

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


