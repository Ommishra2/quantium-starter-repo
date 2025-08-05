import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load and prepare data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

regions = ['all', 'north', 'east', 'south', 'west']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "fontFamily": "Trebuchet MS, Arial, sans-serif",
            "letterSpacing": "2px",
            "marginTop": "15px"
        }
    ),
    html.Div([
        html.Label(
            "Select Region:",
            style={
                "fontWeight": "bold",
                "color": "#34495e",
                "marginRight": "20px",
                "fontSize": "20px"
            }
        ),
        dcc.RadioItems(
            id='region-selector',
            options=[{"label": region.capitalize(), "value": region} for region in regions],
            value='all',
            labelStyle={
                "display": "inline-block",
                "marginRight": "20px",
                "fontSize": "18px",
                "color": "#2680c2"
            },
            inputStyle={"marginRight": "8px"}
        )
    ], style={
        "textAlign": "center",
        "background": "#e9f5ff",
        "borderRadius": "8px",
        "padding": "18px 0",
        "boxShadow": "0 2px 8px #B3C8D9"
    }),
    html.Div([
        dcc.Graph(id='sales-line-chart')
    ], style={
        "background": "white",
        "borderRadius": "13px",
        "marginTop": "25px",
        "padding": "28px",
        "boxShadow": "0 6px 22px rgba(44, 62, 80, 0.11)"
    })

], style={
    "background": "linear-gradient(135deg, #F8FFFE 0%, #E2ECF2 100%)",
    "padding": "40px",
    "minHeight": "100vh"
})

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region',
        title="Pink Morsel Sales Over Time",
        labels={'date': 'Date', 'sales': 'Sales Amount'},
        template="plotly_white"
    )

    fig.add_vline(
        x=pd.Timestamp('2021-01-15'),
        line_dash="dash",
        line_color="red"
    )

    if not filtered_df.empty:
        fig.add_annotation(
            x=pd.Timestamp('2021-01-15'),
            y=filtered_df['sales'].max(),
            text="Price Increase (15 Jan 2021)",
            showarrow=True,
            arrowhead=1,
            yanchor='top',
            font=dict(color="red")
        )

    fig.update_layout(
        plot_bgcolor="rgba(240,250,255,0.8)",
        paper_bgcolor="rgba(0,0,0,0)",
        title_font_size=23,
        legend_title="Region"
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)
