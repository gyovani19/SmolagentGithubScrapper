# 🔍 **GitHub Repo Scanner & Issue Creator**
Este projeto utiliza **`smolagents`** para buscar **repositórios públicos** de um usuário do GitHub via **DuckDuckGoSearchTool** e **criar automaticamente uma issue** no repositório pessoal do usuário com um relatório dos resultados.

---

## 📌 **Funcionalidades**
- 🔎 **Pesquisa repositórios públicos** de qualquer usuário do GitHub sem acessar diretamente a API.
- 📋 **Gera um relatório automático** com os links e descrições dos repositórios encontrados.
- 📝 **Cria uma issue no repositório do usuário** (`github.com/{username}/{username}`) contendo os resultados.

---

## 🛠 **Instalação e Configuração**
### **1️⃣ Instale as dependências**
```bash
pip install smolagents requests python-dotenv
```

### **2️⃣ Configure seu Token do GitHub**
- Crie um arquivo `.env` no diretório do projeto e adicione:
  ```
  GITHUB_TOKEN=seu_token_aqui
  ```
  🔹 O token é necessário para criar issues no GitHub.

---

## 🚀 **Como Usar**
1️⃣ **Execute o script**:
   ```bash
   python github_issue_creator.py
   ```

2️⃣ **Digite o nome do usuário do GitHub** quando solicitado:
   ```
   Digite o nome do usuário do GitHub: torvalds
   ```

3️⃣ **Saída esperada**:
   ```
   🔍 Repositórios Públicos do Usuário:
   - github.com/torvalds?tab=repositories
   - github.com/torvalds/linux
   - github.com/torvalds/subsurface

   📌 Status da Issue:
   ✅ Issue criada com sucesso no repositório torvalds!
   ```

---

## ⚙️ **Estrutura do Projeto**
```
📂 github-repo-scanner
│── 📄 github_issue_creator.py  # Script principal
│── 📄 .env                     # Arquivo com token do GitHub
│── 📄 requirements.txt         # Lista de dependências
│── 📄 README.md                # Documentação do projeto
```

---

## 🛠 **Tecnologias Utilizadas**
- **Python 3.x**
- **smolagents**
- **DuckDuckGoSearchTool**
- **GitHub API**
- **requests**
- **dotenv**

---

## 📌 **Contribuição**
🔹 Pull Requests são bem-vindos! Caso queira melhorar o projeto, abra uma **issue** ou envie um **PR**.  

---

## ⚡ **Licença**
MIT License. Sinta-se à vontade para usar e modificar! 🚀🔥
