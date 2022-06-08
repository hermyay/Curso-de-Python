# Perfil do usuario: Comece com uma copia de user_profile.py, da pagina 210. Crie um perfil seu chamado build_profile(), usando seu primeiro nome e o sobrenome , alem de tres outros pares chave-valor que o descrevam.

def build_profile(first, last, **user_info):
    """Constroi um dicionario contendo tudo que sabemos sobre um usuario."""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('azagaia','repper',location = 'mozambique', field = 'Mc', style = 'underground', especialization = 'alternative rep')

print(user_profile)