import matplotlib.pyplot as plt
import numpy as np 

dados = (89.2866, 86.6530, 83.9683, 83.5592, 84.2496, 82.0762)

cor = ('r', 'g', '#00FF33')

legenda = ('SMO', 'J48', 'REPTree', 'NaiveBayes', 'ZeroR', 'RandomTree')

#vai ler a variavel dados criando 6 pontos no grafico
eixox = np.arange(len(dados))

#largura da barra 
largura = 0.50 

# Cria os eixo (x e y) neste caso 
ax = plt.axes() 
   
# Cria as barras onde: 
# eixox = sao os pontos (1, 2 , 3) do eixo x 
# dados = valores da variavel dados (eixo y) 
# yerr = margem de erro em y (repare que tem uma linha azul no centro 
# de cada barra) dependendo do valor digitado essa margem aumenta ou diminui 
# align = Alinhamento do grafico se nao utilizar este parametro
# as barras ficam coladas nas bordas do grafico 
#grafico = plt.bar(eixox, dados, largura, color=cor, yerr=5, align='center') 

grafico = plt.bar(eixox, dados, largura, color=cor, align='center') 
    
for barras in grafico: 
   
# barras.get_x() faz com que o valor da variavel dados acompanhe o topo da barra 
# barras.get_width() dividido por 2.0 faz com que os dados fiquem no centro 
	ax.text(barras.get_x() + (barras.get_width() / 2.0),
# altura dos dados que ficam acima da linha azul podem ser utilizadas 
# outras alturas como + 7, + 8, o que ficar melhor no seu grafico 
barras.get_height() + 6, 
# texto acima das barras e centralizado 
barras.get_height(), ha='center') 

# Cria os pontos do eixo x (1, 2, 3) 
# sem isso a variavel legenda fica alinhada a esquerda 
# ao inves de ficar no centro 
ax.set_xticks(eixox) 
# Cria a legenda na base das barras 
# 1, 2, 3 = 2013, 2014, 2015 
ax.set_xticklabels(legenda) 
# Cria o texto do eixo x 
plt.xlabel('Algoritmo') 
# Cria o texto no eixo y 
plt.ylabel('Porcentagem(%)') 
# Ativa as linhas de grade no grafico 
plt.grid(False) 
# Cria a legenda com as cores e o texto que esta 
# na variavel legenda 
#plt.legend(grafico, legenda)

plt.axis(['','',0,100])


# Exibe o grafico 
plt.show()