def calculate(*args: int, act: str = 'add', fl: bool = False):
    try:
        actions = {
            "add": args[0] + args[1],
            "sub": args[0] - args[1],
            "mul": args[0] * args[1],
            "div": args[0] / args[1]
        }
        res = actions[act]
        if fl:
            return f'The result is {float(res)}'
        return f'The result is {res}'
    except ZeroDivisionError:
        return 'You cannot do calculations with zero!!!!'


print(calculate(42, 33242, act='sub', fl=True))
