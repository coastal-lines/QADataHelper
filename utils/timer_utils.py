from time import sleep


def check_number_response_and_wait(list_test_cases: list):
    if ((len(list_test_cases) / 500).is_integer()):
        sleep(91)