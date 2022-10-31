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
        `cd git/f22_cis3760_team106online`
        `git pull`
        `$ sudo make production`
- To run the server in debug mode:
    - Run the following command: 

            `$ make debug_flask`
    - Open a new terminal and navigate to the '/web' directory
    - Run the following commands:

            `$ yarn install`
            `$ yarn start`

