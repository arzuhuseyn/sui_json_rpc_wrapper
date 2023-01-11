from sui_json_rpc.method_builder import sui_rpc_method_builder
from sui_json_rpc.base import Method


@sui_rpc_method_builder.register("get_balance")
class GetBalance(Method):
    METHOD_NAME = "sui_getBalance"
    REQUIRED_PARAMS = ["address"]


@sui_rpc_method_builder.register("get_transaction")
class GetTransaction(Method):
    METHOD_NAME = "sui_getTransaction"
    REQUIRED_PARAMS = ["transaction_hash"]


@sui_rpc_method_builder.register("batch_transaction")
class BatchTransaction(Method):
    METHOD_NAME = "sui_batchTransaction"
    REQUIRED_PARAMS = ["sender", "move_call_requests", "gas_price"]


@sui_rpc_method_builder.register("get_all_coins")
class GetAllCoins(Method):
    METHOD_NAME = "sui_getAllCoins"
    REQUIRED_PARAMS = ["address"]


@sui_rpc_method_builder.register("get_all_coins_by_owner")
class GetAllCoinsByOwner(Method):
    METHOD_NAME = "sui_getAllCoinsByOwner"
    REQUIRED_PARAMS = ["address"]


@sui_rpc_method_builder.register("get_events")
class GetEvents(Method):
    METHOD_NAME = "sui_getEvents"
    REQUIRED_PARAMS = ["query"]


@sui_rpc_method_builder.register("get_all_balances")
class GetAllBalances(Method):
    METHOD_NAME = "sui_getAllBalances"
    REQUIRED_PARAMS = ["address"]
