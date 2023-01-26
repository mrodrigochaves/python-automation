import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
import pandas as pd

# Carregar dados de custos da AWS a partir de um arquivo CSV
df = pd.read_csv("costs.csv", sep=";")

# Criar uma função para retornar o gráfico de barras de custos por serviço
def create_bar_chart(df):
    services = df['Service'].value_counts().index
    costs = df['Cost'].groupby(df['Service']).sum().values
    data = [go.Bar(x=services, y=costs, name='Costs')]
    layout = go.Layout(title='Costs by Service', xaxis={'title':'Service'}, yaxis={'title':'Costs'})
    return go.Figure(data=data, layout=layout)

# Criar a aplicação Dash
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='AWS Cost Dashboard'),
    dcc.Graph(id='bar-chart', figure=create_bar_chart(df)),
])

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
