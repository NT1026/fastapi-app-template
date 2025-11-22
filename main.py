from uvicorn import run

from api import app
from configs import SETTINGS


if __name__ == "__main__":
    run(
        app,
        host=SETTINGS.app_host,
        port=SETTINGS.app_port,
    )
