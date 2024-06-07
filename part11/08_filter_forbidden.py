
def filter_forbidden(string: str, forbidden: str):
    return ''.join([c for c in string if c not in forbidden])