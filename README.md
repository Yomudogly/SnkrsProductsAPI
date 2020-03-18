# Load Tracking API

Load Tracking is a Flask + MongoDB API for dealing with tracking of time.

## Installation

Use the package manager [pipenv](https://github.com/pypa/pipenv) to install .

```bash
pipenv install

or

pip install -r requirements.txt
```

## Setup *.flaskenv* file

```python
FLASK_ENV=development

FLASK_APP=main.py

DB_CONNECTION_STRING=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/
<database-name>?retryWrites=true&w=majority

DB_NAME=<database-name>

SECRET_KEY=<super-secret>

ANOTHER_SECRET_KEY=<another-super-secret>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)