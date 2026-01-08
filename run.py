from app import create_app
from config import DevConfig

app = create_app(config=DevConfig)

if __name__ == "__main__":
    app.run(debug=True)
