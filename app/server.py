from app import app, application
from .layouts.main_layout import get_main_layout
from .resources import initialize_local_data

def setup_app():
    initialize_local_data()
    app.layout = get_main_layout()

# Run the app if this script is executed directly.
if __name__ == "__main__":
    setup_app()
    application.run(host="127.0.0.1", port=8050, debug=False)
