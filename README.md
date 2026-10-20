# Assignment-4-DevOps

## Project
A Flask application containerized using Docker and Docker Compose.

## Technologies
- Python and Flask
- Docker and Docker Compose
- MySQL
- Docker volumes, networks, and health checks

## Run the Application
1. Create a local .env file using the example configuration.
2. Start Docker Desktop.
3. Run:

docker compose up --build -d

## Access the Application
- Home: http://localhost:5000
- Health: http://localhost:5000/health
- Database Health: http://localhost:5000/db-health

## Stop the Application
docker compose down

Note: Do not commit .env files or real credentials.
