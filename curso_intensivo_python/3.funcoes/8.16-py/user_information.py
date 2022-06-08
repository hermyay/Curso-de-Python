def build_profile(first, last, **user_info):
    """Constroi um dicionario contendo tudo que sabemos sobre um usuario."""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile