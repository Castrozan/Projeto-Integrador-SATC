DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS modulo;
DROP TABLE IF EXISTS inversor;


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
    quantidade TEXT NOT NULL,
    potencia TEXT NOT NULL
);

CREATE TABLE inversores (
    id_inversores INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modelo TEXT NOT NULL,
    quantidade TEXT NOT NULL,
    potencia TEXT NOT NULL
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