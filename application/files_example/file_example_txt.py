from application.config.paths import FILES_OUTPUT_PATH
from application.files_example.generators import generate_humans
from application.logging.loggers import get_core_logger


def file_example_txt() -> None:
    logger = get_core_logger()
    path_to_file = FILES_OUTPUT_PATH.joinpath("output.txt")
    amount: int = 10
    with open(path_to_file, mode="w") as file:
        for human in generate_humans(amount=amount):
            file.write(f"{human.name} {human.age}\n")

    logger.info(f"Path to file: file://{path_to_file}")

    files_content = path_to_file.read_text()

    print(files_content)


if __name__ == "__main__":
    file_example_txt()
