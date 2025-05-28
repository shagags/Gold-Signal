import os
from uvicorn import run
import app  # or goldwick_api.app as app

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
