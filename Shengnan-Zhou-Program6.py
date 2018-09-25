# -------------------------------------------------
# CSCI 127, Lab 13
# Shengnan Zhou
# July 2, 2018
#
# This program contains two graphs of datas of
# immigrations.
# -------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def main():

    data_frame = pd.read_csv("immigration.csv")                 #create varible and read the file

    most_arrived = data_frame["Arrived"].max()                  #find the most number of people arriving a country
    most_arrived_country = ""                                   #create empty string for country
    most_arrived_year = ""                                      #create empty string for year
    for i in range(len(data_frame)):                            #loop through the file
        if data_frame.ix[i, "Arrived"] == most_arrived:         #when the number matches the max value
            most_arrived_country = data_frame.ix[i, "Country"]  #get the country with the max value
            most_arrived_year = data_frame.ix[i, "Year"]        #get the year with the max value
    print("\nThe country that most people arrived to seek refugee status and asylum is " + most_arrived_country + ", and the number is " + str(most_arrived) + ", in the year of " + str(most_arrived_year) + ".\n")



    # Figure 1 is a pie plot
    plt.figure("Immigration Pie Chart")                         #create plot and change the window title
    data_frame["Country"].value_counts()[:10].plot.pie(autopct='%1.0f%%')   #create pie plot
    plt.title("Popular Immigration Countries")          #show the chart title

    # Figure 2 is a bar plot
    plt.figure("Immigration Bar Chart")                         #create plot and change the window title
    data_object = data_frame.groupby("Year")                    #group the data by year
    condensed_data_frame = data_object.sum()                    #condense the data

    condensed_data_frame["Arrived"].plot.bar()                  #create bar plot
    plt.title("Numbers of Immigrations Arrived in Years")       #change title
    plt.xticks(np.arange(10), ("2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"))                                                            #change x-ticks
    plt.xlabel("Years")                                         #change x-label
    plt.ylabel("Population")                                    #change y-label



    plt.show()                                                  #show both plots

# -------------------------------------------------

main()
