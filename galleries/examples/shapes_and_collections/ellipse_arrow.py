"""
===================================
Ellipse with orientation arrow demo
===================================

This demo shows how to draw an ellipse with
an orientation arrow (clockwise or counterclockwise).
Compare this to the :doc:`Ellipse collection example
</gallery/shapes_and_collections/ellipse_collection>`.
"""

import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.patches import Ellipse
from matplotlib.transforms import Affine2D


# Create a figure and axis
fig, ax = plt.subplots(1, 1, subplot_kw={"aspect": "equal"})

# Define an ellipse clockwise
center = (2, 4)
width = 30
height = 20
angle = 35
ellipse_clockwise = Ellipse(
    xy=center,
    width=width,
    height=height,
    angle=angle,
    facecolor="none",
    edgecolor="b",
    label="clockwise"
)

# Get position of vertex for arrow marker
vertices = ellipse_clockwise.get_co_vertices()

# Add the ellipse patch to the axis
ax.add_patch(ellipse_clockwise)

# Plot a arrow marker at the end point of minor axis
t = Affine2D().rotate_deg(ellipse_clockwise.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)

# Define an second ellipse counterclockwise
center = (2, 4)
width = 30
height = 15
angle = -20
ellipse_counterclockwise = Ellipse(
    xy=center,
    width=width,
    height=height,
    angle=angle,
    facecolor="none",
    edgecolor="g",
    label="counterclockwise"
)

# Add the ellipse patch to the axis
ax.add_patch(ellipse_counterclockwise)

# Get position of vertex for arrow marker
vertices = ellipse_counterclockwise.get_co_vertices()

# Plot a arrow marker at the end point of minor axis
t = Affine2D().rotate_deg(ellipse_counterclockwise.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="g",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)


plt.legend()
plt.show()

center = (2, 4)
width = 30
height = 20
angle = 35
ellipse = Ellipse(
    xy=center,
    width=width,
    height=height,
    angle=angle
)
print(ellipse.get_vertices())
print(ellipse.get_co_vertices())

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.patches`
#    - `matplotlib.patches.Ellipse`
