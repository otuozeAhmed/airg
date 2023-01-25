Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You will need to have the following installed:

- make - https://www.gnu.org/software/make/
- Docker - https://www.docker.com/products/docker-desktop/

This project requires **Docker 17.06+ CE**. 
The current Docker version used for this project is **Docker 20.10.22 CE** 
I recommend Docker Stable, butDocker Edge should work as well.

**NOTE:** Switching between Docker Stable and Docker Edge will remove all images and
settings.  Don't forget to restore your memory setting and be prepared to
provision.

For macOS users, please use `Docker for Mac`_. Previous Mac-based tools (e.g.
boot2docker) are *not* supported. 


Please note
~~~~~~~~~~~

1. You should run all ``make`` commands described below on your local machinge, *not*
from within a Virtual Machine, as these commands are meant to stand up a VM-like environment using
Docker containers.
2. Ensure to append ``sudo`` to all commands if your Docker permission configs is not properly set
Or if you always require sudo to execute docker commands 

Directions to setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone this project or downloadthe zip file. You may also run online with Gitpod - 
Get Gitpod here - https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki


Start the project. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make start

    This will also install all the required packages for this project.

Solution - 1: Use this command to see results of question 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make fetch.api

Solution - 2: Use these commands to see results of question 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make generate.random.data (without parametera)
       make generate.random.data n=100 f=sample.csv (with parameters)
       make generate.random.data n=100 f=sample (without extension: will append .csv automatically)
       make generate.random.data n=high f=0-=23.csv (with incorrect parameters: will use default values)
       
   Note: Running this solution without parameters will use default values.
         (n=number of rows, f=filename). Pass without spaces...
         filename provided is generated in solution__2 folder

Solution - 3: Use this command to see results of question 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make format.csv
       
(note: output file is generated in solution__3 folder "output.csv" )

Use this command to show logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make show-logs

Use this command to manually install requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make requirements

Use this command to top all running containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       make stop


Alternatively,you can still run this project on your PC (e.g. Windows) if you don't have
WSL installed or make and/or Docker - You must have Python3.4+ already installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       pip -m venv venv
       
note: For Linux & Mac: use pip3 if you receive an error using ordinary pip

Activate it
~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       source venv/bin/activate - Linux & Mac
       source venv/Scripts/activate - Windows (you must have Git installed to use source on Windows)
       
Download the requirements file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       pip install -r requirements.txt
       source venv/Scripts/activate - Windows (you must have Git installed to use source on Windows)

 Note before you run the solution file: 
    use python3 - Linux & Mac if you don't already have na alias using python
    python - Windows default

Run Solution - 1 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       cd solution__1 && python fetch_data.py

Run Solution - 2 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    note: Return to the root directory before you run solution 2 & 3

   .. code:: sh

       cd solution__2 && python random_data_gen.py -n 200 -f file.csv (with parameters)
       cd solution__2 && python random_data_gen.py (without parametera)
       cd solution__2 && python random_data_gen.py -n 50 -f data (without extension: will append .csv automatically)
       cd solution__2 && python random_data_gen.py -n code -f =--12- (with incorrect parameters: will use default values)

(note: -n = number of rows, -f = filename)

Run Solution - 3 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       cd solution__3 && python format_csv.py

Run the tests for solution - 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code:: sh

       cd solution__2 && python tests.py