from argparse import ArgumentParser, Action

class FormatType(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        file_format = values
        namespace.file_format=file_format
        #namespace.destination = destination

def create_parser():
    parser = ArgumentParser("""
    Exporting user user names, IDs, home directories, and shells into CSV or JSON format
    Example:
    hr --format=csv --path=path/to/users.csv
    """)
    parser.add_argument("--format",
            help="Choose CSV or JSON format",
            nargs=1,
            action=FormatType,
            required=False)
    parser.add_argument("--path",help="destination to save the file")
    return parser
