# Python Exercícios

Este repositório contém exercícios em Python, organizados por temas. É um espaço de aprendizado e prática da linguagem.

## Estrutura
- **zip_frutas**: Demonstra o uso da função `zip()` para combinar listas.

## Sobre o Exercício `zip_frutas`
A função **`zip()`** no Python é usada para combinar elementos de duas ou mais sequências (como listas ou tuplas) em pares ou grupos, criando um iterador. No caso do exercício `zip_frutas`, ela é utilizada para combinar:

- Uma lista de frutas.
- Uma lista de cores correspondentes.

### Exemplo:
```python
frutas = ["maçã", "banana", "uva"]
cores = ["vermelha", "amarela", "roxa"]

resultado = zip(frutas, cores)
print(list(resultado))

