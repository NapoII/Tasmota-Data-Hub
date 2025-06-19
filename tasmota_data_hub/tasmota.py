from __future__ import annotations

import requests


class TasmotaClient:
    """Simple client for querying Tasmota devices via HTTP."""

    def __init__(self, base_url: str, timeout: int = 5) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _request(self, command: str) -> dict:
        url = f"{self.base_url}/cm?cmnd={command}"
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def status10(self) -> dict:
        """Return sensor status (STATUS 10)."""
        return self._request("Status%2010")

    def energy_status(self) -> dict:
        """Return energy data from the device."""
        data = self.status10()
        return data.get("StatusSNS", {}).get("ENERGY", {})
