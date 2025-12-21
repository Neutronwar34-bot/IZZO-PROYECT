from izzoApp import create_app
from izzoApp.config.development import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run(debug=True)
