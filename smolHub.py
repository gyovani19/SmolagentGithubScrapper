import os
import requests
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, ManagedAgent
from dotenv import load_dotenv

# Carregar variáveis do ambiente (.env)
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Configure seu token no .env
BASE_URL = "https://api.github.com"

# Criar o modelo
model = HfApiModel()

# Criar um agente que faz buscas na web
web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# Criar um agente gerenciado para buscas
managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="web_search",
    description="Runs web searches for you. Provide a search query as an argument."
)

# Criar um agente gerenciador que usa o agente de busca
manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[managed_web_agent]
)

def criar_issue(username: str, title: str, body: str) -> str:
    """
    Cria uma issue no repositório pessoal do usuário (com o mesmo nome do usuário).

    Args:
        username (str): Nome do usuário do GitHub.
        title (str): Título da issue.
        body (str): Conteúdo da issue.

    Returns:
        str: Mensagem de sucesso ou erro.
    """
    repo = username  # O nome do repositório é igual ao nome do usuário
    url = f"{BASE_URL}/repos/{username}/{repo}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"title": title, "body": body}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return f"✅ Issue criada com sucesso no repositório {repo}!"
    else:
        return f"❌ Erro ao criar issue: {response.status_code} - {response.json()}"

# Execução com input do terminal
if __name__ == "__main__":
    username = input("Digite o nome do usuário do GitHub: ").strip()
    
    # Criar a consulta de busca para encontrar os repositórios públicos do usuário
    search_query = f"site:github.com/{username}?tab=repositories"
    
    # Executa a busca e recebe os resultados
    result = manager_agent.run(f"web_search('{search_query}')")

    print("\n🔍 Repositórios Públicos do Usuário:\n")
    print(result)

    # Criar uma issue com o resumo dos repositórios encontrados
    issue_title = "🔍 Relatório de Repositórios Públicos"
    issue_body = f"### Relatório gerado automaticamente:\n\n{result}"

    issue_response = criar_issue(username, issue_title, issue_body)
    
    print("\n📌 Status da Issue:")
    print(issue_response)
