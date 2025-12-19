"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import argparse
import importlib
import inspect
import logging
import pkgutil

from jaxl.api import resources
from jaxl.api._client import attest
from jaxl.api.client.types import Response


def _init_subparsers(
    subparsers: argparse._SubParsersAction,  # type: ignore[type-arg]
) -> None:
    for module_info in pkgutil.iter_modules(resources.__path__):
        module_name = module_info.name
        full_module_name = f"{resources.__name__}.{module_name}"
        try:
            mod = importlib.import_module(full_module_name)
            # pylint: disable=protected-access
            if hasattr(mod, "_subparser") and inspect.isfunction(mod._subparser):
                help_text = getattr(
                    mod._subparser,
                    "__doc__",
                    f"Manage {module_name.capitalize()}",
                )
                parser = subparsers.add_parser(module_name, help=help_text)
                mod._subparser(parser)
        # pylint: disable=broad-exception-caught
        except Exception as e:
            logging.info(f"Skipping {full_module_name} due to error: {e}")


def main() -> None:
    """CLI Main"""
    logging.getLogger("examples").setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(prog="jaxl", description="Jaxl CLI")
    _init_subparsers(parser.add_subparsers(dest="resource", required=True))
    args = parser.parse_args()
    attest()
    arguments = {k: getattr(args, k) for k in getattr(args, "_arg_keys", [])}
    response = args.func(arguments)
    if not isinstance(response, Response):
        print(response)
    else:
        print(response.parsed)


def entry_point() -> None:
    """CLI entry point"""
    main()
