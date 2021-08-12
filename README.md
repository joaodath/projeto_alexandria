# Alexandria (The Project)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/joaodath/projeto_alexandria)
[![Lines of Code](https://img.shields.io/tokei/lines/github/joaodath/projeto_alexandria)](https://img.shields.io/tokei/lines/github/joaodath/projeto_alexandria)
[![Number of Files](https://img.shields.io/github/directory-file-count/joaodath/projeto_alexandria)](https://img.shields.io/github/directory-file-count/joaodath/projeto_alexandria)
[![Repo Size](https://img.shields.io/github/repo-size/joaodath/projeto_alexandria)](https://img.shields.io/github/repo-size/joaodath/projeto_alexandria)

A full-fledged online library manager based on Python, HTML, CSS and JS.

Alexandria is a tribute to the original Library of Alexandria, destroyed by 
those whom feared open knowledge. 

<div align='center'>
<img  src="alexandria/frontend/static/img/logo/alexandria_logo.svg" width='300px' style='display: flex; justify-content: center'>
</div>

## Main Goal
To develop a full-fledged online library manager and a community of readers 
interested in sharing what they're reading now but also to keep account 
of what they've read already. 

Alexandria is meant to be always open-source, free to use and free to modify. 
Right now, we're in dev stage squashing bugs and creating new features. 
If you want to check out how we're doing so far, you're welcome to try it. 
You can also help us fixing bugs, suggesting and creating new features as well 
as improving existing ones.

## Get Involved

### Trying Alexandria before release
You may want to try Alexandria before it reaches a stable release, if that's 
the case, we welcome you. Follow the instructions below to do so.

**Here's what you'll need to do:**
- Clone this repository
- Download the dependencies
- Set up a database for Alexandria
- Run!


#### Clone this repository
If you're here, we will assume you already have Git installed and know 
how to deal with it. You just need to run the code below to clone this repo:

```
git clone https://github.com/joaodath/projeto_alexandria.git
```

#### Download the dependencies

Then, you'll need to install our dependencies. It's pretty easy! We will 
assume you already have the latest Python installed on your machine 
(that will be 3.9.6) but if you need help, you can [click here](link) and 
will guide you through the process.

We designed Alexandria to rely on minimal dependencies but we still need some. 
To download and install them is just as quick as Ctrl+C + Ctrl+V.

##### Windows
Open the folder where you've cloned this repository, 
use the combo Shift + right-click anywhere and choose "Open CMD here" option. 
Newer Windows versions will show "Open PowerShell here", it's fine.
After that, copy and paste the following command and press enter if needed.

```
python -m pip install -r requirements.txt
```

##### Linux-based systems
Open the folder where you've cloned this repository, right-click anywhere and 
choose the "Open on Terminal" option. 
After that, copy and paste the following command and press enter if needed.

```
python3.9 -m pip install -r requirements.txt
```

#### Set up a database for Alexandria
For tests purposes, 
we will use a PostgreSQL managed database on ElephantSQL.com. 
They have a very nice documentation that you can use to get started. 
[Click here to see their docs.](https://www.elephantsql.com/docs/)

After you have set up a database, you must copy the URI and paste it 
inside the file config.py where it reads:

```
SQLALCHEMY_DATABASE_URI = os.getenv[DATABASE_URI]
```
Yours should look like this:
```
SQLALCHEMY_DATABASE_URI = 'postgresql://yclpqsad:8a4LgQpctwTio0jipae_zPbJabcx4lFg@kesavan.db.elephantsql.com/yclpqsad'
```
After that, open a new terminal inside the folder you've clonned this 
repository and run the following commands one after the other 
(they will initialize the database):

- **Windows:**
```
python app.py db init
python app.py db migrate
python app.py db upgrade
```
- **Linux-based systems:**
```
python3.9 app.py db init
python3.9 app.py db migrate
python3.9 app.py db upgrade
```

#### Run!
Now it's time to run! The code, we mean.
Run this command on the same terminal window and it should display 
the URL of your local copy of Alexandria.

- **Windows:**
```
python app.py runserver
```

- **Linux-based systems:**
```
python3.9 app.py runserver
```

### Improve Alexandria

You want to help us make Alexandria better? That's awesome! 
Here is what you can do.

#### Code with us
If you know how to code and want to help, you can fork our project and start 
working on your fork. Once you're done, create a pull request and 
we will check your code!

**Keep it in mind:**
- A great way to start coding Alexandria is to check the open issues and see 
if there's anything there you can help us.

- Commit your changes with nice messages. Commits with 'minor changes' 
comments are not nice. Instead, tell us what you did on your commit. 
A better commit message would be something more specific like
 'changed the PostgreSQL driver'.

- Always work from the release-candidate branch and your pull request must 
always be to release-candidate. No pull requests directly 
to main will be allowed.

- If you're working on a patch for a security breach you found, use the 
methods we provide on our Security Policy (SECURITY.md) 
to disclose the breach securely.

#### Talk to us!
If you don't know how to code and you found a bug or perhaps you want to 
request a feature or an improvement for an existing one, 
you can always open an issue. 

**Keep it in mind:**

- **Avoid duplicates.** Before opening an issue, search the previous ones 
to see if it has been talked about before. If that's the case, 
don't create a duplicate. Instead, comment on the issue already open.

- When you open an issue, everything you say there will be publicly available. 
Try not to share any personal data and if you believe that the issue you want 
to open is about a security breach, do not open an issue. 
Instead, use the protocol set in place in SECURITY.md.

- When you open an issue, a template will be available to help you organize 
your ideas better.

- Last but not least, try to be nice when opening an issue. 
This is an open source project, nor we nor the other contributors 
are paid to code for Alexandria, be polite when you talk to us. ;)

## Help
##### Installing Python
This project was created using Python v3.9.6 as a programming language.
You may use down to Python v3.6 but we strongly recommend a newer version.
Python v3.5 or below is not supported since we use the `f-string` String
Formatting Syntax available only on Python v3.6 and newer. 
We provide info as how to install Python on Windows and Ubuntu. 
Support for bugs will only be available for installations with Python v3.9.5+.

##### Windows
If you're on Windows, you can head to Python's download page to download an
executable (.exe) for quick installation. Choose the latest version.
[Click here](https://www.python.org/downloads/windows/) to download Python.


##### Linux-based systems
We'll show how to download and install Python on Ubuntu OS. The instructions
for other systems might be similar.

* Install  the `deadsnakes` PPA to get the latest Python available
```
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

* Install Python 3.9
```
$ sudo apt-get update
$ sudo apt-get install python3.9
```

## The team behind

- [Thaynar Brandão](github.com/thaynar96)
- [João Rodrigues](github.com/joaodath)
- [Felipe Menezes](github.com/menezesfelipee)
- [Fábio Araujo](github.com/fharaujo)
- [Bianca Monteiro Corrêa](github.com/Bianca-22)