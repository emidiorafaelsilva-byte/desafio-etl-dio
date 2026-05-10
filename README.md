# Desafio ETL - DIO

Projeto desenvolvido para demonstrar um pipeline ETL utilizando Python e Pandas.

## Objetivo

O projeto realiza:

- Extract → leitura de dados CSV
- Transform → tratamento e enriquecimento dos dados
- Load → geração de uma nova planilha Excel

---

## Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- CSV
- Excel

---

## Estrutura do projeto

```bash
desafio-etl-dio/
│
├── SDW2023_clientes.csv
├── clientes_transformados.xlsx
├── etl.py
├── requirements.txt
└── README.md
```

---

## Processo ETL

### Extract

Leitura do arquivo CSV contendo informações de clientes bancários.

### Transform

Foram realizadas transformações como:

- classificação de clientes por saldo
- criação de mensagens personalizadas
- enriquecimento dos dados

### Load

Os dados transformados foram exportados para um novo arquivo Excel:

```bash
clientes_transformados.xlsx
```

---

## Como executar o projeto

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar pipeline

```bash
python etl.py
```

---

## Resultado

O pipeline gera automaticamente um novo arquivo Excel contendo os dados transformados.

---

## Autor

Rafael Emidio
