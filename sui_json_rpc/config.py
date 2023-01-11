import os


class Config:
    DEFAULT_RPC_URL: str = "https://fullnode.devnet.sui.io:443"
    RPC_URL: str = os.getenv("SUI_RPC_URL", DEFAULT_RPC_URL)
    JSON_RPC_VERSION: str = "2.0"
    JSON_RPC_ID: int = 1


config: object = Config()
