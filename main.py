from application.files_example.file_example_csv import file_example_csv
from application.logging.init_logging import init_logging


def main() -> None:
    # print(greetings(), student_grade())
    # file_example_txt()
    file_example_csv()


if __name__ == "__main__":
    init_logging()
    main()
