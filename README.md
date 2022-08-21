# procx-py

`procx-py` is a simple wrapper library for [procx](https://github.com/robertlestak/procx). `procx-py` exports a single function, `procx`, which accepts one argument `args` and returns a tuple of the form `(output, error)`. If the query runs successfully but returns no output, `output` will be `None`.

You must have `procx` installed in order to use `procx-py`.

See `examples/example.py` for an example of using one codebase and dynamically pushing to multiple services with a single configuration array.

Here is a basic example:

```python
args = [
    "-driver",
    "redis-list",
    "-redis-host",
    "localhost",
    "-redis-port",
    "6379",
    "-redis-key",
    "test-redis-list",
]

out, err = procx.procx(args)
print(out)
```

Since the entire data layer configuration is contained within the `args` array, this can be moved to a configuration layer such as Vault or Consul. If you ever need to change the data layer configuration, you can simply update the `args` configuration, and your code will remain entirely the same.
