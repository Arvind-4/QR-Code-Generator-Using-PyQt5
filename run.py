import os

from app.main import main

os.environ.setdefault("XDG_SESSION_TYPE", "wayland")
os.environ.setdefault("QT_QPA_PLATFORM", "xcb")

if __name__ == "__main__":
    main()
