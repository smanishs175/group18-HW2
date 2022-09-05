"""" 
    Helper class for parsing arguments
"""
import sys


class CLI:

    def __init__(self):
        self.allowed_args = {'-d', '-e', '-f', '-h', '-n', '-s', '--eg', '--dump', '--file', '--help', '--nums',
                             '--seed'}

    def parse_user_arguments(self, args):

        arguments = []
        arguments_values = []

        # --help is an exception as we only show help and don't take input, so we process it first
        if '-h' in args or '--help' in args:
            showHelp()
            args.remove("-h" if '-h' in args else "--help")

        # odd indexes are cli options and even indexes are there corresponding values.
        # we ignore the first index as it will be the filename.
        for i in range(1, len(args)):
            if i % 2 == 0:
                arguments_values.append(args[i])
            else:
                arguments.append(args[i])

        self.validate_user_input(arguments, arguments_values)
        return arguments, arguments_values

    def validate_user_input(self, input_arg_list, input_val_list):

        if len(input_arg_list) != len(input_val_list):
            sys.exit("The input arguments are not correct, please check!")

        for argument in input_arg_list:
            if argument not in self.allowed_args:
                sys.exit(f"{argument} is not valid, please check!")


def showHelp():
    helper_string = """
    CSV : summarized csv file

    USAGE: python3 csv.py [OPTIONS]

    OPTIONS:
    −e −−eg start−up example = nothing
    −d −−dump on test failure, exit with stack dump = false
    −f −−file file with csv data = ../data/auto93.csv
    −h −−help show help = false
    −n −−nums number of nums to keep = 512
    −s −−seed random number seed = 10019
    """
    print(helper_string)
