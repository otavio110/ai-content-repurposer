#!/usr/bin/env python3
"""
AI Content Repurposer - CLI
Recebe um texto longo e gera:
- Resumo executivo em ate 5 topicos
- 3 variacoes de post para redes sociais
- 3 titulos alternativos

Uso:
    python repurposer.py caminho/do/arquivo.md
    python repurposer.py caminho/do/arquivo.txt --output conteudo.json
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def read_input(filepath: str) -> str:
    """Le o arquivo de entrada (.txt ou .md) e remove marcacao Markdown basica."""
    path = Path(filepath)
    if not path.exists():
        print(f"Erro: arquivo nao encontrado -> {filepath}")
        sys.exit(1)
    if path.suffix.lower() not in (".txt", ".md"):
        print("Erro: apenas arquivos .txt ou .md sao suportados.")
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    # Remove linhas que comecam com # (titulos Markdown)
    text = re.sub(r"^#+\s*.*$", "", text, flags=re.MULTILINE)
    return text.strip()


def extract_keywords(text: str, n: int = 5) -> list:
    """Extrai palavras-chave simples (palavras mais frequentes, ignorando comuns)."""
    stopwords = {
        "o", "a", "os", "as", "um", "uma", "de", "do", "da", "dos", "das",
        "e", "que", "em", "no", "na", "nos", "nas", "por", "para", "com",
        "sem", "sob", "sobre", "entre", "durante", "apesar", "embora", "e",
        "sao", "foi", "foram", "ser", "estar", "ter", "haver", "mais",
        "menos", "muito", "pouco", "tudo", "nada", "todo", "qual", "como",
        "quando", "onde", "porque", "mas", "ou", "se", "the", "and", "of",
        "to", "in", "for", "on", "with", "at", "by", "from", "as", "is",
        "it", "this", "that", "a", "an", "are", "was", "were", "be", "been",
        "conteudo", "criar", "fazer", "dizer", "ver", "usar", "poder", "dever",
        "querer", "saber", "passar", "novo", "cada", "todos", "todas", "bem",
        "assim", "onde", "aqui", "agora", "depois", "antes", "desde", "ate",
        "mesmo", "proprio", "outro", "outra", "outros", "outras", "muitos",
        "muitas", "tanto", "tanta", "tantos", "tantas", "content", "marketing",
        "strategy", "create", "make", "need", "want", "will", "can", "also",
        "just", "like", "one", "two", "three", "first", "last", "new", "good",
        "best", "way", "work", "use", "help", "get", "know", "come", "look",
        "voce", "voces", "nos", "eles", "elas", "meu", "minha", "seu", "sua",
        "nosso", "nossa", "publicar", "aparecer", "ajudar", "mudar", "funcionar",
        "realmente", "aqui", "exemplo", "artigo", "texto", "sobre", "abaixo",
        "precisa", "necessario", "necessaria", "importante", "outro", "outra",
        "pessoa", "pessoas", "alguem", "todos", "todas", "qualquer", "mesmo",
        "sendo", "fazendo", "tendo", "dando", "vendo", "sendo",
        "mudou", "muda", "mudar", "transformou", "transforma", "transformar",
        "gera", "gerar", "gerando", "bons", "boas", "bom", "boa"
    }
    words = re.findall(r"\b[a-zA-Zà-úÀ-Ú]{4,}\b", text.lower())
    freq = {}
    for w in words:
        if w in stopwords:
            continue
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:n]]


def split_sentences(text: str) -> list:
    """Divide o texto em frases simples."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) > 20]


def generate_summary(text: str) -> list:
    """Gera resumo executivo com ate 5 topicos."""
    sentences = split_sentences(text)
    if len(sentences) < 5:
        return sentences
    # Pega frases distribuidas ao longo do texto para cobrir o conteudo
    step = max(1, len(sentences) // 5)
    selected = [sentences[i * step] for i in range(5)]
    return [f"{i+1}. {s}" for i, s in enumerate(selected)]


def generate_social_posts(text: str) -> list:
    """Gera 3 variacoes de post para redes sociais."""
    keywords = extract_keywords(text, 3)
    keyword_phrase = ", ".join(keywords) if keywords else "este conteudo"
    sentences = split_sentences(text)
    hook = sentences[0] if sentences else "Descubra como transformar seu conteudo."

    return [
        {
            "plataforma": "LinkedIn",
            "texto": (
                f"{hook}\n\n"
                f"Se voce trabalha com {keyword_phrase}, esse material e para voce.\n\n"
                f"Aqui estao os pontos que mais me chamaram atencao:\n"
                f"- {keywords[0] if keywords else 'Estrategia'}\n"
                f"- {keywords[1] if len(keywords) > 1 else 'Execucao'}\n"
                f"- {keywords[2] if len(keywords) > 2 else 'Resultado'}\n\n"
                f"Qual desses voce quer aplicar primeiro? Comenta aqui."
            )
        },
        {
            "plataforma": "Instagram / Threads",
            "texto": (
                f"{hook}\n\n"
                f"{keyword_phrase} nao precisa ser complicado.\n"
                f"O segredo e transformar ideias grandes em acoes pequenas.\n\n"
                f"Salva esse post para revisar depois e me conta: qual dica fez mais sentido para voce?"
            )
        },
        {
            "plataforma": "X (Twitter)",
            "texto": (
                f"{hook}\n\n"
                f"3 aprendizados rapidos sobre {keyword_phrase}:\n"
                f"1. Clareza vence volume.\n"
                f"2. Foco no publico certo.\n"
                f"3. Repeticao com proposito.\n\n"
                f"Concorda? Da RT se fez sentido."
            )
        }
    ]


def generate_titles(text: str) -> list:
    """Gera 3 titulos alternativos."""
    keywords = extract_keywords(text, 3)
    k1 = keywords[0] if keywords else "conteudo"
    k2 = keywords[1] if len(keywords) > 1 else "estrategia"
    return [
        f"Como transformar {k1} em resultados reais",
        f"O guia pratico de {k2} que voce precisa ler",
        f"{k1.capitalize()}: o que funciona (e o que nao funciona) em 2025"
    ]


def process_content(text: str) -> dict:
    """Processa o conteudo e retorna o JSON final."""
    return {
        "resumo_executivo": generate_summary(text),
        "posts_sociais": generate_social_posts(text),
        "titulos_alternativos": generate_titles(text),
        "metadados": {
            "data_geracao": datetime.now().isoformat(),
            "total_caracteres": len(text),
            "total_palavras": len(text.split()),
            "modo": "local"
        }
    }


def save_json(data: dict, output_path: str):
    """Salva o resultado em JSON."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Resultado salvo em: {output_path}")


def save_markdown(data: dict, output_path: str):
    """Salva o resultado em Markdown (opcional)."""
    lines = []
    lines.append("# Conteudo Reaproveitado\n")
    lines.append(f"_Gerado em: {data['metadados']['data_geracao']}_\n")

    lines.append("## Resumo Executivo\n")
    for item in data["resumo_executivo"]:
        lines.append(f"- {item}\n")

    lines.append("\n## Posts para Redes Sociais\n")
    for post in data["posts_sociais"]:
        lines.append(f"### {post['plataforma']}\n")
        lines.append(f"{post['texto']}\n\n")

    lines.append("## Titulos Alternativos\n")
    for title in data["titulos_alternativos"]:
        lines.append(f"- {title}\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print(f"Versao Markdown salva em: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="AI Content Repurposer: transforme textos longos em pecas prontas para publicar."
    )
    parser.add_argument("input", help="Caminho do arquivo .txt ou .md de entrada")
    parser.add_argument("--output", "-o", default="conteudo.json",
                        help="Nome do arquivo de saida (padrao: conteudo.json)")
    parser.add_argument("--md", action="store_true",
                        help="Tambem gera uma versao em Markdown do resultado")

    args = parser.parse_args()

    print(f"Lendo arquivo: {args.input}")
    text = read_input(args.input)

    print("Gerando conteudo...")
    result = process_content(text)

    save_json(result, args.output)
    if args.md:
        md_path = args.output.replace(".json", ".md")
        save_markdown(result, md_path)

    print("\nPronto! Agora voce pode revisar no dashboard.")


if __name__ == "__main__":
    main()
