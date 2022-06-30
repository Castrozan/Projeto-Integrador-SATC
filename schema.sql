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

CREATE TABLE relatorios (
    id_relatorios INTEGER PRIMARY KEY AUTOINCREMENT,
    notas_geracao TEXT NOT NULL,
    min_geracao TEXT NOT NULL,
    presente_geracao TEXT NOT NULL,
    max_geracao TEXT NOT NULL,
    notas_inversor TEXT NOT NULL,
    min_inversor TEXT NOT NULL,
    presente_inversor TEXT NOT NULL,
    max_inversor TEXT NOT NULL,
    notas_mppts TEXT NOT NULL,
    notas_tensao_mppt1 TEXT NOT NULL,
    min_mppt1 TEXT NOT NULL,
    presente_mppt1 TEXT NOT NULL,
    max_mppt1 TEXT NOT NULL,
    notas_corrente_mppt1 TEXT NOT NULL,
    notas_tensao_mppt2 TEXT NOT NULL,
    min_mppt2 TEXT NOT NULL,
    presente_mppt2 TEXT NOT NULL,
    max_mppt2 TEXT NOT NULL,
    notas_corrente_mppt2 TEXT NOT NULL,
    notas_tensao_mppt3 TEXT NOT NULL,
    min_mppt3 TEXT NOT NULL,
    presente_mppt3 TEXT NOT NULL,
    max_mppt3 TEXT NOT NULL,
    notas_corrente_mppt3 TEXT NOT NULL,
    notas_tensao_mppt4 TEXT NOT NULL,
    min_mppt4 TEXT NOT NULL,
    presente_mppt4 TEXT NOT NULL,
    max_mppt4 TEXT NOT NULL,
    notas_corrente_mppt4 TEXT NOT NULL
);