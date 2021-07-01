# HouseRocket
House Rocket Company
Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog Seja um Data Scientist, para mais informações clique no link a seguir.

SejaUmDataScientist

Descrição
House Rocket é uma empresa do ramo imobiliario que procura novos imóveis para seu catalogo, fomentada pela alta e baixa recorrente do mercado imobiliario a empresa busca novas oportunidades de compra de imóveis. A empresa procurou um Cientista de dados para ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em condições regulares quando estiverem em baixa no mercado e revende-las quando o mercado estiver em alta. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. As questões a serem respondidas são:

Quais casas a House Rocket deveria comprar e por qual preço de compra?
Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?
Premissas do Negócio
As seguintes premissas foram consideradas para esse projeto:

Os valores iguais a zero em yr_renovated são casas que nunca foram reformadas.
O valor igual a 33 na coluna bathroom foi considerada um erro e por isso foi delatada das análises.
Os valores não inteiros nos atributos bathrooms e floors foram arrendados com o intuito de simplificar o projeto.
A coluna price significa o preço que a casa foi / será comprada pela empresa House Rocket.
Valores duplicados em ID foram removidos e considerados somente a compra mais recente.
A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel.
A estação do ano foi a característica decisiva para a época da venda do imóvel.
Planejamento do Projeto
Coleta de dados via Kaggle
Entendimento de negócio
Tratamento de dados
3.1. Tranformação de variaveis

3.2. Limpeza

3.3. Entendimento

Exploração de dados
Responder problemas do negócio
Resultados para o negócio
Conclusão
Ferramentas utilizadas
Python 3.8.0
Jupyter Notebook
Streamlit
Heroku
Conclusão
Os objetivos foram alcançados. Os imóveis foram agrupados por região (zipcode). Considerando o preço do imóvel e a condição minima como regular (3 - 5) foi calculado a mediana do preço. Ao total 10565 imóveis foram declarados como Imóveis com alto potencial de revenda, dentre estes foram sugeridos os 20 mais lucrativos para a empresa comprar. Os imóveis aptos para compra foram agrupados pela localidade e a estação do ano. A mediana foi calculada e imóveis com preço abaixo da mediana teve um acréscimo de 10% em seu valor, enquanto imóveis com preço acima da mediana teve um acréscimo de 30% acima do seu valor.

Proximos passos
Seria interessante analisar o potencial de lucratividade atraves de reformas para alguns imóveis baseados em sua localização, comprando imoveis em condições ruins, reformando-os e revendendo-os com finalidade de avaliar qual tipo de reforma retornaria lucro para a empresa. Outra ideia seria a possibilidade de prever a valorização do imóvel, tirando o limitando de 4 estações para os valores dos imóveis, possibilitando uma margem de lucro maior.

Contato
Este Projeto for realizado e revisado por Leonardo Canuto Chaves, Administrador de Empresas:

Leonardo-Canuto - GitHub

Leonardo-Canuto - Instagram

Leonardo-Canuto - LinkedIn

