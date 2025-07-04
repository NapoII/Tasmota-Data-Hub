# Tasmota Data Hub

A simple Flask application for reading energy data from a Tasmota Smart Plug and displaying it in real-time with a modern "liquid glass" style interface.

## Features

- Periodically queries a Tasmota device using its HTTP API.
- Serves a minimal web page powered by [Flask](https://flask.palletsprojects.com/) and [Chart.js](https://www.chartjs.org/) to visualize power usage.
- Designed to be lightweight and easy to deploy.

## Requirements

- Python 3.11+
- `pip install -r requirements.txt`
- A Tasmota device accessible via HTTP

## Running

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set the `TASMOTA_URL` environment variable to the base URL of your device, e.g. `http://192.168.1.50`.

3. Start the application:

```bash
python -m tasmota_data_hub.app
```

Open `http://localhost:5000` in your browser to view the dashboard.

## Configuration

- `TASMOTA_URL` – Base URL of the Tasmota device (default `http://192.168.1.100`).
- `TASMOTA_POLL_INTERVAL` – Polling interval in seconds (default `30`).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
