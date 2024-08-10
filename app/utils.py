import pathlib
from datetime import date, datetime

from app.config import BASE_DIR, SAVE_FOLDER_NAME


def get_file_name() -> str:
    today = date.today()
    date_stamp = today.strftime("%d-%m-%Y")
    now = datetime.now()
    time_stamp = now.strftime("%H-%M-%S")
    return f"{time_stamp}_{date_stamp}.png"


def get_save_folder_name() -> pathlib.Path:
    if not (BASE_DIR / SAVE_FOLDER_NAME).exists():
        (BASE_DIR / SAVE_FOLDER_NAME).mkdir(exist_ok=True, parents=True)
    return BASE_DIR / SAVE_FOLDER_NAME
