import pandas as pd
import geopandas
import streamlit as st
import numpy as np
import plotly.express as px
import folium
import time
from PIL import Image
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

(pd.set_option('display.float_format', lambda x: '%.3f' % x))
st.set_page_config( layout='wide')

image = Image.open('HRC.png')
st.sidebar.image(image, use_column_width=True)

options = st.sidebar.radio('Selecione uma seção do Projeto para visitar.', (
'Estudo', 'Estatística Descritiva', 'Densidade de Portfólio','Análises Hipoteses','Avaliação Negócio'))
if options == 'Estudo':
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i + 1)
    st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
    link = '[SejaUmDataScientist](hhttps://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)'
    st.write(
        'Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog Seja um Data Scientist, para mais informações clique no link a seguir.')
    st.markdown(link, unsafe_allow_html=True)
    st.header('Descrição')
    st.write(
        'House Rocket é uma empresa do ramo imobiliario que procura novos imóveis para seu catalogo, fomentada pela alta e baixa recorrente do mercado imobiliario a empresa busca novas oportunidades de compra de imóveis. A empresa procurou um Cientista de dados para ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em condições regulares quando estiverem em baixa no mercado e revende-las quando o mercado estiver em alta. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. As questões a serem respondidas são:')
    st.write('1. Quais casas a House Rocket deveria comprar e por qual preço de compra?')
    st.write(
        '2. Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?')
    st.header('Premissas do Negócio')
    st.write('As seguintes premissas foram consideradas para esse projeto:')
    st.write('- Os valores iguais a zero em yr_renovated são casas que nunca foram reformadas.')
    st.write('- O valor igual a 33 na coluna bathroom foi considerada um erro e por isso foi delatada das análises.')
    st.write(
        '- Os valores não inteiros nos atributos bathrooms e floors foram arrendados com o intuito de simplificar o projeto.')
    st.write('- A coluna price significa o preço que a casa foi / será comprada pela empresa House Rocket.')
    st.write('- Valores duplicados em ID foram removidos e considerados somente a compra mais recente.')
    st.write('- A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel.')
    st.write('- A estação do ano foi a característica decisiva para a época da venda do imóvel.')
    st.header('Planejamento do Projeto')
    st.write('1. Coleta de dados via Kaggle')
    st.write('2. Entendimento de negócio')
    st.write('3. Tratamento de dados')
    st.write('3.1. Tranformação de variaveis')
    st.write('3.2. Limpeza')
    st.write('3.3. Entendimento')
    st.write('4. Exploração de dados')
    st.write('5. Responder problemas do negócio')
    st.write('6. Resultados para o negócio')
    st.write('7. Conclusão')
    st.header('Ferramentas utilizadas')
    st.write('- Python 3.8.0')
    st.write('- Jupyter Notebook')
    st.write('- Streamlit')
    st.write('- Heroku')
    st.header('Conclusão')
    st.write(
        'Os objetivos foram alcançados. Os imóveis foram agrupados por região (zipcode). Considerando o preço do imóvel e a condição minima como regular (3 - 5) foi calculado a mediana do preço. Ao total 10565 imóveis foram declarados como Imóveis com alto potencial de revenda, dentre estes foram sugeridos os 20 mais lucrativos para a empresa comprar. Os imóveis aptos para compra foram agrupados pela localidade e a estação do ano. A mediana foi calculada e imóveis com preço abaixo da mediana teve um acréscimo de 10% em seu valor, enquanto imóveis com preço acima da mediana teve um acréscimo de 30% acima do seu valor.')
    st.header('Proximos passos')
    st.write(
        'Seria interessante analisar o potencial de lucratividade atraves de reformas para alguns imóveis baseados em sua localização, comprando imoveis em  condições ruins, reformando-os e revendendo-os com finalidade de avaliar qual tipo de reforma retornaria lucro para a empresa. Outra ideia seria a possibilidade de prever a valorização do imóvel, tirando o limitando de 4 estações para os valores dos imóveis, possibilitando uma margem de lucro maior.')

    st.markdown("""
    <style>
    .big-font {
        font-size:14px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header('Contato')
    st.write('Este Projeto for realizado e revisado por Leonardo Canuto Chaves, Administrador de Empresas:')
    link2 = '[Leonardo-Canuto - GitHub](https://github.com/Leonardo-Canuto)'
    link3 = '[Leonardo-Canuto - Instagram](https://www.instagram.com/leonardocanutochaves)'
    link4 = '[Leonardo-Canuto - LinkedIn](https://www.linkedin.com/in/perfilleonardocanuto)'
    c1, c2 = st.beta_columns(2)
    with c1:
        st.markdown(link2, unsafe_allow_html=True)
        st.markdown(link3, unsafe_allow_html=True)
        st.markdown(link4, unsafe_allow_html=True)
#    with c2:
#        image2 = Image.open('Assets/Jiban.jpg')
#        c2.image(image2, caption='Jiban o Policial de Aço', width=130)

@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )
    return data

@st.cache(allow_output_mutation=True)
def get_df_buy(pathkc):
    df_buy = pd.read_csv(pathkc)
    return df_buy


@st.cache( allow_output_mutation=True )
def get_geofile( url ):
 geofile = geopandas.read_file( url )
 return geofile

# get geofile
url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
geofile = get_geofile( url )

#new atributes
def set_feature(data):
    data['price_m2'] = data['price'] / data['sqft_lot']
    data['sqm_lot'] = data['sqft_lot'] / 10.764
    data['sqm_living'] = data['sqft_living'] / 10.764
    return data

def overview_data(data):
    if options == 'Estatística Descritiva':
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)
        # =============================================
        #        DATA OVERVIEW
        # =============================================
        data = data1.copy()
        st.sidebar.title('Filtro de Atributos')
        f_attributes = st.sidebar.multiselect('Enter columns', data.columns)
        f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].unique())
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write(
            'Esta seção é destinada para olhar estatísticamente o conjunto de dados, analisando inicialmente algumas métricas para o entendimento do negócio.')


        if (f_zipcode != []) & (f_attributes != []):
            data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
        elif (f_zipcode != []) & (f_attributes == []):
            data = data.loc[data['zipcode'].isin(f_zipcode), :]
        if (f_zipcode == []) & (f_attributes != []):
            data = data.loc[:, f_attributes]
        else:
            data = data.copy()
        if st.checkbox('Mostrar a tabela geral de atributos'):
            st.header('Data Overview')
            st.dataframe(data)


        #  st.write(data.head())
        c1,c2 = st.beta_columns((1,1))
        # Average metrics
        if 'floors' or 'id' or 'zipcode' or 'price' or 'sqm_lot' or 'price_m2' or 'sqm_living' or 'lat' or 'long' or 'date' or 'bathrooms' or 'yr_built' or 'bedrooms' or 'sqft_living' or 'sqft_lot' or 'waterfront' or 'view' or 'condition' or 'grade' or 'sqft_above' or 'sqft_basement' or 'yr_renovated' or 'sqft_living15' or 'sqft_lot15' not in data:
            data['floors'] = data1['floors']
            data['id'] = data1['id']
            data['zipcode'] = data1['zipcode']
            data['price'] = data1['price']
            data['sqm_lot'] = data1['sqm_lot']
            data['price_m2'] = data1['price_m2']
            data['sqm_living'] = data1['sqm_living']
            data['lat'] = data1['lat']
            data['long'] = data1['long']
            data['date'] = pd.to_datetime(data1['date']).dt.strftime('%Y-%m-%d')
            data['bathrooms'] = data1['bathrooms']
            data['yr_renovated'] = data1['yr_renovated']
            data['yr_built'] = data1['yr_built']
            data['bedrooms'] = data1['bedrooms']
            data['sqft_living'] = data1['sqft_living']
            data['sqft_living15'] = data1['sqft_living15']
            data['sqft_lot'] = data1['sqft_lot']
            data['sqft_lot15'] = data1['sqft_lot15']
            data['waterfront'] = data1['waterfront']
            data['view'] = data1['view']
            data['condition'] = data1['condition']
            data['grade'] = data1['grade']
            data['sqft_above'] = data1['sqft_above']
            data['sqft_basement'] = data1['sqft_basement']

        df1 = data[['id','zipcode']].groupby('zipcode').count().reset_index()
        df2 = data[['price','zipcode']].groupby('zipcode').mean().reset_index()
        df3 = data[['sqft_living','zipcode']].groupby('zipcode').mean().reset_index()
        df4 = data[['price_m2','zipcode']].groupby('zipcode').mean().reset_index()

        #merge
        m1 = pd.merge(df1,df2, on='zipcode', how = 'inner')
        m2 = pd.merge(m1,df3, on='zipcode', how = 'inner')
        df = pd.merge(m2,df4, on='zipcode', how = 'inner')
        df.columns = ['ZIPCODE','ID','PRICE','SQRT LIVING','PRICE M/2']

        c1.header('Average Values')
        c1.dataframe(df, height=600)

        # Statistic Descriptive
        num_attributes = data.select_dtypes( include=['int64', 'float64'] )
        media = pd.DataFrame( num_attributes.apply( np.mean ) )
        mediana = pd.DataFrame( num_attributes.apply( np.median ) )
        std = pd.DataFrame( num_attributes.apply( np.std ) )

        max_ = pd.DataFrame( num_attributes.apply( np.max ) )
        min_ = pd.DataFrame( num_attributes.apply( np.min ) )

        df1 = pd.concat([max_, min_, media, mediana, std],axis=1 ).reset_index()
        df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

        c2.header( 'Descriptive Analysis' )
        c2.dataframe( df1, height=800 )

        return None


def portfolio_density(data,geofile):
    if options == 'Densidade de Portfólio':
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.5)
            progress.progress(i+1)
# =======================
# Densidade de Portfolio
# =======================
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write(
            'Esta seção é destinada a visualização geográfica do conjunto de dados, fornecendo um olhar sobre a densidade do portfólio e a densidade de preço do portfólio.')
        st.title('Region Overview')
        # c1,c2 = st.beta_columns((2))
        st.header('Portfólio Density')

        # Base Map = Folium
        density_map = folium.Map(location=[data['lat'].mean(),
                                           data['long'].mean()],
                                 default_zoom_start=15)
        marker_cluster = MarkerCluster().add_to(density_map)
        for name, row in data.iterrows():
            folium.Marker([row['lat'], row['long']],
                          popup='Sold R${0} on: {1} Sqm Living: {2} Bedrooms: {3} Bathrooms: {4}   Year Built: {5}'.format(
                              row['price'],
                              row['date'],
                              row['sqm_living'],
                              row['bedrooms'],
                              row['bathrooms'],
                              row['yr_built'])).add_to(marker_cluster)

        folium_static(density_map)

        # Region Price Map
        st.header('Price Density')

        df = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        df.columns = ['ZIP', 'PRICE']

        geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]

        region_price_map = folium.Map(location=[data['lat'].mean(),
                                                data['long'].mean()],
                                      default_zoom_start=15)

        region_price_map.choropleth(data=df,
                                    geo_data=geofile,
                                    columns=['ZIP', 'PRICE'],
                                    key_on='feature.properties.ZIP',
                                    fill_color='YlOrRd',
                                    fill_opacity=0.7,
                                    line_opacity=0.2,
                                    legend_name='AVG PRICE')

        folium_static(region_price_map)
        return None

def hipoteses(data):
    if options == 'Análises Hipoteses':
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i + 1)

        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write(
            'Esta seção é destinada analise de insights sobre o negócio, verificando a veracidade da hipótese criada com intuito descobrir novas oportunidades para a empresa.')
        st.header('Mas o que são Insights?')
        st.write(
            'Insight é um substantivo com origem no idioma inglês e que significa compreensão súbita de alguma coisa ou determinada situação, o Insight também está relacionado com a capacidade de discernimento, pode ser descrito como uma espécie de epifania. Nos desenhos, o insight é representado com o desenho de uma lâmpada acesa em cima da cabeça do personagem, indicando um momento único de esclarecimento em que se fez luz.')
        st.markdown("<h1 style='text-align: center; color: black;'>Testando Hipóteses de Negócio</h1>",
                    unsafe_allow_html=True)

        c1, c2 = st.beta_columns(2)

        c1.subheader('Hipótese 1:  Imóveis com vista para a água são em média 30% mais caros')
        c1.write(
            '- Falsa, como observado se comparado a média de preços do conjunto de dados, imóveis com vista para a água são em média 300% mais caros.')
        h1 = data[['price', 'waterfront', 'sqft_lot']].groupby('waterfront').mean().reset_index()
        h1['waterfront'] = h1['waterfront'].astype(str)
        fig = px.bar(h1, x='waterfront', y='price', color='waterfront', labels={"waterfront": "Visão para água",
                                                                                "price": "Preço"},
                     template='simple_white')

        fig.update_layout(showlegend=False)
        c1.plotly_chart(fig, use_container_width=True)
        # =========================================
        # ========== H2 ==========
        # ==========================================
        c2.subheader('Hipótese 2: Imóveis com data de construção menor que 1955 são em média 50% mais baratos')
        c2.write(
            '- Falsa, como observado imóveis com data de construção anteriores a 1955 são apenas 0.56% mais baratos que a média total dos imóveis.')
        data['construcao'] = data['yr_built'].apply(lambda x: '> 1955' if x > 1955
        else '< 1955')

        h2 = data[['construcao', 'price', 'sqft_lot']].groupby('construcao').mean().reset_index()

        fig2 = px.bar(h2, x='construcao', y='price', color='construcao', labels={"contrucao": "Ano da Construção",
                                                                                 'price': 'Preço'},
                      template='simple_white')

        fig2.update_layout(showlegend=False)
        c2.plotly_chart(fig2, use_container_width=True)
        # =========================================
        # ========== H3 ==========
        # ==========================================
        c3, c4 = st.beta_columns(2)

        c3.subheader('Hipótese 3: Imóveis sem porão possuem área total 40% maiores que os imóveis com porão.')
        c3.write(' - Verdadeira, como observado imóveis sem porão são em édia 89% maiores que imóveis com porão.')
        data['porao'] = data['sqft_basement'].apply(lambda x: 'nao' if x == 0
        else 'sim')

        h3 = data[['porao', 'sqm_lot', 'price']].groupby('porao').sum().reset_index()
        fig3 = px.bar(h3, x='porao', y='sqm_lot', color='porao', labels={'price': 'Preço',
                                                                         'sqm_lot': 'Área Total'},
                      template='simple_white')
        fig3.update_layout(showlegend=False)
        c3.plotly_chart(fig3, use_container_width=True)

        # =========================================
        # ========== H4 ==========
        # ==========================================
        c4.subheader('Hipótese 4: Imóveis que nunca sofreram reformas são em média 30% mais baratos')
        c4.write(
            ' - Verdadeira, como observado imóveis que nunca sofreram reformas são 30.21% mais baratos que os imóveis que ja sofreram algum tipo de reforma.')
        data['renovacao'] = data['yr_renovated'].apply(lambda x: 'sim' if x > 0 else
        'nao')

        h6 = data[['price', 'renovacao']].groupby('renovacao').mean().reset_index()
        fig4 = px.bar(h6, x='renovacao', y='price', color='renovacao', labels={'renovacao': 'Renovação',
                                                                               'price': 'Preço'},
                      template='simple_white')
        fig4.update_layout(showlegend=False)
        c4.plotly_chart(fig4, use_container_width=True)
    return None

def evaluate_house(df_buy):
    if options == 'Avaliação Negócio':
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.5)
            progress.progress(i+1)

        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write(
            'Como mencionado anteriormente a House Rocket é uma empresa que trabalha com o ramo imobiliário, focada na compra e venda de imóveis, a empresa busca as melhores oportunidades de compra dentro do mercado, para futuramente revender quando o mercado estiver em alta. Diante disto o trabalho do Cientista de dados da empresa é de orientar e propor as melhores alternativas, ajudando assim a empresa encontrar as melhores oportunidades de negócio.')
        st.markdown("<h1 style='text-align: center; color: black;'> Questões de Negócio</h1>", unsafe_allow_html=True)
        st.subheader('Quais são os imóveis que a House Rocket deveria comprar e por qual preço?')
        st.write(
            'Através do portfólio disponibilizado pela empresa e com base na mediana de preço de cada região e na condição dos imóveis, foram encontradas 10505 imovéis com alto potencial de venda.')

        data1 = df_buy[['zipcode', 'price']].groupby('zipcode').median().reset_index()
        data1.columns = ['zipcode','median_regiao']
        data2 = pd.merge(data,data1, on = 'zipcode', how='inner')
        for i in range(len(data2)):
            if (data2.loc[i, 'price'] < data2.loc[i, 'median_regiao']) & (data2.loc[i, 'condition'] >= 3):
                data2.loc[i, 'Status'] = 'Buy'
            else:
                data2.loc[i, 'Status'] = 'Not buy'

        data2['date'] = pd.to_datetime(data2['date']).dt.strftime('%Y-%m-%d')
        data2['month'] = pd.to_datetime(data2['date']).dt.strftime('%m').astype(int)
        data2['season'] = data2['month'].apply(lambda x: 'spring' if (x >= 3) & (x < 6)
        else 'summer' if (x >= 6) & (x < 9)
        else 'fall' if (x >= 9) & (x < 12)
        else 'winter')

        st.write(
            'Anexo aqui todas as possibilidades de compras oferecidas a House Rocket.')

        tbcompra = data2.loc[data2['Status'] == 'Buy',:]
        st.dataframe(tbcompra)

        data3 = data2[['season', 'price']].groupby('season').median().reset_index()
        data3.columns = ['season', 'Mediana_Seasons']
        # print(data3)
        data4 = pd.merge(data2, data3, on='season', how='inner')
        # print(data4)
        for i in range(len(data4)):
            if (data4.loc[i, 'price'] < data4.loc[i, 'Mediana_Seasons']) & (data4.loc[i, 'Status'] == 'Buy'):
                data4.loc[i, 'sale price'] = data4.loc[i, 'price'] * 1.30
            elif (data4.loc[i, 'price'] > data4.loc[i, 'Mediana_Seasons']) & (data4.loc[i, 'Status'] == 'Buy'):
                data4.loc[i, 'sale price'] = data4.loc[i, 'price'] * 1.10
            else:
                data4.loc[i, 'sale price'] = 0
        data4['profit'] = data4['sale price'] - data4['price']

        data5 = data4[
            ['id', 'date', 'price', 'condition', 'median_regiao', 'Status', 'season', 'Mediana_Seasons', 'sale price',
             'profit']].sort_values('profit', ascending=False)
        data6 = data5.head(20)
        st.subheader('Uma vez o imóvel comprado, qual o melhor momento para vende-lo? e por qual preço?')
        st.write('Para a venda dos imóveis comprados, foi analisado o comportamento dos preços para o ano anterior, buscando qual seria a melhor estação do ano para vender o imóvel, para isso foi realizado a mediana dos preços para cada região durante cada estação do ano, diante disso se o preço pelo qual o imóvel foi comprado fosse menor que a mediana da estação o imóvel seria vendido pelo preço que foi comprado +30%, e caso o preço de aquisição fosse maior que a mediana de estação o valor de venda seria o valor da compra + 10%.')
        st.markdown("<h1 style='text-align: center; color: black;'> Sugestão de compra de imóveis</h1>", unsafe_allow_html=True)
        st.write('Após a analise de melhor periodo para venda o Cientista de dados elencou os 20 imóveis mais lucrativos e sugeriu que a empresa devesse adquiri-los.')
        st.write('Ao final foi disponibilizado uma tabela para a equipe de negócios, com todos os dados referentes a venda dos imóveis, incluindo o lucro esperado em quais estações vender o determinado imóvel.')

        st.dataframe(data6)


    return None


if __name__ == '__main__':
    path = 'kc_house_data.csv'
    pathkc = 'kc_house.csv'
    data = get_data(path)
    data1 = get_data(path)
    df_buy = get_df_buy(pathkc)
    set_feature(data)
    overview_data(data)
    portfolio_density(data,geofile)
    hipoteses(data)
    evaluate_house(df_buy)


