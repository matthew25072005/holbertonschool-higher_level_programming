#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as file:
        file.seek(16)
        code = marshal.load(file)
        module = types.ModuleType("hidden_module")
        exec(code, module.__dict__)

    names = dir(module)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
