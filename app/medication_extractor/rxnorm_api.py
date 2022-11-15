# standard libaries
import json
import re
from typing import Any, Dict

# third party libraries
import requests

REGEX_SPACE = re.compile(r"\s")


class RXNormAPI:
    """
    RXNorm API Interface
    """

    rxnorm_base = "https://rxnav.nlm.nih.gov/"

    @classmethod
    def get_approximate_match(cls, query: str, max_entries: int = 2, active_concepts: bool = True) -> Dict[str, Any]:
        """Query RXNorm database with fuzzy string matching.

        Args:
            query (str): Drug name
            max_entries (int, optional): Max entries to return. Defaults to 2.
            active_concepts (bool, optional): If true return only active drugs. Defaults to True.

        Returns:
            Dict[str, Any]: RXNorm JSON response
        """
        query = format_query_spaces(query)

        url: str = RXNormQueries.approximate_match.format(
            query=query, max_entries=max_entries, active_concepts=int(active_concepts)
        )

        resp = requests.get(cls.rxnorm_base + url)
        return json_encode_response(resp)


class RXNormQueries:
    """
    RXNorm API formatted queries
    """

    approximate_match: str = "REST/approximateTerm.json?term={query}&maxEntries={max_entries}&option={active_concepts}"


def format_query_spaces(query: str) -> str:
    """Format multitoken string with API formatted whitespaces

    Args:
        query (str): API query

    Returns:
        str: API query formatted whitespaces characters
    """
    return re.sub(REGEX_SPACE, "%", query)


def json_encode_response(resp: requests.models.Response) -> Dict[str, Dict[str, str]]:
    """Convert requests response object into json instance

    Args:
        resp (requests.models.Response): Response from Requests library

    Returns:
        Dict[str, Dict[str, str]]: json instance
    """
    return json.loads(resp.content)
