# script.py

def filtrar_alunos_aprovados(lista_alunos, nota_minima=7.0):
    """
    Filtra os alunos que obtiveram nota maior ou igual à nota mínima.
    """
    aprovados = []
    for aluno in lista_alunos:
        if aluno["nota"] >= nota_minima:
            aprovados.append(aluno)
    return aprovados

def exibir_resultados(alunos_totais, alunos_aprovados):
    """
    Exibe de forma organizada a lista geral e os alunos aprovados.
    """
    print("-" * 40)
    print("LISTA GERAL DE ALUNOS:")
    print("-" * 40)
    for aluno in alunos_totais:
        print(f"Nome: {aluno['nome']:<15} | Nota: {aluno['nota']:>4.1f}")
        
    print("\n" + "-" * 40)
    print("ALUNOS APROVADOS (Nota >= 7.0):")
    print("-" * 40)
    if not alunos_aprovados:
        print("Nenhum aluno foi aprovado.")
    for aluno in alunos_aprovados:
        print(f"Parabéns! {aluno['nome']:<13} | Nota: {aluno['nota']:>4.1f}")
    print("-" * 40)

def main():
    # Estrutura de dados: Lista contendo Dicionários
    alunos = [
        {"nome": "Ana Silva", "nota": 8.5},
        {"nome": "Bruno Costa", "nota": 6.2},
        {"nome": "Carlos Souza", "nota": 7.0},
        {"nome": "Daniela Lima", "nota": 9.5},
        {"nome": "Eduardo Alves", "nota": 5.8}
    ]
    
    # Filtragem
    aprovados = filtrar_alunos_aprovados(alunos)
    
    # Saída de dados
    exibir_resultados(alunos, aprovados)

if __name__ == "__main__":
    main()
