from typing import Dict

from sui_json_rpc.config import config


class SuiJsonRPCMethodsBuilder:
    METHODS: dict[str, callable] = {}

    def __getattr__(self, method: str):
        """Get an attribute.

        :param method: The method to get.
        :return: The method.
        """
        sui_method = self.METHODS.get(method)

        if sui_method is None:
            raise AttributeError(f"Method `{method}` does not exist.")

        def wrapper(**kwargs):

            if sui_method.REQUIRED_PARAMS:
                for param in sui_method.REQUIRED_PARAMS:
                    if param not in kwargs:
                        raise ValueError(f"Missing required parameter `{param}`.")
            return self.prepare_body(sui_method, kwargs)

        return wrapper

    def prepare_body(self, method: str, params: dict) -> Dict:
        """Prepare the body of the request.

        :param method: The method to call.
        :param params: The parameters to pass to the method.
        :return: The body of the request.
        """
        return {
            "jsonrpc": config.JSON_RPC_VERSION,
            "id": config.JSON_RPC_ID,
            "method": method.METHOD_NAME,
            "params": list(params.values()),
        }

    def register(self, method: str) -> callable:
        """Register a method.

        :param method: The method to register.
        :return: The method.
        """

        def decorator(object):

            if method in self.METHODS:
                raise ValueError(f"Method `{method}` already exists.")

            self.METHODS[method] = object()
            return object

        return decorator


sui_rpc_method_builder: object = SuiJsonRPCMethodsBuilder()
