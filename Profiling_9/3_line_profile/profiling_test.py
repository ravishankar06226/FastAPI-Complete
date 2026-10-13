#kernprof -v -l profiling_test.py
from app import process_data


@profile
def run():
    process_data(10000)


if __name__ == '__main__':
    run()
