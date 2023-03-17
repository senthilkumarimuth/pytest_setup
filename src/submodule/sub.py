
def divide(a,b):
    try:
        c = a/b

    except ZeroDivisionError as e:
        c = e
    return c