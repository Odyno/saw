"""
Entry point for the CLI application.

"""
import argparse
import sys
import logging
from dotenv import load_dotenv

from commands import do_dummy, do_env



class CommandLineParser:

    parser = argparse.ArgumentParser(description="Dummy Descriptions")
    args = None

    def __init__(self):
        commands = self.parser.add_subparsers(title="commands", dest="command", help="All possible commands are:")
        
        #######################------
        dummy_command=commands.add_parser('dummy', help='[deprecated] Dummy')
        
        #######################------
        env_command=commands.add_parser('env', help='Print all environment variables')
        env_command.add_argument('-a', '--all',  type=str, help='Dummy All', required=True)
                
        self.args = vars(self.parser.parse_args())

    def is_command(self,command:str) -> bool :
        return self.get('command') == command
        
    def get(self,arg, default = None) :
        out = self.args.get(arg)
        if not out and default:
            out=default
        return  out
    
    def print_help(self):
        self.parser.print_help()




def main():
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s",
                        level=logging.DEBUG,
                        handlers=[
                            logging.FileHandler(
                                "./run.log", mode='a', encoding=None, delay=False),
                            logging.StreamHandler(sys.stdout)
                        ]
                        )
    logging.debug("-----------------------------------")

    load_dotenv(".env_defaults")  # take Defaults
    load_dotenv()                   # Take environment variables if exists

    clp = CommandLineParser()

    # Define a dictionary mapping commands to their corresponding functions and arguments
    commands = {
        'dummy': (do_dummy, []),
        'env': (do_env, ['all']),
        
    }

    for command, (func, args) in commands.items():
        if clp.is_command(command):
            try:
                func(*(clp.get(arg) for arg in args))
            except Exception as e:
                print(f"An error occurred while executing {command}: {e}")
            break
    else:
        logging.error(f"An error occurred while executing")


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    main()
