# Roteiro de Apresentacao - AI Content Repurposer

> Guia para apresentar o projeto ao chefe. Use as tecnicas de memorizacao abaixo.

---

## 1. Estrutura da apresentacao (modele 5-7 minutos)

### Abertura (30 segundos)
"Eu desenvolvi uma ferramenta chamada AI Content Repurposer. Ela pega um texto longo, como um artigo ou anotacao, e transforma em pecas prontas para publicar nas redes sociais."

### O problema (1 minuto)
- Criar conteudo para redes sociais e demorado.
- Textos longos (artigos, reunioes, anotacoes) acabam subaproveitados.
- Equipes pequenas nao tem tempo de reescrever o mesmo conteudo varias vezes.

### A solucao (2 minutos)
A ferramenta tem duas partes:
1. **CLI (terminal)**: um script Python que le .txt ou .md e gera automaticamente:
   - Resumo executivo com ate 5 topicos.
   - 3 variacoes de post para redes sociais.
   - 3 titulos alternativos.
   - Salva tudo em `conteudo.json`.

2. **Dashboard Web**: uma pagina HTML simples onde voce:
   - Cola o JSON gerado.
   - Revisa cada peca.
   - Marca como aprovada ou descartada.
   - Copia o texto final com um clique.

### Demonstracao (2 minutos)
"Vou mostrar rapidinho como funciona."
1. Rode o comando no terminal.
2. Mostre o `conteudo.json` gerado.
3. Abra o dashboard, clique em "Ver exemplo" e mostre aprovacao/copia.

### Aprendizado (1 minuto)
"O que mais me marcou foi ver como um arquivo JSON pode ligar duas interfaces diferentes: o terminal e o navegador. Tambem aprendi a usar branches no Git para nao mexer direto na main e abrir Pull Requests antes de mergear."

### Fechamento (30 segundos)
"A proxima versao pode integrar uma API de IA de verdade, como OpenAI, para deixar os textos ainda mais criativos."

---

## 2. Tecnica de memorizacao: o metodo da jornada

Imagine que voce esta andando pelo seu quarto ou casa. Cada comodo representa uma parte da apresentacao:

1. **Porta de entrada** = Abertura: "AI Content Repurposer, texto longo vira pecas prontas."
2. **Sofa** = Problema: conteudo demora, textos sao subaproveitados.
3. **Mesa do computador** = Solucao: CLI gera JSON, dashboard revisa e aprova.
4. **Tela do computador** = Demonstracao: rodar script, abrir dashboard, copiar texto.
5. **Cama** = Aprendizado: JSON conecta terminal e navegador; Git com branches e PRs.
6. **Janela** = Fechamento: proximo passo e integrar IA real.

Antes de dormir, visualize essa jornada 3 vezes mentalmente.

---

## 3. Regra dos 3

Toda vez que for explicar algo, agrupe em 3 itens. O cerebro memoriza melhor assim.

Exemplos:
- **3 saidas do CLI**: resumo executivo, posts sociais, titulos alternativos.
- **3 plataformas dos posts**: LinkedIn, Instagram/Threads, X (Twitter).
- **3 acoes do dashboard**: revisar, aprovar/descartar, copiar.
- **3 branches principais**: feature/cli-repurposer, feature/dashboard, staging.
- **3 comandos Git**: add, commit, push.

---

## 4. Perguntas que o chefe pode fazer

### "Por que voces nao usaram uma API de IA de verdade?"
Resposta: "A versao atual funciona localmente, sem depender de chave de API. Isso garante que qualquer pessoa possa rodar sem custo. A proxima etapa e integrar OpenAI ou Claude para textos mais criativos."

### "Qual foi o maior desafio?"
Resposta: "Organizar o workflow do Git. A gente precisou criar branches, fazer commits separados e abrir Pull Requests para nao mexer direto na main. Foi importante para aprender como trabalha em equipe."

### "Como voce testou?"
Resposta: "Criei um arquivo de exemplo em `examples/artigo-exemplo.md`, rodei o script e verifiquei se o JSON gerado tinha a estrutura certa. Depois testei o dashboard colando o JSON e aprovando itens."

### "O que voce aprendeu de novo?"
Resposta: "Aprendi que um arquivo JSON pode ser a ponte entre um programa de terminal e uma interface web. Tambem aprendi os comandos `git checkout -b`, `git status`, `git add`, `git commit` e `git push` na pratica."

### "Qual e o proximo passo?"
Resposta: "Integrar uma API de IA real, permitir upload direto do JSON no dashboard e adicionar testes automaticos no script Python."

---

## 5. Dicas para a apresentacao

- Fale devagar e faca pausas.
- Olhe para o chefe, nao so para a tela.
- Se esquecer algo, respire e volte para a jornada mental (porta, sofa, mesa, tela, cama, janela).
- Mostre o GitHub e os Pull Requests como prova de trabalho organizado.
- Termine sempre falando do proximo passo: isso mostra visao.

---

## 6. Checklist antes de dormir

- [ ] Leu este roteiro em voz alta 2 vezes.
- [ ] Visualizou a jornada mental 3 vezes.
- [ ] Testou rodar o script uma ultima vez.
- [ ] Abriu o dashboard no navegador e clicou em "Ver exemplo".
- [ ] Revisou as 5 perguntas e respostas.

Boa sorte na apresentacao!
