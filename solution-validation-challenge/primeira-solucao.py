
def validate(_logic):
    _logic = str(_logic)
    if 'def' not in _logic:
        return 'missing def'

    if ':' not in _logic:
        return 'missing :'

    if not '(' in _logic or not ')' in _logic:
        return 'missing paren'

    if "".join(['(', ')']) in _logic:
        return 'missing param'

    if '    ' not in _logic:
        return 'missing indent'

    if 'validate' not in _logic:
        return "wrong name"

    if 'return' not in _logic:
        return "missing return"

    return True
