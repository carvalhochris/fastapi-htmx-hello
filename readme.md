Clone repo

```
git clone https://github.com/carvalhochris/fastapi-htmx-hello.git
cd fastapi-htmx-hello
```

Create virtual env

```
python3 -m venv env
```

Activate virtual env

```
source env/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run

```
uvicorn main:app --reload --port 8001
```