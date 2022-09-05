import sys
import cli
from settings import the

if __name__ == '__main__':
    cli_opts = cli.CLI()
    args, args_vals = cli_opts.parse_user_arguments(sys.argv)
    theObj = the()
    theObj.change_user_settings(args, args_vals)
    print(str(theObj))
    
