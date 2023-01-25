from argparse import ArgumentParser
import csv
import random
import re
import string


class CSVRandomDataGenerator:
    """This module randomly generates data into a created CSV file
    using the specified row number (arg) passed with a desired filename"""

    global ERROR_TEXT
    global ERROR_NUM_ROWS

    ERROR_TEXT = "Invalid file format: Replacing the filename with default value"
    ERROR_NUM_ROWS = (
        "Inputed value is not an integer: Replacing the num_row with default value"
    )

    def __init__(self, num_rows: int, filename: str) -> None:
        self.num_rows = abs(num_rows)
        self.filename = filename

    def formatter(self) -> str:
        if not self.filename.endswith(".csv"):
            return self.filename + ".csv"
        return self.filename
        # self.filename = re.sub(r"[^a-zA-Z0-9 ]", "", self.filename)
        # return self.filename

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(-n {self.num_rows} -f {self.filename})"

    def __str__(self) -> str:
        return f"...writing {self.num_rows} number of rows to {self.filename}"

    def _random_to_file(self) -> None:
        def random_generator():
            for _ in range(self.num_rows):
                yield [
                    int(random.randint(1000, 9999)),
                    " " + "".join(random.choices(string.ascii_letters.lower(), k=12)),
                ]

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(random_generator())

    @staticmethod
    def _parser() -> ArgumentParser:
        parser = ArgumentParser()
        parser.add_argument(
            "-n", "--num_rows", default=10, type=int, help="Number of rows to generate"
        )
        parser.add_argument(
            "-f",
            "--filename",
            default="data.csv",
            type=str,
            help="Filename to use for CSV file",
        )
        return parser

    @staticmethod
    def format_num_rows(num_rows_obj: int) -> int:
        if isinstance(num_rows_obj, int):
            return num_rows_obj
        print(ERROR_NUM_ROWS)
        num_rows_obj = 10
        return num_rows_obj

    @staticmethod
    def format_filename(filename_obj: str) -> str:
        pattern = r"^[a-zA-Z]+[a-zA-Z0-9_\-]"
        filename_obj.strip()
        # Check if the file name matches the pattern
        match = re.match(pattern, filename_obj)
        if not filename_obj.endswith(".csv") and match:
            return filename_obj + ".csv"
        if filename_obj.endswith(".csv") and not match:
            print(ERROR_TEXT)
            filename_obj = "data.csv"
            return filename_obj
        if filename_obj.endswith(".csv") and match:
            return filename_obj
        print(ERROR_TEXT)
        filename_obj = "data.csv"
        return filename_obj


def main():
    args = CSVRandomDataGenerator._parser().parse_args()
    args.filename = CSVRandomDataGenerator.format_filename(args.filename)
    args.num_rows = CSVRandomDataGenerator.format_num_rows(args.num_rows)
    generator = CSVRandomDataGenerator(args.num_rows, args.filename)
    generator.formatter()
    generator._random_to_file()


if __name__ == "__main__":
    main()
