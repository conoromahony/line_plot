import matplotlib.pyplot as plt

# This file displays a grid of the available matplotlib chart styles, so you can quickly look at the styles
# to determine which you like.  It writes the grid of styles to chart_styles.pdf, indicating the name of the
# style as the title of each chart in the grid.

# Some data to plot on the charts.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Available styles include: 'Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background',
# 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
# 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted',
# 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks',
# 'seaborn-white', 'seaborn-whitegrid', and 'tableau-colorblind10'
style_list = plt.style.available
grid_x = 5
grid_y = 6
i = 1

fig, ax = plt.subplots(grid_x, grid_y)
fig.set_size_inches(20, 15)

# This will iterate through the available styles.
for current_style in style_list:
    plt.style.use(current_style)
    plt.subplot(grid_x, grid_y, i)
    plt.title(current_style, fontsize=10, fontweight=0, color='grey', loc='left')
    plt.plot(input_values, squares, linewidth=3)
    i += 1

plt.savefig('chart_styles.pdf', bbox_inches='tight')
quit()