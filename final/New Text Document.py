'''

THIS APP IS A TEST DASH markdown
dash,html,table,markdown,table-design

'''


from dash import Dash,dash_table,html
import pandas as pd
#####TO DO READ DATA 

df = pd.read_csv('Names.csv')

####TO DO Create app
app = Dash(__name__)

table=dash_table.DataTable(
    id = 'table',
    data=df.to_dict('records'),pagesize=10,


### TO DO fill table
    columns=[
    {'id':'index','name':''},
    {'id':'name' , 'name':'Name'},
    {'id':'price','name':'Price'},
    {'id':'linkimage','name':'Photo',"presentation": "markdown"}],
    
    markdown_options={"html": True},

###TO DO desgin table
    style_table={"width": 500},
    style_cell={'textAlign': 'center'},
    style_header={
        'backgroundColor': 'rgb(30, 30, 30)',
        'border': '2px solid blue' ,
        'color':'white'
    },
    style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'border': '2px solid blue' ,
        'color': 'yellow'
    },
    )

####TO DO creat table  
### one column of table has markdown presentation 
### markdown presntation runs html codes
### 
app.layout=html.Div([table])


if __name__ == "__main__":
    app.run_server(debug=True)


###GOOD LUCK
