import csv
import numpy as np
import matplotlib.pyplot as plt

# figure out what data we want to use
categories = []  # column headers from excel data
installs = []  # installs row
ratings = []  # ratings row

with open('data/googeplaystore.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        # move page column headers out of actual data to get clean dataset
        if line_count is 0:  # this will be text, not data
            print('pushing categories into a seperate array')
            categories.append(row)  # push text into this array
            line_count += 1  # increment the line count for next loop
        else:
            ratingsData = row[2]
            ratingsData = ratingsData.replace("NaN","0")
            ratings.append(float(ratingsData))
            # Int will turn text into number
            # print('pushing ratings data info the ratings array')
            installData = row[5]
            installData = installData.replace(",", "")  # get rid of commas
            installs.append(np.char.strip(installData, "+"))  # get rid of trailing +
            line_count += 1

#  get some values we can work with
#  how many ratings are 4+?
#  how many are below 2?
#  how many are in the middle?
np_ratings = np.array(ratings)  # turn a plain python list into numpy array
popular_apps = np_ratings > 4
print("popular apps:", len(np_ratings[popular_apps]))

percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(percent_popular)

unpopular_apps = np_ratings < 4
print("unpopular apps:", len(np_ratings[unpopular_apps]))

percent_unpopular = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100
print(percent_unpopular)

kinda_popular = 100 - (percent_popular + percent_unpopular)
print(kinda_popular)

# do a visualization with our shiny new data
labels = "Sucks", "Meh", "Love it!"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Do we love us some apps?")
plt.xlabel("User Ratings - App Installs (10,000+ apps)")
plt.show()