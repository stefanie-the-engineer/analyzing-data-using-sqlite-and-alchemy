# Hawaiian Vacation

A trip to Hawaii is being planned and the task is to obtain the data and run some analytics to get some of the statistics related to the rainfall over the last year. The task was completed using SQLite as a database and Alchemy as the ORM to query the SQLite database. From here we created a couple of graphs using Pandas and Matplotlib. We have a Data Frame that depicts the general statistics, 2 bar graphs and a histogram. There is also a CSV in which we printed the results obtained from a query. The statistics that we obtained are outlined below.

## Get Date 1 Year Before Last Data Point in Database
![One_Year_Date](Images/1_Year_Date.png)

## Get All Precipitation Data Over The Year Starting From Last Data Point in Database (In CSV)
![Precipitation_Data_Over_Last_Year](Output/Precipitation_Data_Over_Year.csv)

## Data Frame Containing Data Over The Year Starting From Last Data Point in Database (Head Of First 20)
![Year_Precipitation_Data_Frame](Images/)

## Maximum Precipitation Data For Each Day Over The Year Starting From Last Data Point in Database (Head Of First 20)
![Maximum_Precipitation_Over_Year](Images/Precipitation_Maximum_Day_For_Year_Head_Data_Frame.png)

## Bar Chart Outlining The Highest Precipitation Over The Year Starting From Last Data Point In Database
![Bar_Chart_Precipitation_Data](Images/Precipitation_Bar_Chart.png)

## Precipitation Summary Statistics Spanning Entire Data Set Minus Precipitation With No Values
![Precipitation_Summary_Statistics_Entire_Data_Set](Images/Calculate_Temperature_Using_Vacation_Dates.png)

## Number Of All Weather Stations in Database
![Number_Of_Weather_Stations](Images/Station_Counts.png)

## Most Active Stations In Descending Order
![Most_Active_Weather_Stations](Images/)

## Statistics Of Most Active Station
![Most_Active_Weather_Station_Statistics](Images/)

## Most Active Station With Temperature Observations Data Frame
![Weather_Station_Temperature_Observations_Data_Frame](Images/)

## Histogram Of Most Active Station With Temperature Observations Data Frame
![Histogram_Most_Active_Weather_Station_Temperatures](Images/Temperature_Count_Histogram.png)

## Calculate Temperatures Function Example
![Calculate_Temperatures_Function_Statistics_Example](Images/Calculate_Temperature_Function_Example.png)

## Calculate Temperatures Function Using 1 Year Before Vacation (Custom Time Frame In Which We Plan The Vacation)
![Calculate_Temperatures_Function_Statistics_Vacation_Dates](Images/Calculate_Temperature_Using_Vacation_Dates.png)

## Bar Chart For Trip Average Temperature With Error Bar
![Bar_Chart_Trip_Average_With_Error_Bar](Images/Trip_Average_Temperature_With_Error.png)

## Weather Station Information Using 1 year Before Vacation (Custom Time Frame In Which We Plan The Vacation)
![Weather_Station_Information_Vacation_Dates](Images/Group_By_Station_Precipitation.png)
