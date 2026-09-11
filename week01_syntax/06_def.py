def do_nothing():
    pass


def greeting(name: str) -> None:
    print(f"Hello {name}!")


def echo(arg):
    return arg + " " + arg


def is_None(thing):
    is_None.calls += 1  # количесво раз вызова функции (обнуляется вне функции, сразу после объявления)
    match thing:
        case None:
            print(f"{(is_None.calls)}. thing is None")
        case True:
            print(f"{is_None.calls}. thing is True")
        case False:
            print(f"{is_None.calls}. thing is False")
        case x if x:
            print(f"{is_None.calls}. thing is truthy: {x!r}")
        case _:
            print(f"{is_None.calls}. thing is falsy/empty")


is_None.calls = 0

is_None(None)
is_None(0)
is_None(1)
is_None([])
is_None(tuple(x for x in range(3)))
is_None({key: val for key, val in enumerate([x for x in range(3)])})
is_None({x for x in range(3)})


def menu(wine, dessert, entree="beef"):
    return {"wine": wine, "entree": entree, "dessert": dessert}


print(menu(dessert="cake", wine="chardonnary", entree="chiken"))
print(menu(dessert="cake", wine="chardonnary"))


def print_args(text, *args):
    print(text, args)


print_args("Positional argument tuple: ", "a", "b", "c")


def print_kwargs(text, **kwargs):
    print(text, kwargs)


print_kwargs("Keyword arguments: ", wine="merlot", entree="mutton", dessert="macaroon")


def sum_args(*args):
    return sum(args)


def run_func(func, *args):
    return func(*args)


print(run_func(sum_args, 1, 2, 3, 4, 5))


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()
print(counter())  # 1
print(counter())  # 2


func = [lambda x=i: x for i in range(2, 10)]
print([f() for f in func])
