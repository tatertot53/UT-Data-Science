

```python

from matplotlib import pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import os
import seaborn as sns
%matplotlib inline


```


```python
#"C:\Users\ckent\Desktop\utDataAnalytics\pyber\Resources\city_data.csv"

ride_data_path = os.path.join("..","Pyber","Resources","ride_data.csv")
city_data_path = os.path.join("..","Pyber","Resources","city_data.csv")

ride_data = pd.read_csv(ride_data_path)
city_data = pd.read_csv(city_data_path)



```


```python
ride_data.head()



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>1/16/2016 13:49</td>
      <td>38.35</td>
      <td>5.403690e+12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>1/2/2016 18:42</td>
      <td>17.49</td>
      <td>4.036270e+12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>1/21/2016 17:35</td>
      <td>44.18</td>
      <td>3.645040e+12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>7/31/2016 14:53</td>
      <td>6.87</td>
      <td>2.242600e+12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>7/9/2016 4:42</td>
      <td>6.28</td>
      <td>1.543060e+12</td>
    </tr>
  </tbody>
</table>
</div>




```python
#find duplicate values creating "ValueError: cannot reindex from a duplicate axis" error
#after merging tables below:

#city_data['city'].value_counts()


```


```python
#remove duplicate value

city_data = city_data.drop_duplicates('city',keep = 'first')

```


```python
#combine data sets on column "city"

pyber_df = city_data.merge(ride_data, on='city')

pyber_df.head()




```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>8/19/2016 4:27</td>
      <td>5.51</td>
      <td>6.246010e+12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>4/17/2016 6:59</td>
      <td>5.54</td>
      <td>7.466470e+12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>5/4/2016 15:06</td>
      <td>30.54</td>
      <td>2.140500e+12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>1/25/2016 20:44</td>
      <td>12.08</td>
      <td>1.896990e+12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>8/9/2016 18:19</td>
      <td>17.91</td>
      <td>8.784210e+12</td>
    </tr>
  </tbody>
</table>
</div>



RIDE SHARING GROUP CALCULATIONS


```python
avg_fare = pyber_df.groupby('city')['fare'].mean()

num_rides_city = pyber_df.groupby('city')['ride_id'].count()

num_drivers_city = pyber_df.groupby('city')['driver_count'].first()

city_type = pyber_df.groupby('city')['type'].first()

tot_fare_city = pyber_df.groupby('city')['fare'].sum()


data_calculated = pd.DataFrame({"fare":avg_fare,
                               "rides":num_rides_city,
                               "drivers":num_drivers_city,
                               "type":city_type,
                               "total fare":tot_fare_city
                               })

data_calculated.head()



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>drivers</th>
      <th>fare</th>
      <th>rides</th>
      <th>total fare</th>
      <th>type</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>21</td>
      <td>23.928710</td>
      <td>31</td>
      <td>741.79</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>67</td>
      <td>20.609615</td>
      <td>26</td>
      <td>535.85</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>16</td>
      <td>37.315556</td>
      <td>9</td>
      <td>335.84</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>21</td>
      <td>23.625000</td>
      <td>22</td>
      <td>519.75</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>49</td>
      <td>21.981579</td>
      <td>19</td>
      <td>417.65</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>



BUBBLE PLOT OF RIDE SHARING DATA



```python
urban = data_calculated[data_calculated['type'] == "Urban"]
suburban = data_calculated[data_calculated['type'] == "Suburban"]
rural = data_calculated[data_calculated['type'] == "Rural"]
plt.axes([1.025,1.025,1.95,1.95])


plt.scatter(urban['rides'],urban["fare"], color = 'Coral', edgecolors = 'black', s = urban['drivers']*20,
            label = 'Urban', alpha = .75, linewidths=1.25)
plt.scatter(suburban['rides'],suburban["fare"], color = 'LightSkyBlue', edgecolors = 'black', s = suburban['drivers']*20,
           label = 'Suburban', alpha = .75, linewidths=1.25)
plt.scatter(rural['rides'],rural["fare"], color = 'Gold', edgecolors = 'black', s = rural['drivers']*20, 
             label = 'Rural', alpha = .75, linewidths=1.25)

plt.legend(loc = 'upper right', fontsize = 'large', title="City Types",)
plt.title("Pyber Ride Sharing Data (2016)", fontsize = 'xx-large')
plt.ylabel("Average Fare ($)", fontsize = 'x-large')
plt.xlabel("Total Number of Rides (Per City)", fontsize = 'x-large')
plt.text(37,35,"Note:\nCircle size correlates with number of drivers per city", fontsize = 'x-large')


plt.grid()
plt.show()
```


![png](output_9_0.png)


GROUP BY CITY TYPE


```python
city_type_sorted = data_calculated.groupby('type')

city_type_df = pd.DataFrame()

city_type_df['Total Rides'] = city_type_sorted["rides"].sum()
city_type_df['Total Drivers'] = city_type_sorted["drivers"].sum()
city_type_df['Total Fare'] = city_type_sorted["total fare"].sum()
city_type_df.reset_index(inplace=True)
city_type_df.head()


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>Total Rides</th>
      <th>Total Drivers</th>
      <th>Total Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rural</td>
      <td>125</td>
      <td>104</td>
      <td>4255.09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Suburban</td>
      <td>625</td>
      <td>635</td>
      <td>19317.88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Urban</td>
      <td>1625</td>
      <td>2607</td>
      <td>40078.34</td>
    </tr>
  </tbody>
</table>
</div>



TOTAL FARES BY CITY TYPE


```python
colors = {"Urban":"Coral","Suburban":"LightSkyBlue","Rural":"Gold"}

explode_dict = {"Urban":0.1,"Suburban":0,"Rural":0}
city_type_df["explode"] = [explode_dict[x] for x in city_type_df["type"]]
city_type_df["colors"] = [colors[x] for x in city_type_df["type"]]

city_type_df.plot(kind="pie",y="Total Fare", autopct='%1.1f%%',
                  startangle=120, shadow=True, explode=city_type_df.explode,
                  colors=city_type_df.colors, labels=city_type_df.type, legend=False,
                  wedgeprops = { 'linewidth' : 1 , 'edgecolor' : 'lightgrey'}
                 )

plt.axis('off')
plt.axis('equal')

plt.title('% of Total Fares by City Type')

plt.show()
```


![png](output_13_0.png)


TOTAL RIDES BY CITY TYPE


```python
colors = {"Urban":"Coral","Suburban":"LightSkyBlue","Rural":"Gold"}

explode_dict = {"Urban":0.1,"Suburban":0,"Rural":0}
city_type_df["explode"] = [explode_dict[x] for x in city_type_df["type"]]
city_type_df["colors"] = [colors[x] for x in city_type_df["type"]]

city_type_df.plot(kind="pie",y="Total Rides", autopct='%1.1f%%',
                  startangle=120, shadow=True, explode=city_type_df.explode,
                  colors=city_type_df.colors, labels=city_type_df.type, legend=False,
                  wedgeprops = { 'linewidth' : 1 , 'edgecolor' : 'lightgrey'}
                 )

plt.axis('off')
plt.axis('equal')

plt.title('% of Total Rides by City Type')

plt.show()
```


![png](output_15_0.png)


TOTAL DRIVERS BY CITY TYPE


```python
city_type_df["explode"] = [explode_dict[x] for x in city_type_df["type"]]
city_type_df["colors"] = [colors[x] for x in city_type_df["type"]]

city_type_df.plot(kind="pie",y="Total Drivers", autopct='%1.1f%%',
                  startangle=120, shadow=True, explode=city_type_df.explode,
                  colors=city_type_df.colors, labels=city_type_df.type, legend=False,
                  wedgeprops = { 'linewidth' : 1 , 'edgecolor' : 'lightgrey'}
                 )

plt.axis('off')
plt.axis('equal')

plt.title('% of Total Drivers by City Type')

plt.show()
```


![png](output_17_0.png)


OBSERVABLE TRENDS:
    1. Pyber is much more widely used in Urban areas.
    2. Rural and Suburban areas contribute a higher percentage of the total Pyber Fare revenue due to having fewer drivers 
    and higher relative fares per ride.
    3. Rural areas have more rides than drivers, creating a higher relative cost per ride.
    
    
    
