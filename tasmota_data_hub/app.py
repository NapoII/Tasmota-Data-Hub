from __future__ import annotations
import os
import threading
import time
from flask import Flask, jsonify, render_template

# Import the client as a top-level module so the app can be run
# either as ``python -m tasmota_data_hub.app`` or ``python tasmota_data_hub/app.py``.
from tasmota import TasmotaClient


def create_app() -> Flask:
    app = Flask(__name__)
    tasmota_url = os.getenv("TASMOTA_URL", "http://192.168.1.100")
    poll_interval = int(os.getenv("TASMOTA_POLL_INTERVAL", "30"))

    client = TasmotaClient(tasmota_url)
    data_lock = threading.Lock()
    latest_data: dict[str, float] = {}

    def poll_data() -> None:
        nonlocal latest_data
        while True:
            try:
                energy = client.energy_status()
                with data_lock:
                    latest_data = energy
            except Exception as exc:  # noqa: BLE001
                print("Error fetching data:", exc)
            time.sleep(poll_interval)

    threading.Thread(target=poll_data, daemon=True).start()

    @app.route("/data")
    def data() -> str:
        with data_lock:
            return jsonify(latest_data)

    @app.route("/")
    def index() -> str:
        return render_template("index.html")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
