import sys
from argparse import Action, ArgumentParser

def get_arg_parser():
    parser = ArgumentParser(description='Search program that searches through the courses offered at the University of Guelph.', add_help=False)
    parser.add_argument('-name', default=None, type=str, help='course name eg. "Intro Financial Accounting"', nargs='+')
    parser.add_argument('-code', default=None, type=str, help='course code eg. ACCT1220')
    parser.add_argument('-faculty', default=None, type=str, help='faculty eg. ACCT')
    parser.add_argument('-credits', default=None, type=str, help='number of credits eg. 0.5')
    parser.add_argument('-level', default=None, type=str, help='eg. undergraduate, graduate')
    parser.add_argument('-term', default=None, type=str, help='eg. \'Fall 2022\'', nargs='+')
    parser.add_argument('-location', default=None, type=str, help='location of the course eg. Guelph')
    parser.add_argument('-building', default=None, type=str, help='building code eg. ROZH')
    parser.add_argument('-instructor', default=None, type=str, help='instructor name eg. P. Lassou', nargs='+')
    parser.add_argument('-year', default=None, type=str, help='year offered eg. 2022')
    parser.add_argument('-q', default=False, nargs='?', action=QuitAction)
    parser.add_argument('-h', default=False, nargs='?', action=HelpAction)
    return parser

# The action that is carried out when the user wants to quit the program
class QuitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('Exiting App')
        sys.exit(0)

# The action that is carried out when the user wants help with the program
class HelpAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('usage: Add filters by adding the following flags to your query:\n\n'
            '-h: help\n'
            '-q: quit\n'
            '-name: course name eg. ""Intro Financial Accounting""\n'
            '-code: course code eg. ACCT1220\n'
            '-faculty: faculty eg. ACCT\n'
            '-credits: number of credits eg. 0.5\n'
            '-level: course level eg. undergraduate, graduate\n'
            '-term: term offered eg. \'Fall 2022\'\n'
            '-location: location of the course eg. Guelph\n'
            '-building: building code eg. ROZH\n'
            '-instructor: instructor name eg. P. Lassou\n'
            '-year: year offered eg. 2022\n'
        )
