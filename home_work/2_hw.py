def task_1() -> None:
    a: int = 2
    b: float = 3.25
    c: str = 'Hello World!'
    d: list = [1, 2, 3, 4, 5]
    e: bool = True

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))

task_1()


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21] #Числа Фибоначчи
    print (a[0:3])

task_2()


def task_3(x: int) -> int:
    return x**2

print(task_3(25))



