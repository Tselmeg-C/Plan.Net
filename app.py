# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_cost = pd.read_csv('cost_media.csv')
print(df_cost)

fig1 = px.bar(df_cost, x="media", y=["Company A","Company B"], barmode="group")

df_monthly_cost_comA = pd.read_csv('cost_bymonth_company_a.csv')
print(df_monthly_cost_comA)
fig2 = px.line(df_monthly_cost_comA, x="month", y=['Magazines', 'Newspapers', 'Online', 'Out-of-home',
       'Postal mailings', 'Radio', 'TV'])

df_monthly_cost_comB = pd.read_csv('cost_bymonth_company_b.csv')
print(df_monthly_cost_comB)
fig3 = px.line(df_monthly_cost_comB, x="month", y=['Magazines', 'Newspapers', 'Online', 'Out-of-home',
       'Postal mailings', 'Radio', 'TV','Cinema'])

df_monthly_tv = pd.read_csv('cost_bymonth_mediafirst_TV.csv')
df_monthly_newspaper = pd.read_csv('cost_bymonth_mediafirst_Newspapers.csv')
df_monthly_online = pd.read_csv('cost_bymonth_mediafirst_Online.csv')
df_monthly_magazine = pd.read_csv('cost_bymonth_mediafirst_Magazines.csv')
df_monthly_cinema= pd.read_csv('cost_bymonth_mediafirst_Cinema.csv')
df_monthly_out_of_home = pd.read_csv('cost_bymonth_mediafirst_Out-of-home.csv')
df_monthly_post = pd.read_csv('cost_bymonth_mediafirst_Postal mailings.csv')
df_monthly_radio = pd.read_csv('cost_bymonth_mediafirst_Radio.csv')


df_monthly_tv['media']='TV'
df_monthly_newspaper['media']='Newspapers'
df_monthly_online['media']='Online'
df_monthly_magazine['media']='Magazine'
df_monthly_cinema['media']='Cinema'
df_monthly_out_of_home['media']='Out of home'
df_monthly_post['media']='Postal maillings'
df_monthly_radio['media']='Radio'

df_monthly = pd.concat([df_monthly_tv,
                        df_monthly_newspaper,
                        df_monthly_online,
                        df_monthly_magazine,
                        df_monthly_cinema,
                        df_monthly_out_of_home,
                        df_monthly_post,
                        df_monthly_radio],axis=0)
fig4 = px.line(df_monthly, x="month", y=["Company A","Company B"], facet_col='media',facet_col_wrap=4)

#fig10.add_trace(fig5, row=1, col=2)
#fig10.add_trace(fig6, row=2, col=1)
#fig10.add_trace(fig7, row=2, col=2)


app.layout = html.Div(children=[
    # first plot showing spending of two companies on different media
    html.Div([

        html.H1(children='Plan.Net Interview'),

        html.Div(children='''
            Dash: Cost on different media
        '''),

        dcc.Graph(
            id='cost_media',
            figure=fig1
        )
    ]),
    # second plot showing monthly cost of company A on different media
    html.Div([
        
        html.Div(children='''
            Dash: Monthly-Cost of Company A on different media
        '''),

        dcc.Graph(
            id='df_monthly_cost_comA',
            figure=fig2
        ),
    ]),
    # third plot showing monthly cost of company B on different media
    html.Div([
        
        html.Div(children='''
            Dash: Monthly-Cost of Company B on different media
        '''),

        dcc.Graph(
            id='df_monthly_cost_comB',
            figure=fig3
        ),
    ]),
    html.Div([
        
        html.Div(children='''
            Dash: Monthly-Cost on different media
        '''),

        dcc.Graph(
            id='df_monthly_cost_media',
            figure=fig4
        ),
    ]),
    
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
