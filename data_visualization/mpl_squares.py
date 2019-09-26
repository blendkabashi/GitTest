import matplotlib.pyplot as plt

x_poi = list(range(1, 5001))
y_poi = [x**3 for x in x_poi]
plt.scatter(x_poi, y_poi, c=y_poi, cmap=plt.cm.Reds,
            s=50, edgecolors='none')

plt.tick_params(axis='both', labelsize=10)

plt.savefig('plotFig.png', bbox_inches='tight')