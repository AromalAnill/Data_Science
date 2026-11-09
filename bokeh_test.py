from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# 1. Generate Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# ==========================================
# 2. Matplotlib (The Classic Workhorse)
# ==========================================
plt.figure(figsize=(7, 4))
plt.plot(x, y, label="Sine Wave", color="blue", linewidth=2)
plt.title("Matplotlib: Static Sine Wave", fontsize=14)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

print("Displaying Matplotlib plot... (Close window to proceed to Seaborn)")
plt.show()

# ==========================================
# 3. Seaborn (Beautiful Statistical Plots)
# ==========================================
sns.set_theme(style="darkgrid")
plt.figure(figsize=(7, 4))

sns.lineplot(x=x, y=y, color="crimson", label="Sine Wave", linewidth=2.5)
plt.title("Seaborn: Styled Sine Wave", fontsize=14)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

print("Displaying Seaborn plot... (Close window to proceed to Plotly)")
plt.show()

# ==========================================
# 4. Plotly (Interactive Web-based Charts)
# ==========================================
print("Opening Plotly chart in your browser...")
fig_plotly = px.line(
    x=x, y=y,
    labels={'x': 'X Axis', 'y': 'Y Axis'},
    title="Plotly: Interactive Sine Wave"
)
fig_plotly.show()

# ==========================================
# 5. Bokeh (Interactive Professional Dashboards)
# ==========================================
print("Opening Bokeh plot in your browser...")
# Output to a static HTML file
output_file("bokeh_sine_wave.html")
# Create a new plot with a title and axis labels
p = figure(title="Bokeh: Interactive Sine Wave", x_axis_label='X Axis', y_axis_label='Y Axis', width=700, height=400)

# Add a line renderer with legend and line thickness
p.line(x, y, legend_label="Sine Wave", line_width=2, color="green")

# Add a hover tool to make it interactive
p.add_tools(HoverTool(tooltips=[("X", "$x"), ("Y", "$y")]))

# Show the results
show(p)