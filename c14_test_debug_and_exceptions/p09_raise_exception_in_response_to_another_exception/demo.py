

try:
    int('N/A')
except Exception as e:
    # raise RuntimeError('A parsing error occurred')
    # raise RuntimeError('A parsing error occurred') from e
    raise RuntimeError('A parsing error occurred') from None
