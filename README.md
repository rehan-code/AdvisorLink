## AdvisorLink

### Description

This is a prototype web server run using Flask, NGINX, React, Tailwind CSS, TypeScript, and hosted on Azure. This prototype will serve as the foundation for upcoming sprints. The homepage can be found at [advisorlink.ml](advisorlink.ml).

### Requirements
- Python3, node, yarn, Flask, gunicorn
- These can be manually installed with:

            `$ sudo ./install.sh`

### Usage
- Use "sudo make production" to run the web server using gunicorn
- To run the server in debug mode
    - Run the following command: 

            `$ make debug_flask`
    - Open a new terminal and navigate to the '/web' directory
    - Run the following commands:

            `$ yarn install`
            `$ yarn start`
            