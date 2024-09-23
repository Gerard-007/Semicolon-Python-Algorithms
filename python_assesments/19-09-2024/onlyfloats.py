def only_floats(a, b):
    if isinstance(a, float):
        return a
    elif isinstance(b, float):
        return b
    elif isinstance(a, float) and isinstance(b, float):
        return (a, b)