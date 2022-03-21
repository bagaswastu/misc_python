from dataclasses import dataclass
from datetime import datetime

import cloudscraper


@dataclass
class Breach:
    name: str
    title: str
    domain: str
    date: datetime
    pwn_count: int
    breached_data: list[str]


class ScrapeException(Exception):
    """
    Exception that occurred while checking.
    """

    def __init__(self, message: str, detail: str):
        self.message = message
        self.detail = detail
        super().__init__(self.message)


def check_breach(email: str) -> list[Breach]:
    """
    Check breached data with email from HIBP. Will return list breached information.
    """

    scraper = cloudscraper.create_scraper()

    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"

    try:
        res = scraper.get(url)
        if res.status_code == 200:
            breaches = res.json()["Breaches"]

            if len(breaches) == 0:
                return []

            return list(
                map(
                    lambda breach: Breach(
                        name=breach["Name"],
                        title=breach["Title"],
                        domain=breach["Domain"],
                        breached_data=breach["DataClasses"],
                        date=breach["BreachDate"],
                        pwn_count=breach["PwnCount"],
                    ),
                    breaches,
                )
            )
        else:
            ScrapeException(
                f"Error {res.status_code} when doing requests.", str(res.headers)
            )
    except Exception as e:
        raise ScrapeException(f"Unknown error, please check your internet", str(e))
