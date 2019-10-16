HR
==

CLI for exporting users information

##Usage

This tools exports user information and saves it in  CSV or JSON format
Command will export names, IDs, home directories, and shells.
This command will include information about system users

Example:

```
$ hr --format=csv --path=path/to/users.csv
$ hr --path=path/to/users.json

```

 --format flag for csv as an alternative export type.
 --path flag can specify where to save the file

 ##Installation From Source
 To install package after you've cloned the epository, run the following coomand:

 ```

 pip install --user -e .

 ```

##Preparing for Development

Folow these steps to start developing with this project

1. Ensure 'pip' and 'pipenv' installed
2. Clone repository: 'git clone git@github.com:example/hr'
3. 'cd' into the repository
4. Activate virtualenv:  'pipenv shell'
5. Install dependencies: 'pipenv install'
