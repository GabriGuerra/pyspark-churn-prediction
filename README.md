# PySpark Churn Prediction Project / Projeto PySpark de Predição de Cancelamento

[![Python Version](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/release/python-3120/)
[![PySpark Version](https://img.shields.io/badge/pyspark-4.0.1-orange)](https://spark.apache.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

---

## English

This project performs a basic load and analysis of the churn dataset using PySpark.

### How to use

1. Install Java 8 and Apache Spark 3.5.1 and configure the environment variables `JAVA_HOME` and `SPARK_HOME`.
2. Setup Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Download the dataset `churn-bigml-20.csv` into the `data/` folder:

```bash
wget https://raw.githubusercontent.com/bensadeghi/pyspark-churn-prediction/master/data/churn-bigml-20.csv -P data/
```

4. Run the main script:

```bash
python src/main.py
```

---

## Portuguese (Português)

Este projeto realiza a carga e análise básica do dataset de churn (cancelamento) usando PySpark.

### Como usar

1. Instale Java 8 e Apache Spark 3.5.1 e configure as variáveis de ambiente `JAVA_HOME` e `SPARK_HOME`.
2. Configure ambiente virtual Python e instale dependências:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Baixe o dataset `churn-bigml-20.csv` para a pasta `data/`:

```bash
wget https://raw.githubusercontent.com/bensadeghi/pyspark-churn-prediction/master/data/churn-bigml-20.csv -P data/
```

4. Execute o script principal:

```bash
python src/main.py
```

---

## Dependencies / Dependências

- PySpark 4.0.1
- findspark

---

## License / Licença

MIT License

---

## Author / Autor

Gabriel
