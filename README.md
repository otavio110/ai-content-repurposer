# AI Content Repurposer

Ferramenta que pega um conteudo longo (artigo, transcrição de reuniao ou anotações) e transforma em pecas prontas para publicação.

O projeto tem duas partes:

1. **CLI (linha de comando)**: um script Python que processa o texto e gera `conteudo.json`.
2. **Dashboard Web**: uma interface HTML simples para revisar, aprovar e copiar as pecas geradas.

---

## Funcionalidades

- Gera um **resumo executivo** com ate 5 topicos.
- Cria **3 variações de post** para redes sociais (LinkedIn, Instagram/Threads e X/Twitter).
- Sugere **3 titulos alternativos**.
- Salva o resultado em `conteudo.json`.
- Permite revisar cada peca no dashboard, marcar como aprovada ou descartada.
- Copia o texto final aprovado com um clique.

---

## Como rodar a ferramenta

### 1. Clone o repositorio

```bash
git clone https://github.com/SEU_USUARIO/ai-content-repurposer.git
cd ai-content-repurposer
```

### 2. Instale as dependencias

```bash
cd cli
pip install -r requirements.txt
```

> Nesta versao, o script usa apenas bibliotecas padrao do Python. O `requirements.txt` esta pronto para adicionar a API da OpenAI no futuro.

### 3. Rode o script

No Windows, se o comando `python` abrir a Microsoft Store, use o caminho completo onde o Python foi instalado:

```bash
python repurposer.py ../examples/artigo-exemplo.md --output ../conteudo.json --md
```

Ou, se o comando acima nao funcionar:

```bash
/c/Users/matte/AppData/Local/Programs/Python/Python311/python.exe repurposer.py ../examples/artigo-exemplo.md --output ../conteudo.json --md
```

O que cada parte faz:

- `python repurposer.py` → executa o script
- `../examples/artigo-exemplo.md` → caminho do arquivo de entrada
- `--output ../conteudo.json` → nome do arquivo de saida
- `--md` → tambem gera uma versao em Markdown

### 4. Veja o resultado

Depois de rodar, abra o arquivo `conteudo.json`. Ele tera esta estrutura:

```json
{
  "resumo_executivo": ["1. ...", "2. ..."],
  "posts_sociais": [
    {"plataforma": "LinkedIn", "texto": "..."},
    {"plataforma": "Instagram / Threads", "texto": "..."},
    {"plataforma": "X (Twitter)", "texto": "..."}
  ],
  "titulos_alternativos": ["...", "...", "..."],
  "metadados": {
    "data_geracao": "...",
    "total_caracteres": 1234,
    "total_palavras": 200,
    "modo": "local"
  }
}
```

### 5. Use o dashboard

Abra o arquivo `dashboard/index.html` no navegador (de um duplo clique nele).

No dashboard:

1. Cole o conteudo do `conteudo.json` na caixa de texto.
2. Clique em **Carregar no dashboard**.
3. Revise cada titulo, topico e post.
4. Clique em **Aprovar** ou **Descartar**.
5. Ao final, clique em **Copiar texto final**.

---

## Prints da interface

### Tela inicial do dashboard

![dashboard-inicial](docs/print-dashboard-inicial.png)

> O dashboard mostra uma caixa de texto onde voce cola o JSON gerado pelo script.

### Dashboard com conteudo carregado

![dashboard-conteudo](docs/print-dashboard-conteudo.png)

> Depois de carregar, aparecem os titulos, o resumo executivo e os posts. Cada um pode ser aprovado ou descartado.

### Texto final aprovado

![dashboard-final](docs/print-dashboard-final.png)

> Ao final, voce copia o texto aprovado com um clique.

---

## Estrutura do projeto

```
ai-content-repurposer/
├── cli/
│   ├── repurposer.py       ← script de terminal
│   └── requirements.txt    ← dependencias
├── dashboard/
│   └── index.html          ← interface web de revisao
├── examples/
│   └── artigo-exemplo.md   ← texto de teste
├── docs/
│   └── prints do dashboard  ← adicione aqui
├── README.md               ← este arquivo
└── .gitignore
```

---

## Workflow Git e GitHub

Este projeto segue um workflow com branches:

- `main`: branch principal, so recebe codigo aprovado via Pull Request.
- `feature/cli-repurposer`: branch onde desenvolvemos o script de terminal.
- `feature/dashboard`: branch onde desenvolvemos a interface web.

Passos usados:

```bash
# Criar nova branch
git checkout -b feature/nome-da-feature

# Ver o que mudou
git status

# Adicionar arquivos
git add .

# Salvar mudancas
git commit -m "Mensagem clara do que foi feito"

# Enviar para o GitHub
git push origin feature/nome-da-feature
```

Depois, abrimos um Pull Request no GitHub e fazemos o merge para `main`.

---

## O que aprendi

Neste projeto, aprendi como transformar uma ideia simples em um produto funcional com duas interfaces: uma para o terminal e outra para o navegador. O maior aprendizado foi entender como o script em Python pode gerar um arquivo JSON padronizado, e como o dashboard em HTML le esse JSON para criar uma experiencia visual de revisao.

Descobri tambem a importancia do `git status` antes de cada commit: ele mostra exatamente quais arquivos foram alterados e ajuda a nao enviar arquivos desnecessarios. Outro comando que fez diferenca foi o `git checkout -b nome-da-branch`, que permite trabalhar em novas funcionalidades sem mexer diretamente na `main`.

A logica do dashboard me ajudou a revisar JavaScript basico: como criar elementos HTML dinamicamente, mudar classes CSS com `classList.add/remove` e usar `document.execCommand('copy')` para copiar texto. Mesmo sem usar uma API externa, a ferramenta ja entrega valor porque processa o texto e organiza as pecas de forma clara.

---

## Proximos passos

- Integrar com API de IA (OpenAI, Anthropic) para gerar textos mais criativos.
- Permitir upload direto do arquivo `conteudo.json` no dashboard.
- Adicionar testes automaticos para o script Python.
- Criar uma versao em Node.js como alternativa ao Python.
