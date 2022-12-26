# Commands

- python -m pip --version
- pip list
- pip install virtualenv

### Activate venv : From inside the project folder(fastapi-learnings)
- python -m venv fastapienv
- . fastapienv/bin/activate

### Installing dependencies for FASTAPI
- pip install fastapi
- pip install uvicorn
  - or
- pip install fastapi uvicorn

### Start the app
- uvicorn books:app --reload
- http://127.0.0.1:8000/
- swagger docs : http://127.0.0.1:8000/docs
- openapi.json : http://127.0.0.1:8000/openapi.json
- 
