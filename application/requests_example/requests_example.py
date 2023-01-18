import json

import requests

from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger
import urllib.parse


def requests_example() -> None:
    logger = get_core_logger()
    # url = 'https://httpbin.org/get'
    url = "https://cataas.com/cat?json=true"

    path = FILES_OUTPUT_PATH.joinpath("output.json")

    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response}")
        response_json = response.json()
        logger.info(f"{response_json=}")

        path.write_text(json.dumps(response_json, indent=2))

        url_part_to_image = response_json["url"]
        url_to_image = urllib.parse.urljoin(url, url_part_to_image)

        response_with_image = session.get(url_to_image)
        logger.info(f"{response_with_image}")

        extension = response_json["file"].rsplit(".", maxsplit=1)[-1]
        path_image = FILES_OUTPUT_PATH.joinpath(f"cat.{extension}")
        path_image.write_bytes(response_with_image.content)
