import bonobo


# https://www.youtube.com/watch?v=OrNkstD_1O8

def call_a():
    return 'a'


def call_b():
    return 'b'


def generate_data():
    yield call_a()
    yield call_b()


def uppercase(x: str):
    return x.upper()


def output(x: str):
    print(x)


graph = bonobo.Graph(
    generate_data,
    uppercase,
    output,
)

if __name__ == '__main__':
    bonobo.run(graph)
