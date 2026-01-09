import os

# Define the project structure
folders = [
    "data/raw",              # Original images of slips
    "data/processed",        # Preprocessed/cleaned images
    "data/annotations",      # Label Studio exports
    "models/donut_finetuned", # Where we save the AI brain
    "backend/app",           # FastAPI logic
    "backend/workers",       # Celery worker code
    "frontend",              # Streamlit dashboard
    "logs",                  # Error and audit logs
    "storage/encrypted_slips" # Secure image storage
]

files = {
    "requirements.txt": """
fastapi
uvicorn
python-multipart
sqlalchemy
psycopg2-binary
cryptography
python-jose[cryptography]
passlib[bcrypt]
transformers
torch
torchvision
pytorch-lightning
opencv-python
pandas
streamlit
celery
redis
pillow
""",
    "backend/app/main.py": "# FastAPI entry point\n",
    "frontend/dashboard.py": "# Streamlit entry point\n",
    "docker-compose.yml": "# To orchestrate Postgres, Redis, and the App\n"
}

def setup():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    
    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content.strip())
        print(f"Created file: {file_path}")

    print("Project structure ready. Run 'pip install -r requirements.txt' next.")

if __name__ == "__main__":
    setup()