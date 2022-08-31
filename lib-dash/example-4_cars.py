from enum import auto
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import no_update
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__)

#Clear the layout, do not display exception until callback gets executed
app.config.suppress_callback_exceptions = True

auto_data = pd.read_csv(r'C:\Users\krzys\Desktop\Python\Projekty\03-Car-Automobile\automobileEDA.csv')

#Layout starts
app.layout = html.Div(children=[html.H1('Car Automobile Components', style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 24}),

                                #Outer division starts
                                html.Div([
                                            #First inner divsion for adding dropdown helper text for Selected Drive wheels
                                            html.Div(
                                                        [html.H2('Drive Wheels Type:', style={'margin-right': '2em'}),]
                                                    ),
                                                    dcc.Dropdown(id='demo-dropdown', 
                                                                 options=[
                                                                            {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                                                                            {'label': 'Front Wheel Drive', 'value': 'fwd'},
                                                                            {'label': 'Four Wheel Drive', 'value': '4wd'}                         
                                                                         ],
                                                                 value='rwd'                                                
                                                                ),

                                            #Second Inner division for adding 2 inner divisions for 2 output graphs 
                                            html.Div(
                                                        [
                                                            html.Div([ ], id='plot1'),
                                                            html.Div([ ], id='plot2')
                                                        ], 
                                                        style={'display': 'flex'}
                                                    ),


                                        ])
                                #Outer division ends

                                ]
                    )
#Layout ends

#Decorator
@app.callback([Output(component_id='plot1', component_property='children'),
               Output(component_id='plot2', component_property='children')],
               Input(component_id='demo-dropdown', component_property='value'))


#Callback function (gets called whenever the input property changes)
def display_selected_drive_charts(value):

    filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels', 'body-style'], as_index=False).mean()
    filtered_df = filtered_df

    fig1 = px.pie(filtered_df, values='price', names='body-style', title='Pie Chart')
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')

    return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig2)]

#Run the app
if __name__ == '__main__':
    app.run_server()