DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS modulo;
DROP TABLE IF EXISTS inversor;
DROP TABLE IF EXISTS arranjos;


CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE modulos (
    id_modulos INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modelo TEXT NOT NULL,
    potencia TEXT NOT NULL,
    tensao TEXT NOT NULL,
    corrente TEXT NOT NULL
);

CREATE TABLE inversores (
    id_inversores INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modelo TEXT NOT NULL,
    potencia TEXT NOT NULL,
    tensao_max TEXT NOT NULL,
    tensao_min TEXT NOT NULL,
    corrente TEXT NOT NULL,
    mppts TEXT NOT NULL,
    quantidade TEXT NOT NULL
);

CREATE TABLE arranjos (
    id_arranjos INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    numero_total_modulos TEXT NOT NULL,
    num_strings_mppt1 TEXT NOT NULL,
    mod_strings_mppt1 TEXT NOT NULL,
    azimute_mppt1 TEXT NOT NULL,
    inclinacao_mppt1 TEXT NOT NULL,
    num_strings_mppt2 TEXT NOT NULL,
    mod_strings_mppt2 TEXT NOT NULL,
    azimute_mppt2 TEXT NOT NULL,
    inclinacao_mppt2 TEXT NOT NULL,
    num_strings_mppt3 TEXT NOT NULL,
    mod_strings_mppt3 TEXT NOT NULL,
    azimute_mppt3 TEXT NOT NULL,
    inclinacao_mppt3 TEXT NOT NULL,
    num_strings_mppt4 TEXT NOT NULL,
    mod_strings_mppt4 TEXT NOT NULL,
    azimute_mppt4 TEXT NOT NULL,
    inclinacao_mppt4 TEXT NOT NULL
);

CREATE TABLE consumo_anual (
    id_consumo_anual INTEGER PRIMARY KEY AUTOINCREMENT,
    escola TEXT NOT NULL,
    janeiro TEXT NOT NULL,
    fevereiro TEXT NOT NULL,
    marco TEXT NOT NULL,
    abril TEXT NOT NULL,
    maio TEXT NOT NULL,
    junho TEXT NOT NULL,
    julho TEXT NOT NULL,
    agosto TEXT NOT NULL,
    setembro TEXT NOT NULL,
    outubro TEXT NOT NULL,
    novembro TEXT NOT NULL,
    dezembro TEXT NOT NULL
);