import matplotlib.pyplot as plt 
import numpy as np
categories = ['Math', 'Science', 'English', 'History', 'Art']
men_scores = [85, 80, 78, 90, 88]
women_scores = [88, 85, 82, 87, 91]
n = len(categories)
ind = np.arange(n)
width = 0.35
fig, ax = plt.subplots (figsize=(10, 6))
bars1 = ax.bar(ind - width/2, men_scores, width, label='Men', color='green')
bars2 = ax.bar(ind + width/2, women_scores, width, label='Women', color='yellow')
ax.set_xlabel('Subjects')
ax.set_ylabel('Scores')
ax.set_title('Scores by gender and subject')
ax.set_xticks (ind)
ax.set_xticklabels (categories)
ax.legend()
def add_labels (bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
        add_labels (bars1)
        add_labels (bars2)
        plt.show()