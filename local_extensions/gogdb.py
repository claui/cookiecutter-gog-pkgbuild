# SPDX-FileCopyrightText: Claudia Pellegrino
# SPDX-License-Identifier: 0BSD

"""Local extension to download metadata from gogdb.org."""

import json
from types import SimpleNamespace
import urllib.request

from jinja2 import Environment
from jinja2.ext import Extension


class GogDbExtension(Extension):  # pylint: disable=abstract-method
    """Custom addition to Jinja’s `globals` and `filters` spaces.
    Allows a Jinja template to download and use live metadata from
    the gogdb.org database.
    """

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        def _gog_metadata(gog_id: str) -> SimpleNamespace:
            """Download product metadata from gogdb.org for the
            given gog_id and return it as a dictionary."""

            gogdb_product_endpoint = (
                f"https://www.gogdb.org/data/products/{int(gog_id)}/product.json"
            )
            with urllib.request.urlopen(gogdb_product_endpoint) as response:
                data = response.read()
            # Need attribute access so templates can use `attr` and `selectattr`
            return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

        environment.filters["gog_metadata"] = _gog_metadata
        environment.globals["gog_metadata"] = _gog_metadata
