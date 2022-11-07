## AdvisorLink

### Description

This is a prototype web server run using Flask, NGINX, React, Tailwind CSS, TypeScript, and hosted on Azure. This prototype will serve as the foundation for upcoming sprints. The homepage can be found at [advisorlink.ml](http://advisorlink.ml).

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
- To run the server in debug mode:
    - Run the following command: 

            `$ make debug_flask`
    - Open a new terminal and navigate to the '/web' directory
    - Run the following commands:

            `$ yarn install`
            `$ yarn start`

### To Create a Course Schedule
- On the Calendar page, you can search and add courses using the search bar at the top of the page.

        - Using the search bar, the user can search for courses by name, course code and professor
        - Results of the search will show up in the My Courses section of the page, which will show as a list of courses
        - When the user selects a course, the course will be automatically added to the calendar below the search bar
        - If there is a conflict, the user will be notified with a message above the calendar with the courses that are conflicting
