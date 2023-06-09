'''
Salam 
In Code Pythoni Bra Search Dar SearchBox Site Digikala.ir Neveshteh Shode Ast.
Barnameh Dar Link :http://127.0.0.1:313 , Run Misheh
Link Ro Baz Koinid.
'''
from dash import Dash,dcc,html,callback,Output,Input,dcc,dash_table
import dash_bootstrap_components as dbc
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
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


def notfound():
        time.sleep(2) 
        '''
        Check the product list after search and load page
        If product dont found after search return True
        '''
        element=driver.find_elements(By.CSS_SELECTOR,".product-list_ProductList__emptyWrapper__Hh8Ij")
        if len(element)==1:
            return True


def scroll():
    '''
    scroll page for get and load data from server.
    '''
    time.sleep(1)
    i,k=0,500
    while len(driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI'))<80:  #For Scroll and load page for get complete data.
        i+=500
        k+=500
        time.sleep(0.6)
        driver.execute_script("window.scrollTo({},{});".format(i,k))
        time.sleep(0.2)


option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)


app = Dash(__name__,external_stylesheets=[dbc.themes.ZEPHYR])

header = html.H1(children='سلام بر سلام',style={'text-align':'center','color':'green','font-size':'20px'})
searcht=html.H1(children='لطفا کلید واژه ی جستجو را وارد کنید ',style={'text-align':'center','color':'green','font-size':'16px'})
warn=html.H1(children='ممکن است فرایند دریافت اطلاعات و نمایش اندکی زمانبر باشد ',style={'text-align':'center','color':'black','font-size':'12px'})
searchbox=dbc.Input(id='searchbox',value='',
        style={'text-align':'center','color':'green','font-size':'16px','width':'500px','padding': '10px','margin':'auto','border': '3px solid green'})
searchbuttom=dbc.Button('seacrh',id='buttom',className='text-center',n_clicks=0,
        style={'text-align':'center','color':'white','background-color':'green','border': '1px solid black','width':'100px','margin':'auto'})
section = html.Section(style={'height':'5px'})


data = html.Div()


@callback(
    Output(data,component_property='children'),
    Output(searchbuttom,component_property='n_clicks'),
    Input(searchbuttom,component_property='n_clicks'),
    Input(searchbox,component_property='value')
)

def updates(n_clicks,value):
    content=[]
    if n_clicks > 0: 
        url = "https://www.digikala.com/search/?q={}".format(value)
        site=driver.get(url)

        check= notfound()
        if check == True:
            content=[]
            content.append(html.Center(children='عزیزجان،کالایی با این مشخصات پیدا نکردیم',style={'text-align':'center','color':'green','font-size':'14px'}))
            content.append(html.Center(children='پیشنهاد می‌کنیم کلید واژه جستجو را تغییر دهید',style={'text-align':'center','color':'black','font-size':'12px'}))
        if check != True:
            content=[]
        #........................................................................................................#
            scroll()
        #........................................................................................................#
            time.sleep(0.5)
            elements=driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
            data=list()
            index=1
            for element in elements[0:50]:
                datadic=dict()
        #--------------------------------------------------------------------------------------------------------------#find index and name 
              ##  index=element.get_attribute('data-product-index')             bug                                    # get data-product-index from each elements
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
                index+=1
        #........................................................................................................#


            # WRITE DATA in csv format
            csv_columns = ['index','name','prolink','price','img','link']
            csv_file = "data.csv "
            with open(csv_file, 'w', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for i in data:
                        writer.writerow(i)
            #........................................................................................................#
            # Read data in csv formate , create table and chart. 

            df = pd.read_csv('data.csv')
            content.append(html.Center([
            dash_table.DataTable(
            id = 'table',
            data=df.to_dict('records'),page_size=6,


        ### TO DO fill table
            columns=[
            {'id':'prolink','name':'لینک مستقیم',"presentation": "markdown"},
            {'id':'img','name':'تصویر',"presentation": "markdown"},
            {'id':'price','name':"(قیمت)تومان"},
            {'id':'name' , 'name':'نام محصول'},
            {'id':'index','name':'شماره'},
    ],
            
            markdown_options={"html": True,"link_target":"_self"},

        ###TO DO desgin table
            style_table={"width":500},
            style_header={
                'backgroundColor': 'green',
                'border': '0.5px solid black' ,
                'font_size': '12px',
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
            # TO DO create chart with matplotlib
            fig,ax1 = plt.subplots()
            ax1.plot(df['index'],df['price'],color='green',linewidth=1)
            ax1.set_xlabel('شماره محصول', color='green')
            ax1.set_ylabel("(قیمت)تومان", color='green')
            ax1.tick_params(labelcolor='tab:green')
            ax1.grid(color='black', linestyle='--', linewidth=0.5)
            plotly_fig = mpl_to_plotly(fig)

            content.append(
                html.Center(
                dcc.Graph(figure=plotly_fig,style={'width': '150vh', 'height': '150vh'})
                )
                
            )
        n_clicks = 0
        return content,n_clicks

app.layout=html.Center([
    html.Center(children=[header,searcht,warn,searchbox],className='text-center'),
    html.Center(children=[section,searchbuttom],className='text-center'),
    html.Center(children=[section,data])


])   

if __name__ == '__main__':
    app.run_server(port=313)

'''
Team Members :
            Morteza Hashemizade 
            Shima Beiranvand
            Mohamamd Najafi

'''