# Memories
A web-app that allow users to store their memories about certain places they have visited

### Main features

* User registration and logging in as demo

* Add memories to the page

* Bootstrap static files included

* SQLite by default 

# Usage

First activate the virtualenv for your project.

    $ python3 -m venv venv 
    $ source venv/bin/activate
    
Clone the repository from Github.

    $ git clone https://github.com/KienTruong123/Memories.git

Install project dependencies:

    $ pip install -r requirements.txt
    
Switch to the new directory:

    $ cd memories
    
Then simply make and apply the migrations:

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate 
    

You can now run the development server:

    $ python3 manage.py runserver 8000

Visit http://localhost:8000 ( ensure is not http://127.0.0.1:8000/ {Insecure Login Blocked by FB} )
