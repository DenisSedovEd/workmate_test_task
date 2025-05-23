from argparse import ArgumentParser

from controller import controller


def main() -> None:
    parser = ArgumentParser("main")
    parser.add_argument("-f", "--file", nargs="+")
    parser.add_argument("-r", "--report", nargs="?")
    args = parser.parse_args()
    list_of_files = args.file
    report_name = args.report
    controller(list_of_files, report_name)


if __name__ == "__main__":
    main()
