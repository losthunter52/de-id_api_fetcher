URL = "http://127.0.0.1:8000"

RESULTS_PATH = "./tests/results/"

ERROR_SLEEP_TIME = 1

PAYLOAD_CONFIGURATION = {
    "params": [
        {
            "tool": "nulling_out",
            "fields": [
                "nome"
            ]
        },
        {
            "tool": "swapping",
            "fields": [
                "sobrenome"
            ]
        },
        {
            "tool": "masking",
            "fields": [
                "rg",
                "data_de_nascimento",
                "local_de_nascimento",
                "endereco"
            ]
        },
        {
            "tool": "perturbation",
            "config": {
                "method": "number_variation",
                "variation": 10,
                "jump": 1,
                "decimal_places": 2
            },
            "fields": [
                "latitude"
            ]
        },
        {
            "tool": "perturbation",
            "config": {
                "method": "random_number_variation",
                "variation": 10,
                "jump": 1,
                "decimal_places": 2
            },
            "fields": [
                "longitude"
            ]
        },
        {
            "tool": "masking",
            "config": {
                "method": "positional",
                "initial_rage": 3,
                "final_range": 10
            },
            "fields": [
                "gender",
                "ip",
                "cidade",
                "estado",
                "telefone"
            ]
        },
        {
            "tool": "masking",
            "config": {
                "method": "right_to_left",
                "length": 5,
                "mask_result_lenght": False
            },
            "fields": [
                "anamnese",
                "plano_terapeutico",
                "laudo_exames",
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
        },
        {
            "tool": "masking",
            "config": {
                "method": "left_to_right",
                "length": 5,
                "mask_result_lenght": True
            },
            "fields": [
                "celular",
                "renda",
                "titulo_de_eleitor",
                "cartao_de_credito",
                "ra_exercito",
                "nacionalidade"
            ]
        },
        {
            "tool": "masking",
            "config": {
                "method": "cpf",
                "masked": False
            },
            "fields": [
                "cpf"
            ]
        },
        {
            "tool": "masking",
            "config": {
                "method": "email"
            },
            "fields": [
                "email"
            ]
        }
    ],
}