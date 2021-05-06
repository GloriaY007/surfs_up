# Surf'n Shake Analysis

Analyzing weather data in Hawaii using Jupyter Notebook, SQLite, VS Code & Flask


## Climate Analysis
The purpose of this analysis was to address Mr. W. Avy's concerns about the weather in Hawaii, so that he may invest in the Surf n' Shake business venture that is planned for that location. We want to see if running a surf shop is sustainable year around. To address that concern, we took a look at the temperature statistics for June and December, to see if running a surf shop would be sustainable year around. 

In order to get the required data to perform the analysis, to get the temperature data, we ran two seperate queries. One query for the month of June and the other for December. Once we ran the queries, teh results of the queries (temperatures) were stored in a list, then converted into a data frame. With the created dataframe, we then get the summary statistics by using the .describe() method. 

The results were as follows:

- The results showed that for the month of June, the low (minimum) temperature is **64 degrees**, the high (maximum) temperature is **85 degrees**, and the average temperature is approximately **74.94 degrees**.

    ![June Summary Statistics](https://github.com/GloriaY007/surfs_up/blob/main/Resources/June_summary_statistics.PNG)

- The results showed that for the month of December, the low (minimum) temperature is **56 degrees**, the high (maximum) temperature is **83 degrees**, and the average temperature is approximately **71.04 degrees**.

    ![December Summary Statistics](https://github.com/GloriaY007/surfs_up/blob/main/Resources/December_summary_statistics.PNG)

The Standard deviation is **3.26** in June and **3.75** in December, making a **0.49** difference in the two different seasons. Although there seems that there are slighly more variation in temperatures for the temperatures in the month of December, there is no significant difference between the two standard deviations.

## Recommendation
From our data we can tell what our temperatures, year round, do not vary drastically. However, there are other attributes to the weather such as precipitation, wind, or cloudiness, that would complete this analyis and further reassure Mr. W. Avy in his decision. If we ran additional queries on these attributes we would have a better idea of  whether or not people would come and visit the shop. With more data for the area, we can run even more queries. From there we can decide how we would like to build the shop and what areas would make this a more prominent location for visitors to come.

