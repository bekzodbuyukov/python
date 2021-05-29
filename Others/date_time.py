from contextlib import contextmanager
from datetime import datetime


# context manager
@contextmanager
def tag(some_output):
    """ Just to make it easier to look at a result on terminal """
    print(f'{some_output}')
    yield
    print(f'{some_output}')


def main():
    # print date and time in default style
    print(datetime.now())


if __name__ == "__main__":
    with tag('\n'):
        main()
