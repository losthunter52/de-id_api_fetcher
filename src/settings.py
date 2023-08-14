URL = "http://127.0.0.1:8000"

LOGIN_URL = "http://127.0.0.1:8000/login"

REGISTER_URL = "http://127.0.0.1:8000/register"


USERNAME = "username"
PASSWORD = "password"

RESULTS_PATH = "./tests/results/"

ERROR_SLEEP_TIME = 1

PAYLOAD_CONFIGURATION = {
"execution_parameters": [
        {
            "algorithm": "hash.md5",
            "columns": [
                "nome"
            ]
        },
        {
            "algorithm": "hash.sha1",
            "columns": [
                "sobrenome"
            ]
        },
        {
            "algorithm": "hash.sha256",
            "columns": [
                "email"
            ]
        }
    ]
}