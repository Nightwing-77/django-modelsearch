import argparse
import os

import django

from django.core.management import call_command


def main():
    parser = argparse.ArgumentParser(
        description="Run Django tests with a specified search backend."
    )
    parser.add_argument(
        "--backend",
        required=True,
        help="Specify the search backend (db, elasticsearch7, elasticsearch8, elasticsearch9, opensearch2, opensearch3).",
    )
    parser.add_argument(
        "--test",
        default=None,
        help="Specific test to run (e.g., modelsearch.tests.test_sqlite_backend.TestSQLiteSearchBackend.test_ranking)",
    )

    args = parser.parse_args()

    os.environ["SEARCH_BACKEND"] = args.backend
    os.environ["DJANGO_SETTINGS_MODULE"] = "modelsearch.test.settings"

    django.setup()

    if args.test:
        call_command("test", args.test)
    else:
        call_command("test")


if __name__ == "__main__":
    main()
