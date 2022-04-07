import plotly.figure_factory as ff
import statistics as st
import random
import pandas as pd
import csv

data = pd.read_csv("project.csv")

readingTime = data["reading_time"].tolist()

fig = ff.create_distplot([readingTime], ["reading_time"], show_hist=False)
# fig.show()

meanP = st.mean(readingTime)


print("Mean of Population:- ",meanP)


# --------------------------------------------- mean of 100 random data points for 1000 times -------------------------------------

dataList = []
meanList = []
def meanFinder():
    for i in range(0,100):
        value = random.choice(readingTime)
    
        dataList.append(value)

    mean = st.mean(dataList)
    return mean


for i in range(0,1000):
    setOfMeans = meanFinder()
    meanList.append(setOfMeans)
    

meanS = st.mean(meanList)

print("----------------------------------------")
print("Mean of sample:- ",meanS)