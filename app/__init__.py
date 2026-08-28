import os

from flask import Flask, send_from_directory
import dash
import dash_bootstrap_components as dbc
import logging

from .config import LOCAL_FOLDER
from .data.user_management import login_manager

# this function sets up the logging configuration
def setup_logging():
    logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Console handler that logs only higher level messages
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


setup_logging()


# Flask is the local HTTP server used by Dash.
application = Flask(__name__)
application.secret_key = os.getenv("SEGBUILDER_SECRET_KEY", "local-development-key")
application.config["SESSION_COOKIE_SECURE"] = False


@application.route("/local-storage/<path:filename>")
def local_storage_file(filename):
    return send_from_directory(LOCAL_FOLDER, filename)

login_manager.init_app(application)

# Initialize Dash application with Flask as server
app = dash.Dash(__name__, server=application, title="SegBuilder",
                url_base_pathname='/', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Importing layouts and callbacks after app initialization to avoid circular imports
from .layouts import main_layout
from .callbacks import register_callbacks


register_callbacks(app)
