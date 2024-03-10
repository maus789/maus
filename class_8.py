def iter_numbers():
    for i in range(10):
        yield i

iterator = iter_numbers()

for i in iterator:
    print(i)


def func_gen():
    i = 1
    while True:
        yield i
        i += 1
f = func_gen()
print(next(f))
print(next(f))


def func_gen():
    i = 1
    while True:
        yield i
        i += 1
f = func_gen()
print(next(f))


f = (i for i in range(50))
print(f)
print(next(f))
print(next(f))
print(next(f))


def test_range():
    for i in range(0, 1):
        yield i

i = test_range()
print(next(i))


def outer_function():
    x = 10
    def inner function():
        nonlocal x
        x += 1
        return x

return inner_function

function = outer_function()

print(function())


@guard_zero
def divide(x, y):
    return x / y


def divide(x, y)
    return x, y


def guard_zero (operate):
    def inner(x, y):
        if y == 0:
            print("Cannot divide by 0.")
            return
        return operate(x, y)
    return inner


divide = guard_zero(divide)


@guard_zero
def divide(x, y):
    return x / y


print(divide(5,  0)
print(divide (5,  2))


Cannot divide by 0.
None
2.5


def guard_zero (operate):

    def inner (x, y):
        if y == 0:
            print("Cannot divide by Θ.")
            return
        return operate(x, y)

    return inner

1 usage new
11
@quard_zero
12
def divide (x, y):
13
return x Y
print(divide(x: 5, у 0)) # виводить Cannot divide by («На 8 ділити не можна»)