URL = "http://127.0.0.1:8000/anonymize"
LOGIN_URL = "http://127.0.0.1:8000/login"
REGISTER_URL = "http://127.0.0.1:8000/register"


USERNAME = "username"
PASSWORD = "password"


RESULTS_PATH = "./tests/results/"


ERROR_SLEEP_TIME = 1


PAYLOAD_CONFIGURATION = {
  "execution_parameters": [
    {
      "algorithm": "encrypt.chacha20",
      "configuration": {
        "key": "secret_key"
      },
      "columns": ["nome"]
    },
    {
      "algorithm": "encrypt.aes",
      "configuration": {
        "key": "secret_key"
      },
      "columns": ["sobrenome"]
    },
    {
      "algorithm": "encrypt.salsa20",
      "configuration": {
        "key": "secret_key"
      },
      "columns": ["sobrenome"]
    },
    {
      "algorithm": "generalize.percent",
      "columns": ["latitude"]
    },
    {
      "algorithm": "generalize.age",
      "columns": ["longitude"]
    },
    {
      "algorithm": "mask.cpf",
      "columns": ["cpf"]
    },
    {
      "algorithm": "mask.email",
      "columns": ["email"]
    },
    {
      "algorithm": "mask.full",
      "columns": ["rg"]
    },
    {
      "algorithm": "mask.first_n_characters",
      "configuration": {
        "n": 1
      },
      "columns": ["endereco"]
    },
    {
      "algorithm": "mask.last_n_characters",
      "configuration": {
        "n": 1
      },
      "columns": ["telefone"]
    },
    {
      "algorithm": "mask.range",
      "configuration": {
        "start_index": 1,
        "end_index": 3
      },
      "columns": ["anamnese"]
    },
    {
      "algorithm": "swap.rows",
      "columns": ["gender", "ip", "cidade", "estado"]
    },
    {
      "algorithm": "swap.columns",
      "columns": [
        "data_de_nascimento",
        "local_de_nascimento",
        "celular",
        "cartao_de_credito"
      ]
    },
    {
      "algorithm": "hash.md5",
      "columns": ["renda"]
    },
    {
      "algorithm": "hash.sha1",
      "columns": ["titulo_de_eleitor"]
    },
    {
      "algorithm": "hash.sha256",
      "columns": ["ra_exercito"]
    },
    {
      "algorithm": "pseudonymize.rows",
      "columns": ["nacionalidade", "plano_terapeutico"]
    },
    {
      "algorithm": "pseudonymize.columns",
      "columns": ["laudo_exames"]
    },
    {
      "algorithm": "null_out.columns",
      "columns": [
        "prescricao_medica",
        "evolucao_quadro_clinico",
        "trajetoria_clinica",
        "historico_pagamentos",
        "habitos_consumo",
        "preferencias_lazer",
        "origem_etnica",
        "religiao",
        "filiacao_politica",
        "orientacao_sexual",
        "biometria"
      ]
    }
  ],
  "sensitive_columns": [
    "nome",
    "sobrenome",
    "email",
    "gender",
    "ip",
    "endereco",
    "cidade",
    "estado",
    "rg",
    "cpf",
    "data_de_nascimento",
    "local_de_nascimento",
    "telefone",
    "celular",
    "latitude",
    "longitude",
    "cartao_de_credito",
    "renda",
    "titulo_de_eleitor",
    "ra_exercito",
    "anamnese",
    "laudo_exames"
  ],
  "diversity_columns": [
    "nome",
    "sobrenome",
    "email",
    "gender",
    "ip",
    "endereco",
    "cidade",
    "estado",
    "rg",
    "cpf",
    "data_de_nascimento",
    "local_de_nascimento",
    "telefone",
    "celular",
    "latitude",
    "longitude",
    "cartao_de_credito",
    "renda",
    "titulo_de_eleitor",
    "ra_exercito",
    "anamnese",
    "laudo_exames"
  ],
  "closeness_columns": [
    "nome",
    "sobrenome",
    "email",
    "gender",
    "ip",
    "endereco",
    "cidade",
    "estado",
    "rg",
    "cpf",
    "data_de_nascimento",
    "local_de_nascimento",
    "telefone",
    "celular",
    "latitude",
    "longitude",
    "cartao_de_credito",
    "renda",
    "titulo_de_eleitor",
    "ra_exercito",
    "anamnese",
    "laudo_exames"
  ]
}