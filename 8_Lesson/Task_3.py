def type_logger(func):
    def some_def(*args, **kwargs):
        if callable(func):
            print(f'Call for: {func.__name__}')
        for i in args:
            print(f'{i}: {type(i)}')
        rez = func(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                print(f'{key} = {value}: {type(value)}', end=', ')
        print(f'\nRezult:{rez} type:{type(rez)}')
        return rez
    return some_def

@type_logger
def render_input(*args, **kwargs):
    return 1

@type_logger
def calc_cube(x):
    return x ** 3


