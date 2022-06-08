import user_information
from user_information import build_profile
from user_information import build_profile as nf
import user_information as nm

print("=="*20)
# Importacao do modulo user-information
user_profile = user_information.build_profile('azagaia','repper',location = 'mozambique', field = 'Mc', style = 'underground', especialization = 'alternative rep')
print(user_profile)
print("=="*20)

# Importacao da funcao build_profile do modulo user_information
user_profile = build_profile('Edgar', 'Rocker', location = 'aldeia', especialization = 'alternative rock')
print(user_profile)
print("=="*20)

# Importacao da funcao build_profile renomeada com nf do modulo user_information
user_profile = nf('cobica', 'marabenta musician', location = 'comunidade', especialization = 'deep marabenta')
print(user_profile)
print("=="*20)

# Importacao do modulo user_information renomeado com nm do modulo user_information
user_profile = nm.build_profile('augusto', 'soul musician',location = 'maputo', especialization = 'romantic songs')
print(user_profile)
print("=="*20)

# Importacao de todas funcoes em um modulo
user_profile = build_profile('marcia', 'kizomba singer', location = 'maputo', especialization = 'kizomba')
print(user_profile)
print("=="*20)