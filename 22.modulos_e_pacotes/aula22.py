# Modilarizacao e' o acto de construir modulos. O conceito de modularizacao surgiu no inicio da decada de 60 quando os sistemas ficavam cada vez maiores e com isso, os codigos mais extensos. Este conceito surgiu com o objectivo de dividir um programa grande em pequenos pedacos e aumentar a legibilidade e facilitar a manuntencao.

# Imagina que criamos um codigo de funcoes de calculos de factorial, calculo de dobro e calculo de triplo no arquivo numeros.py . Imaginemos que este codigo se torne grande, entao, podemos fazer com que, para nao alongar mais o codigo, em vez de termos as funcoes no arquivo principal, passamos as funcoes para o arquivos de uteis, criando o arquivo uteis.py e passando todas as funcoes para la'.

# Feito isso, se quisermos usar uma determinada funcao no nosso arquivo principal, podemos chamar a funcao atraves de importacao do seu modulo, neste caso, o modulo uteis.py.

# Para importar o modulo, usamos a extensao import uteis

# Para chamar a funcao. Por exemplo, a funcao factorial(num), usamos a extensao: uteis.factorial(num).

# As VANTAGENS do uso de modularizacao e' que facilita a organizacao do seu codigo, deixando mais leve e curto, pois, a gente divide o grande codigo em pequenos que se comunicam entre si. Tambem facilita a manuntencao do codigo, sendo mais facil identificar os erros no codigo, ja' que o mesmo se torna mais pequeno. Alem disso oculta detalhes disnecessarios, no exemplo da funcao, os comentarios e o codigo da funccao sao desnecessarios no codigo mae, o que interessa mesmo e' o uso daquela funcao, e' o que ela faz e nao como foi feita. E por fim faz com que as funcoes ou os codigos sejam utilizados em diferentes projectos, basta copia-los ou simplesmente importa-los se estiverem na mesma pasta.

# Quando os modulos se tornam bastante grandes e nao satisfazem os objectivos para os quais foram criados, os PACOTES entram em cena.

#   PACOTES

# Pacotes sao pastas que contem modulos. No python, todas pastas sao consideradas Pacotes.