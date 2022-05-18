# Cidades: Crie um dicionario chamado cities. Use os nomes de tres cidades como chaves em seu dicionario. Crie um dicionario com informacoes sobre cada cidade e inclua o pais em que a cidade esta localizada, a populacao aproximada e um fato sobre essa cidade. As chaves do dicionario de cada cidade devem ser algo como coutry, population e fact. Apresente o nome de cada cidade e todas as informacoes que voce armazenou sobre ela.

cities = {
    'maputo': {
        'coutry': 'mozambique',
        'population': '12.488.246',
        'fact': 'corupt coutry'
    },
    'sao paulo': {
        'coutry': 'brazil',
        'population': '145.264.218',
        'fact': 'beautiful people'
    },
    'lisbon': {
        'coutry': 'portugal',
        'population': '10.264.254',
        'fact': 'racist'
    }
}

for key, value in cities.items():
    print(f"{key} city:".title())
    for k, v in value.items():
        print(f"{k} => {v}".title())
    print("=="*10)
