```markdown
# Sinapse API 🚀

API REST minimalista desenvolvida com **Flask** e hospedada na **AWS EC2**. Gerenciada com `uv`, o moderno gerenciador de pacotes Python.

---

## 🛠 Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.12+ | Linguagem principal |
| Flask | Microframework web |
| uv | Gerenciador de pacotes e ambiente virtual |
| AWS EC2 | Hospedagem em nuvem (Ubuntu 24.04) |

---

## ☁️ Infraestrutura AWS

- **Instância:** EC2 t3.small — Ubuntu 24.04 LTS
- **Região:** us-east-1 (N. Virginia)
- **Security Group:** porta `22` (SSH) + porta `5000` (API)
- **IP Público:** `44.192.78.9`

---

## 🚀 Como rodar localmente

### 1. Instalar o `uv`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clonar e executar
```bash
git clone https://github.com/felixruntime/sinapse-api.git
cd sinapse-api

# Instalar dependências
uv sync

# Rodar a API
uv run python app.py
```

A API estará disponível em `http://localhost:5000`.

---

## 📡 Endpoints

| Método | Rota | Descrição | Exemplo de resposta |
|---|---|---|---|
| `GET` | `/` | Boas-vindas | `{"message": "Sinapse API Online!", "status": "success"}` |
| `GET` | `/health` | Status da API | `{"service": "sinapse", "status": "ok", "version": "1.0.0"}` |
| `GET` | `/echo/` | Echo com mensagem padrão | `{"echo": "Customize essa mensagem..."}` |
| `GET` | `/echo/<texto>` | Repete o texto enviado na URL | `{"echo": "seutexto"}` |

---

## 🧪 Testando com cURL

```bash
# Boas-vindas
curl http://44.192.78.9:5000/

# Health check
curl http://44.192.78.9:5000/health

# Echo padrão
curl http://44.192.78.9:5000/echo/

# Echo customizado
curl http://44.192.78.9:5000/echo/ola-mundo
```

---

## 🔐 Tratamento de Erros

Todos os erros retornam JSON padronizado:

```json
// 404 — Rota não encontrada
{"error": "Not Found", "message": "Rota inexistente"}

// 500 — Erro interno
{"error": "Internal Server Error", "message": "Erro inesperado"}
```