# F22_CIS3760_Team106online

## Name

University of Guelph Course Scheduling Applications


## Course Schedule Spreadsheet

### Description

This Spreadsheet allows students to be able to generate a course schedule based on a selected course list.
Users can also receive course suggestions based on preferences such as what time of day a course is preferred, what day lectures are on, etc.

### Requirements
- Requires Microsoft Excel with macros enabled.

### Usage

#### Course Selection Scheduling Sheet
- All course information can be viewed on the `courses` sheet.
- The user can then select the courses they are taking in the `course selector` sheet by adding the appropriate course codes under the `Course Code` column and then press the `Create Schedule` button.
- This fills in the `schedule` and `selected courses` sheets. The `schedule` sheet now provides a calendar view of the appropriate meeting times for the courses. The `selected courses` sheet now shows the course information of only the selected courses of the user.
- The `course list` sheet contains a list of information on all the available courses offered by the University of Guelph.

#### Course Suggestion Engine
- The suggestion engine is found on the `course selector` page.
- The user fills out their course codes under the `Course Code` column and presses the `Search Sections` button as usual
- To select the criteria for the selection engine, the user uses the `Suggestion` table to the right of the button. The user can get suggested courses using one of two criteria:

     1. `Time of Day` (`Morning`, `Afternoon` or `Evening`)
     2. `Free Day` (User can find sections corresponding to selected days of the week)
- The user uses the `Suggest Sections` button to show courses that fit the user's criteria.
- The suggested courses will appear in the `Course Code` column and on the course schedule.


## Course Search CLI

### Description

Allows users to search through a course by name, code, location, exam, etc.
The script uses the `courses.json` file located in `src/config` to generate all of the search results.
If one wants to regenerate the `courses.json` file they will need to run the `course_parser` with the steps below on the following application.

### Requirements
- Requires python3 to be installed.
- Requires `src/config/courses.json` to exist to search for courses.

### Usage
- Run `make search_cli` or `python src/scripts/course_search` to run the application.
- Once in the CLI, you can begin inputting queries of courses to find, such as `-name Introductory Microeconomics` 
- Queries can be combined to narrow down course searches even more. eg: `-name Introductory Microeconomics -instructor P. Martin`
- When a search is made, a list of courses matching those parameters will be outputted and another query will be prompted for
- Enter the `-q` command to exit the program or `-h` to receive a help display showing the available options.


## Course HTML Parser 

### Description

This script parses an HTML file `courses.html` within `src/config` that contains University of Guelph course details into a node hierarchical structure.
This node structure is then converted into a JSON dictionary list containing information regarding each course and section offered at the University of Guelph.
This generated JSON is then stored at `courses.json` in `src/config`.
A `courses.csv` is also created containing a comma-delimited list of all courses with their information.

### Requirements
- Requires python3 to be installed.
- Requires the `jsonschema` package to be installed. This can be done with `pip install jsonschema`.
- Requires `src/config/courses.html` to exist to parse courses.

### Usage
- Run `make course_config` or `python src/scripts/course_parser` to run the script.
- The script will then output each of the steps made while parsing the HTML file, and output `courses.json` and `courses.csv` files in `src/config`.


## Authors and acknowledgment
- Hyrum Nantais
- Muhammad Salmaan
- Alif Merchant
- Ivan Odiel Magtangob
- Caleb Beere
- Rehan Nagoor Mohideen
- Samuel Guilbeault
- Parker Carnegie
