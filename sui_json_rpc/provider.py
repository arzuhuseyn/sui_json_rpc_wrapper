import requests

from .config import config
from sui_json_rpc.methods import sui_rpc_method_builder


class SuiJsonRPCProvider:
    """A provider for the Sui RPC JSON API."""

    method_builder = sui_rpc_method_builder

    def __init__(self, rpc_url: str = None):
        self.rpc_url = rpc_url or config.RPC_URL

    def request(self, payload: dict) -> dict:
        """Send a request to the Sui RPC JSON API.

        :param payload: The payload to send.
        :return: The response from the Sui RPC JSON API.
        """
        response = requests.post(self.rpc_url, json=payload)
        response.raise_for_status()
        return response.json()

    def send(self, method: str, params: dict) -> dict:
        """Send a request to the Sui RPC JSON API.

        :param method: The method to call.
        :param params: The parameters to pass to the method.
        :return: The response from the Sui RPC JSON API.
        """
        sui_method = getattr(self.method_builder, method)
        payload = sui_method(**params)
        return self.request(payload)
