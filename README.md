# API de Países com Flask

API REST desenvolvida em Python utilizando Flask, com foco em arquitetura limpa, boas práticas de backend, containerização com Docker e deploy em produção no Google Cloud Run.

---

## Demonstração

🔗 **API em produção (Cloud Run):**
https://api-paises-363649791380.southamerica-east1.run.app

### Exemplos:

* Health check

```
GET /health
```

* Buscar dados de um país

```
GET /api/v1/pais/dados/brasil
```

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte de um estudo de backend em Python.

A API consome dados da API pública [RestCountries](https://restcountries.com/) e retorna informações estruturadas sobre países.

---

## 🧠 Principais aprendizados

* Construção de API REST com Flask
* Arquitetura em camadas (routes → services → clients)
* Separação de responsabilidades (SRP)
* Tratamento centralizado de erros
* Testes automatizados com pytest
* Injeção de dependência
* Containerização com Docker
* Deploy em produção com Google Cloud Run
* Logging estruturado (JSON)
* Configuração por ambiente (dev / prod / test)

---

## ⚙️ Tecnologias utilizadas

* Python 3.12
* Flask
* Requests
* Pytest
* Gunicorn
* Docker
* Google Cloud Run

---

## 📈 Status do projeto

✅ Concluído como projeto de estudo
🚀 Pronto para produção (Cloud Run)
📦 Estruturado para evolução (ex: autenticação, cache, banco de dados)

---

## 👨‍💻 Autor

**Lucas Padovan Cintra Correa**
https://github.com/Lucas-PadovanCintra

---

## 📌 Observação

Este projeto foi desenvolvido com fins educacionais, simulando um ambiente real de backend moderno com deploy em cloud.

---
