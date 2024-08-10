import pathlib

BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent
ICON_DIR = BASE_DIR / "icons"
SAVE_FOLDER_NAME = "qr-codes"
LOGO_FILE = ICON_DIR / "logo.png"
QUIT_FILE = ICON_DIR / "quit.png"
SAVE_FILE = ICON_DIR / "save.png"
