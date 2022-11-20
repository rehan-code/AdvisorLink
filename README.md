## AdvisorLink

### Description

This is a prototype web server run using Flask, NGINX, React, Tailwind CSS, TypeScript, and hosted on Azure. This prototype will serve as the foundation for upcoming sprints. The homepage can be found at [www.advisorlink.ml](http://advisorlink.ml).

### Requirements

- Python3, node, yarn, Flask, gunicorn
- These requirements can be automatically installed with the Makefile or can be manually installed with:

            `$ sudo ./install.sh`

### Usage

- To run the production web server run:

        `$ ssh team106@advisorlink.ml`

        `$ cd git/f22_cis3760_team106online`

        `$ git pull`

        `$ sudo make production`

- If the PostgreSQL database is not running already you can start that with:

        `$ make db`

- To run the server in debug mode:

  - Run the following command:

          `$ make debug_flask`

  - Open a new terminal and navigate to the '/web' directory
  - Run the following commands:

          `$ yarn install`
          `$ yarn start`

### To Create a Course Schedule

On the home page, select the Schedule Courses button to begin creating a schedule.
        - First, use the drop down menu to choose between selecting F22 and W23 courses.
        - Using the search bar, the user can search for courses by name, course code and professor. Use the Search drop down menu to choose the desired criteria.
        - Results of the search will show up in the My Courses section of the page, which will show as a list of courses. The user can click on a course to see its lecture, lab and exam times.
        - Add a course using the + button on the desired section. When the user selects a course, it will be automatically added to the calendar below the search bar.
        - To remove a course, click the - button beside the course on the My Courses section.
        - If there is a conflict, the conflicted section will be coloured red.
        - To switch to the exam schedule, press the Switch to Exam Schedule button below the calendar.
        - To export the file, click the Export file below the calendar.
