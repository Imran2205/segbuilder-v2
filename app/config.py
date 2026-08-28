import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOCAL_FOLDER = Path(os.getenv("SEGBUILDER_STORAGE_DIR", PROJECT_ROOT / "local_storage"))
LOCAL_DB_FILE = Path(os.getenv("SEGBUILDER_DB_FILE", PROJECT_ROOT / "local_db.json"))
LOG_FOLDER = Path(os.getenv("SEGBUILDER_LOG_DIR", PROJECT_ROOT / "logs"))
