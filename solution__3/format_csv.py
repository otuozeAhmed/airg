import csv


def format_csv(
    input_file: str, output_file: str, delimiter: str = "|", quotechar: str = '"'
) -> None:
    # detects the delimeter & quotechar automatically
    if not delimiter and not quotechar:
        with open(input_file, "r") as input_csv:
            format = csv.Sniffer().sniff(input_csv.read(1024))
            delimiter = format.delimiter
            quotechar = format.quotechar
    # if one is provided only
    elif not delimiter:
        delimiter = "|"
    elif not quotechar:
        quotechar = '"'
    with open(input_file, "r") as input_csv:
        reader = csv.reader(input_csv, delimiter=delimiter, quotechar=quotechar)
        with open(output_file, "w", newline="") as output_csv:
            writer = csv.writer(
                output_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in reader:
                new_row = [
                    item.replace('"', '""') if "," in item else item for item in row
                ]
                writer.writerow(new_row)

def main():
    format_csv("input.csv", "output.csv", delimiter='|', quotechar='"')

if __name__ == "__main__":
    main()
