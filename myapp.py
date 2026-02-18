
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Task 4: Use the gapminder dataset instead of stocks
df = pldata.gapminder(return_type='pandas')

# Task 4: creating a series of unique countries removing duplicates
countries = df["country"].drop_duplicates()

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
  dcc.Dropdown(
    # Task 4: had to change the id
    id="country-dropdown",
    # Task 4: dropdown for unique country list
    options=[{
      "label": c,
      "value": c
      } for c in countries],
    # Task 4: change the initial value
    value="Canada"
  ),
  # Task 4: changing the graph id
  dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
  # Task 4: change the output graph id and input dropdown id
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
# Task 4: changing the function parameter to use the selected country
def update_graph(country):
    # Task 4: filter the dataset to only the selected country
    filtered = df[df["country"] == country]
    
    # Task 4: plot year vs gdp per capita for that country
    fig = px.line(
      filtered, 
      x="year", 
      y="gdpPercap", 
      title=f"GDP per Capita Over Time - {country}"
    )
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True)
    
    
# Task 5: deploy to render.com
app = Dash(__name__)
server = app.server 
