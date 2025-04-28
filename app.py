# Save this file as app.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Sales": [150, 200, 250, 300, 400]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Sales by Day", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='day-dropdown',
        options=[{'label': day, 'value': day} for day in df['Day']],
        value='Monday'
    ),
    dcc.Graph(id='sales-graph')
])

# Callback to update graph
@app.callback(
    dash.dependencies.Output('sales-graph', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value')]
)
def update_graph(selected_day):
    filtered_df = df[df['Day'] == selected_day]
    fig = px.bar(filtered_df, x='Day', y='Sales', title=f'Sales on {selected_day}')
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
