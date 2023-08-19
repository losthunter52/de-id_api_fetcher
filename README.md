
# Anonymizer API Fetcher

Configure ./src/settings.py:

```bash
  [...]
  URL = "http://127.0.0.1:8000/anonymize"
  LOGIN_URL = "http://127.0.0.1:8000/login"
  REGISTER_URL = "http://127.0.0.1:8000/register"


  USERNAME = "username"
  PASSWORD = "password"

  [...]
```

On the root of the repository run:

```bash
  [...]
    cd de-id
    python -m venv venv
    venv/scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python .\fecth_results.py -a .\tests\datasets\1kB_100objects_dataset.json -p 5
  [...]
```

