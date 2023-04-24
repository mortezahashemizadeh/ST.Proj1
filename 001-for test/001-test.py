from dash import Dash,dcc,html,callback,Output,Input,dcc,dash_table,State
import pandas as pd 
import dash_bootstrap_components as dbc
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import plotly.express as px
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly

def numberdecode(number):
    '''
    Change persian number to latin nnumber 
    input :'۳,۰۱۸,۶۰۰' type>> str
    output:3018600 type >> int
    '''
    number=number.replace(',','') ### replace ',' to '' so remove ',' from str
    from unidecode import unidecode 
    return int(unidecode(number)) ### english number





app = Dash(__name__,external_stylesheets=[dbc.themes.YETI])

header = html.Header(children='سلام بر سلام',style={'text-align':'center','color':'green','font-size':'16px'})
searcht=html.H1(children='لطفا کلید واژه ی سرچ  خود را وارد کنید ',style={'text-align':'center','color':'green','font-size':'16px'})
searchbox=dbc.Input(id='searchbox',value='',
        style={'text-align':'center','color':'green','font-size':'16px','width':'500px','padding': '10px','margin':'auto','border': '3px solid green'})
searchbuttom=dbc.Button('seacrh',id='buttom',className='text-center',n_clicks=0,
        style={'text-align':'center','color':'white','background-color':'green','border': '1px solid black','width':'100px','margin':'auto'})
section = html.Section(style={'height':'5px'})


data = html.Div()
#footer= dbc.CardFooter(children='این نرم افزار با پایتون طراحی شده است',style={'text-align':'center','color':'green','size':'16px','margin':'auto','background-color':'grean'})

@callback(
    Output(data,component_property='children'),
    Output(searchbuttom,component_property='n_clicks'),
    Input(searchbuttom,component_property='n_clicks'),
    Input(searchbox,component_property='value')
)

def updates(n_clicks,value):
    if n_clicks > 0: 
        content=[]
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        site=driver.get("https://www.digikala.com/search/?q={}".format(value))
        #........................................................................................................#
        time.sleep(5)
        i,k=0,500
        while len(driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI'))<80:  #For Scroll and load page for get complete data.
            i+=500
            k+=500
            time.sleep(0.8)
            driver.execute_script("window.scrollTo({},{});".format(i,k))
            time.sleep(0.2)
        #........................................................................................................#
        time.sleep(1)
        elements=driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
        time.sleep(0.3)

        data=list()
        time.sleep(5)
        data=list()
        for element in elements[0:51]:
            datadic=dict()
            #--------------------------------------------------------------------------------------------------------------#find index and name 
            index=element.get_attribute('data-product-index')                                                 # get data-product-index from each elements
            title=element.find_element(By.TAG_NAME,'a')                                                       #find a tag name from each elements
            name= title.find_element(By.TAG_NAME,'h3').get_attribute('innerHTML')                             # find h3 tag_name  then get inner html from each "a"
            
        
        #--------------------------------------------------------------------------------------------------------------#Find Image Link
            imgname = element.find_element(By.TAG_NAME,'picture').find_element(By.TAG_NAME,'img')             #
            linkimage=imgname.get_attribute('data-src')
        #--------------------------------------------------------------------------------------------------------------#Find Price
            price_el=element.find_element(By.CSS_SELECTOR,".d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1").find_element(By.TAG_NAME,'span')
            price=price_el.get_attribute('innerHTML')
        #--------------------------------------------------------------------------------------------------------------# Find Link
            link = element.find_element(By.TAG_NAME,'a').get_attribute('href')


        #--------------------------------------------------------------------------------------------------------------# WRITE Data in dict then append to mother list
            ####add each data to dict 
            datadic['index']=index
            datadic['name']=name
            datadic['prolink']='[{}]({})'.format('لینک',link)
            datadic['link']=link
            datadic['price']=numberdecode(price)
            datadic['img']="<img src='{}' height='100' />".format(linkimage)
            data.append(datadic)
          #........................................................................................................#


        # WRITE DATA in csv format
        csv_columns = ['index','name','prolink','price','img','link']
        csv_file = "data.csv "
        with open(csv_file, 'w', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for i in data:
                    writer.writerow(i)
        df = pd.read_csv('data.csv')
        content.append(html.Center([
        dash_table.DataTable(
        id = 'table',
        data=df.to_dict('records'),page_size=6,


    ### TO DO fill table
        columns=[
        {'id':'prolink','name':'لینک مستقیم',"presentation": "markdown"},
        {'id':'img','name':'تصویر',"presentation": "markdown"},
        {'id':'price','name':"قیمت تومان"},
        {'id':'name' , 'name':'نام محصول'},
        {'id':'index','name':''},
],
        
        markdown_options={"html": True,"link_target":"_self"},

    ###TO DO desgin table
        style_table={"width":500},
        style_header={
            'backgroundColor': 'green',
            'border': '0.5px solid black' ,
            'color':'white'
        },
        style_data={
            'backgroundColor': 'rgb(255, 255, 255)',
            'border': '0.5px solid black' ,
            'color': 'black',
            'size':'20px'
        },
        style_cell = {
            'font_size': '10px',
            'text_align': 'center',
            'padding-right': '20px', 
            'padding-left': '20px',
        }
        )])),
        fig,ax1 = plt.subplots()
        ax1.plot(df['index'],df['price'],color='green',linewidth=1)
        ax1.set_xlabel('شماره محصول', color='green')
        ax1.set_ylabel('قیمت تومان', color='green')
        ax1.tick_params(labelcolor='tab:green')
        ax1.set_facecolor('white')
        plotly_fig = mpl_to_plotly(fig)
        content.append(
             html.Center(
             dcc.Graph(figure=plotly_fig,style={'width': '150vh', 'height': '150vh'})
             )
            
        )
        return content,n_clicks

app.layout=html.Center([
    html.Center(children=[header,searcht,searchbox],className='text-center'),
    html.Center(children=[section,searchbuttom],className='text-center'),
    html.Center(children=[section,data])


])   



















if __name__ == '__main__':
    app.run_server(port=8000)