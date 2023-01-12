[Sui JSON RPC](https://docs.sui.io/sui-jsonrpc) Python wrapper
=======

### Note:

This project is not production ready and there are still missing methods.
Feel free to add new methods in methods.py file to use in your project.


### Compatibility

Tested on Python 3.10+


### Get Started

**Example (Sui Json RPC rovider):**

```python
>>> from sui_json_rpc import SuiJsonRPCProvider
>>>
>>> sui_provider = SuiJsonRPCProvider()
>>> sui_provider.send("get_balance", params={"account": "0xbff6ccc8707aa517b4f1b95750a2a8c666012df3"})
```

### Add missing method

Currently, there are missing methods in project. If you want to add some of these missing methods,
you can simply create a method object in `methods.py` file and register it on `SuiJsonRPCMethodsBuilder` object.


```python
from sui_json_rpc.method_builder import sui_rpc_method_builder
from sui_json_rpc.base import Method

@sui_rpc_method_builder.register("my_new_method")
class MyNewMethod(Method):
    METHOD_NAME = "sui_myNewMethod"
    REQUIRED_PARAMS = ["address", "param_2"]
```

And that's all. Your new method is ready to use.


```python
>>> from sui_json_rpc import SuiJsonRPCProvider
>>>
>>> sui_provider = SuiJsonRPCProvider()
>>> sui_provider.send("my_new_method", params={"account": "0xbff6ccc8707aa517b4f1b95750a2a8c666012df3", "param_2" : "Other paremeter"})
```
