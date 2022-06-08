
def print_models(unprinted_designs, completed_models):
    """Simula a impressao de cada design, ate que nao haja mais nenhum.
    Transfere vada design para completed_models apos a impressao."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simula a criacao de uma impressao 3D a partir do design
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)