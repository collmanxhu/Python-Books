import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

""" subplots() can generate one or more plots in the same figure.
    fig represents the entire figure or collection of plots that are generated.
    ax represents a single plot in the figure and is the variable we’ll use most of the time.
    plot() try to plot the data it’s given in a meaningful way.
    plt.show() opens Matplotlib’s viewer and displays the plot.
    tick_params() styles the tick marks
"""
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
plt.show()
