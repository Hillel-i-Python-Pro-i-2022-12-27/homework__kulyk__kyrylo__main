import csv
from typing import Final

from application.config.paths import FILES_OUTPUT_PATH
from application.files_example.generators import generate_humans, Human
from application.logging.loggers import get_core_logger

KEY__NAME: Final[str] = "name"
KEY__AGE: Final[str] = "age"


def file_example_csv() -> None:
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("output.csv")

    amount: int = 10

    with open(path_to_file, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=[KEY__NAME, KEY__AGE])

        writer.writeheader()
        for human in generate_humans(amount=amount):
            writer.writerow({KEY__NAME: human.name, KEY__AGE: human.age})

    logger.info(f"Path to file: file://{path_to_file}")

    humans = []
    with open(path_to_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            human = Human(name=row[KEY__NAME], age=int(row[KEY__AGE]))
            humans.append(human)

    print(humans)


if __name__ == "__main__":
    file_example_csv()
