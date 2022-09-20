from argparse import ArgumentError
import os

# If importing from main, it is not run as part of the package, use absolute imports.
# If not, then its a part of the package, so import relatively,
if __name__ == "__main__":
    from utils import *
else:
    from .utils import *

# Helper function to make paths relative to this script instead of the directory
# from which it was run.
script_directory = os.path.dirname(os.path.abspath(__file__))
def relPath(path):
    return os.path.join(script_directory, path)

def main():
    parser = CourseJsonParser()
    sectionMap = parser.parse_json(relPath('../../config/courses.json'))
    print(
            'Welcome to the offline search tool for courses.\n\n'
            'usage: Add filters by adding the following flags to your query:\n\n'
            '-h: help\n'
            '-q: quit\n'
            '-name: course name eg. Intro Financial Accounting\n'
            '-code: course code eg. ACCT1220\n'
            '-faculty: faculty eg. ACCT\n'
            '-credits: number of credits eg. 0.5\n'
            '-level: course level eg. undergraduate, graduate\n'
            '-term: term offered eg. Fall 2022\n'
            '-location: location of the course eg. Guelph\n'
            '-building: building code eg. ROZH\n'
            '-instructor: instructor name eg. P. Lassou\n'
            '-year: year offered eg. 2022\n'
    )
    sections = []
    arg_parser = get_arg_parser()
    while (True):
        try:
            args = arg_parser.parse_args(input('\nQuery: \n').split())

            # Get all the section lists requested in the user query
            if args.name: sections.append(sectionMap.search(SearchOptionEnum.NAME, ' '.join(args.name)))
            if args.code: sections.append(sectionMap.search(SearchOptionEnum.CODE, args.code))
            if args.faculty: sections.append(sectionMap.search(SearchOptionEnum.FACULTY, args.faculty))
            if args.credits: sections.append(sectionMap.search(SearchOptionEnum.CREDITS, args.credits))
            if args.level: sections.append(sectionMap.search(SearchOptionEnum.LEVEL, args.level))
            if args.term: sections.append(sectionMap.search(SearchOptionEnum.TERM, ' '.join(args.term)))
            if args.location: sections.append(sectionMap.search(SearchOptionEnum.LOCATION, args.location))
            if args.building: sections.append(sectionMap.search(SearchOptionEnum.BUILDING, args.building))
            if args.instructor: sections.append(sectionMap.search(SearchOptionEnum.INSTRUCTOR, ' '.join(args.instructor)))
            if args.year: sections.append(sectionMap.search(SearchOptionEnum.YEAR, args.year))

            print()
            if len(sections):
                # Find the common set. O(min(n, m, o, ..)) where n, m , o are the lenghts of the different sections in the query
                filteredList = set.intersection(*sections)
                if len(filteredList) > 0:
                    print('Sections Found: \n\n')
                    for section in filteredList:
                        print(section)
                        print('---------------------------------')
                else:
                    print('No Sections met your criterias.')

                sections = []

        except ArgumentError:
            print('Argument error caught')

if __name__ == "__main__":
    main()
