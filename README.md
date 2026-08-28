# SegBuilder

SegBuilder is a local Dash application for labeling SAM-generated segmentations
for downstream computer vision applications. It stores all application data on
your computer; Docker and AWS are not required.

## Quick launch (macOS/Linux)

Run:

```sh
./launch.sh
```

The launcher creates a private Python environment, installs dependencies when
needed, and starts SegBuilder. Then open <http://127.0.0.1:8050>.

## Manual install

Python 3.11 is recommended.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Then launch with:

```sh
python3 run.py
```

Then open <http://127.0.0.1:8050>.

On the first launch, SegBuilder automatically creates:

- `local_db.json` for users, projects, and class definitions
- `local_storage/` for images, masks, and project files

The initial login is:

- Username: `local_user`
- Password: `password`

Change the password from the user menu after logging in.

## Optional local paths

By default, data is stored in the project directory. You can override the paths
with `SEGBUILDER_DB_FILE`, `SEGBUILDER_STORAGE_DIR`, and `SEGBUILDER_LOG_DIR`.
