import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the processed sales data (ensure formatted_data.csv exists!)
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Create the line chart with color by region
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales Amount"}
)

# Add vertical line for price increase (15 Jan 2021)
fig.add_vline(
    x=pd.Timestamp("2021-01-15"),
    line_dash="dash",
    line_color="red"
)

# Add a label for the price increase marker
fig.add_annotation(
    x=pd.Timestamp("2021-01-15"),
    y=df['sales'].max(),  # place the annotation at the top
    text="Price Increase (15 Jan 2021)",
    showarrow=True,
    arrowhead=1,
    yanchor="top",
    font=dict(color="red")
)

# Create Dash app layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
   app.run(debug=True)

