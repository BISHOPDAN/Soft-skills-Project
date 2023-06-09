# Soft Skill Space

An educational platform to facilitate both tutoring and online courses

## Useful links

- [Gitlab repo](https://gitlab.com/ecclesit/softskillspace)
- [Theme](https://eduport.webestica.com/index.html)

## Requirements

- Python / Django

## Project setup

If not using docker, you can setup a virtual environment using the command below

```sh
python -m venv env
```

then activate it with

```sh
./env/Scripts/activate   # windows or
source env/bin/activate  # linux or mac
```

## Install required packages

Run the command below

```sh
python -m pip install -r requirements-dev.txt
```

Once the virtual environment has been activated, install the necessary requirements by using the command below

```sh
python manage.py migrate
```

##  Setting up default data

Run the code to pre-populate your database with default data

```sh
python manage.py loaddata ./softskillspace/fixtures/subject.json

python manage.py loaddata ./softskillspace/fixtures/location.json
```

## Database backups and restore

Sometimes you may want to delete your database but don't want to lose your data. To do this, run the following script

## Backup command

```sh
python -Xutf8 manage.py dumpdata --natural-primary --exclude=contenttypes --exclude=auth.permission --exclude=admin.logentry --exclude=sessions.session > ../data.json
```

## Restore command

```sh
python manage.py loaddata ../data.json
```


## Important steps

### Pre development
- Go to the GitLab issue board (https://gitlab.com/ecclesit/softskillspace/-/boards/4073022)
- In the backlog lane, choose a ticket an assign to yourself
- Move the chosen ticket to in progress
- Create a branch in your local pc but branching from the develop branch.

```sh
# switches to develop branch
git checkout develop

# get latest and updated changes
git pull

# create a new branch from the develop branch
git checkout -b SSS-1/lowercased-short-description
```

### Dev complete
- Once coding is done, run the commands

- run the `scripts.sh` script. (skip for now unless you know what you are doing)
- Alternatively, you can manually run the commands below

```sh
pylint $(git ls-files '*.py')
flake8
python manage.py test --keepdb -v 2
```

Ensure that

-
```sh
git add .
git commit -m "<ticket-no>: short description of what change you made"
git push -u origin <branch-name>
```

- If successful, `git push` your code to Gitlab
- Create a merge request using the link generated from the terminal

- Notify two colleagues to perform code reviews on the slack channel
- If code review is successful, merge to develop and move ticket to `closed` lane on Gitlab

## Contribution

Pick a ticket on the [Gitlab repository](https://gitlab.com/ecclesit/softskillspace). If you haven't cloned the repository, use the command to clone from the terminal

```sh
git clone https://gitlab.com/ecclesit/softskillspace
```

When creating a new branch, **ENSURE** that the branch name starts with the format **SSS-&lt;issue-no&gt;-&lt;short-description&gt;** e.g. **SSS-1-project-setup** and the main branch is from develop. use the command below when creating a new branch.

```
git checkout develop
git branch -b <branch name>
```

Before creating a pull request, run the commands and fix any warning/errors encountered

```
sh ./scripts.sh

git add .
git commit -m "my commit message"
git push -u origin <branch name>
```

> **Note:** You will need to have isort, autopep8, black and pylint installed for this to work and you can install it using the commands below.

```sh
python -m pip install autopep8 pylint isort black
```

When creating a pull request, please select the target branch as `develop`.

- After writing your code, make sure to run the `scripts.sh` file and **ENSURE** it passes before pushing to the git repository. Use the command below to run the test.

```sh
sh ./scripts.sh
```

## Pushing to the repository

Run the following command

```sh
 # if pushing for the first time
$ git push -u origin <branchname>

# if pushing normally
$ git push
```

## Installing make

```sh
# Install make on windows
choco install make

# Linux or mac
sudo apt install make
```

## Using make command

* Export database content as json for backup purposes

```sh
make backup
```

* Creates a virtual environment in current working directory

```sh
make env
```

* Fixes your database if it gets corrupted. Creates a backup and also restore current data

```sh
make fixdb
```

* Displays help text on how to use the makefile

```sh
make help
```

* Syncs the project dependencies

```sh
make install
```

* Checks if code is conforming to best practices like PEP8

```sh
make lint
```

* Runs makemigrations and migrate commands

```sh
make migrate
```

* Pushes committed changes to the Gitlab remote repository

```sh
make push
```

* Loads previously backed up data into the database

```sh
make restore
```

* Spawns the Django server

```sh
make server
```

* Runs unit test

```sh
make test
```

* Syncs the project dependencies

```sh
make update
```
