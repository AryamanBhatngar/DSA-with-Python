import matplotlib.pyplot as plt
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Ruby']
popularity = [85, 80, 75, 70, 65, 50]
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color='purple')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.show()