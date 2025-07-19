🚀 FastAPI CRUD App with PostgreSQL, Docker, and GitHub Actions CI/CD
This is a production-ready FastAPI project featuring:

✅ Full CRUD operations

✅ PostgreSQL database

✅ Docker + Docker Compose

✅ Environment config with .env

✅ Automated CI/CD pipeline via GitHub Actions

✅ Push to Docker Hub on each commit

📸 Screenshots
Add screenshots here to showcase your app UI, Swagger docs, or CI/CD logs.

Feature

Screenshot

Swagger UI



GitHub Actions



Docker Hub



📁 Project Structure
.
├── app/                    # FastAPI application code
├── tests/                  # Unit and integration tests
├── Dockerfile              # Dockerfile for app
├── docker-compose.yml      # Docker Compose file for multi-container setup
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── .github/
    └── workflows/
        └── ci-cd.yaml      # GitHub Actions pipeline

⚙️ Setup Instructions
1. Clone the Repo
git clone https://github.com/your-username/fastapi-crud-docker.git
cd fastapi-crud-docker

2. Set Up .env File
Create a .env file in the root of your project with the following content:

# .env
DATABASE_URL=postgresql://postgres:Shah%400340@db:5432/fastapi_app

3. Run with Docker Compose
docker-compose up --build

Access your FastAPI app at:

http://localhost:8000/docs

🧪 Run Tests
To run tests inside the Docker container:

docker-compose exec web pytest

Or locally (if not using Docker, ensure dependencies are installed):

pip install -r requirements.txt
pytest

🚀 CI/CD Pipeline (GitHub Actions)
The pipeline performs:

✅ Code Checkout

✅ Linting with flake8

✅ Unit & Integration Testing with pytest

✅ Build Docker image

✅ Push to Docker Hub

✅ Cleanup Docker images

💡 Secrets to set in GitHub repo:

DOCKER_USERNAME

DOCKER_PASSWORD

Workflow file:

.github/workflows/ci-cd.yaml

🐳 Docker Hub Deployment
After successful CI/CD, you can pull your image from Docker Hub:

docker pull your-username/fastapi-app:latest

✅ API Endpoints
Swagger/OpenAPI docs:
http://localhost:8000/docs

Sample endpoints:

GET /items/

POST /items/

PUT /items/{id}

DELETE /items/{id}

📦 Build Locally (Optional)
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app

📸 Screenshots (Folder Placeholder)
Create a screenshots/ folder in the root of your repository and add the following images:

swagger.png

github-actions.png

dockerhub.png

Then update paths above if needed.

🙌 Contributing
Pull requests are welcome.

Open an issue first for significant changes.

📜 License
MIT License (You might want to create a LICENSE file in your repo)

💬 Questions?
Open an issue on GitHub or reach out via LinkedIn.
