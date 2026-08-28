"""Launch SegBuilder locally with `python run.py`."""

from app.server import application, setup_app


if __name__ == "__main__":
    setup_app()
    print("SegBuilder is running at http://127.0.0.1:8050")
    application.run(host="127.0.0.1", port=8050, debug=False)
