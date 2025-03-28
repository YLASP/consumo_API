# consumo_API
# 🚀 Lista de Motos Kawasaki Ninja (+500cc) com Flask

Este projeto é uma aplicação web desenvolvida em **Python (Flask)** que consome uma API externa para listar motocicletas Kawasaki Ninja com cilindrada acima de **500cc**.

## 📌 Funcionalidades
- Consulta a API de motocicletas.
- Filtra apenas as motos com mais de 500cc.
- Exibe os dados em uma interface web simples e responsiva.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Flask, Requests)
- **HTML + CSS** (Template simples para exibição dos dados)
- **JavaScript** (Para buscar os dados da API via Fetch)

---

## 📂 Estrutura do Projeto

```
motos-flask/
│── app.py          # Código principal do Flask
│── /templates      # Pasta para os templates HTML
│   └── index.html  # Página principal da aplicação
│── README.md       # Documentação do projeto
```

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/motos-flask.git
cd motos-flask
```

### 2️⃣ Criar um Ambiente Virtual (Opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install flask requests
```

### 4️⃣ Rodar o Servidor Flask
```bash
python app.py
```

Se tudo estiver certo, você verá a mensagem:
```
 * Running on http://127.0.0.1:5000/
```
Acesse no navegador: **http://127.0.0.1:5000/**

---

## 📌 API Utilizada
A API utilizada é fornecida por [API Ninjas](https://api-ninjas.com/), que retorna dados de motocicletas.

---

## 🤝 Contribuição
Sinta-se à vontade para contribuir! Basta abrir um **Pull Request** ou relatar problemas na aba de **Issues**. 😃

---

## 📜 Licença
Este projeto está sob a licença **MIT**. Você pode usá-lo e modificá-lo como quiser! 🏍️

