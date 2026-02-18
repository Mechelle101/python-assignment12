
import plotly.express as px
import plotly.data as pldata

# Task 3: Interactive Visualizations with Plotly
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

# Clean the data...
df["strength"] = (
  df["strength"]
    .str.replace(r"\+", "", regex=True)
    .str.split("-", n=1).str[0]
    .astype(float)
)

fig = px.scatter(
  df,
  x="strength",
  y="frequency",
  color="direction",
  title="Wind Strength VS Frequency",
  hover_data=["strength", "frequency", "direction"]
)

fig.write_html("wind.html", auto_open=True)
