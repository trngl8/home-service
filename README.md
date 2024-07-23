# home-service

This is a simple Flask app for home-service company

## Requirements

- Python 3.x
- Flask

## Installation

```bash
   git clone https://github.com/trngl8/home-service.git
   cd your-repository
```

After that create the virtual environment:

- On macOS/Linux:

```bash
    python3 -m venv venv
    source venv/bin/activate
```
- On Windows: 

```bash
    python -m venv venv
    venv\Scripts\activate
```

Then install the reuqired packages: 

```bash
    pip install -r requirements.txt
```

In order to run the app you need to do the following in the command line: 

```bash
    flask --app index run
```

The application will be available at  local host http://127.0.0.1:5000.

To run the tests enter the following in the command line:

```bash
    python3 -m unittest discover -s tests
```
