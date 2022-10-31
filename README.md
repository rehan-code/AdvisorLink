## AdvisorLink

### Description

This is a prototype web server run using Flask, NGINX, React, Tailwind CSS, TypeScript, and hosted on Azure. This prototype will serve as the foundation for upcoming sprints. The homepage can be found at [advisorlink.ml](http://advisorlink.ml).

### Requirements
- Python3, node, yarn, Flask, gunicorn
- These requirements can be automatically installed with the Makefile or can be manually installed with:

            `$ sudo ./install.sh`

### Starting and Restarting Server
- The Azure servers are setup using docker containerized images
- To build the images and upload them to the Gitlab Container Registry run:

            `$ make build_images`
- To deploy the images to the Azure server, we trigger a webhook telling the server to pull the latest images by running:

            `$ make deploy_images`

### Usage
- To run the production web server on the currently logged in computer run:

        `$ sudo make production`
- To run the server in debug mode:
    - Run the following command: 

            `$ make debug_flask`
    - Open a new terminal and navigate to the '/web' directory
    - Run the following commands:

            `$ yarn install`
            `$ yarn start`

