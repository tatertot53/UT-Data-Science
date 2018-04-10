

```python
import pandas as pd
import os
import dateutil
import datetime


```

# Cleaning Hawaii Measurements CSV


```python
measurement_data = pd.read_csv('Resources/hawaii_measurements.csv',encoding="iso-8859-1")
measurement_data.head()


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
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>1/1/2010</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>1/2/2010</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>1/3/2010</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>1/4/2010</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>1/6/2010</td>
      <td>NaN</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>




```python
measurement_data.shape
```




    (19550, 4)




```python
measurement_data.duplicated().sum()
```




    0




```python
measurement_data.isnull().sum()
```




    station       0
    date          0
    prcp       1447
    tobs          0
    dtype: int64




```python
measurement_data['prcp'].fillna(0, inplace=True)
measurement_data


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
      <th>station</th>
      <th>date</th>
      <th>prcp</th>
      <th>tobs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>1/1/2010</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>1/2/2010</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>1/3/2010</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>1/4/2010</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>1/6/2010</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519397</td>
      <td>1/7/2010</td>
      <td>0.06</td>
      <td>70</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519397</td>
      <td>1/8/2010</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00519397</td>
      <td>1/9/2010</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00519397</td>
      <td>1/10/2010</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
    <tr>
      <th>9</th>
      <td>USC00519397</td>
      <td>1/11/2010</td>
      <td>0.01</td>
      <td>64</td>
    </tr>
    <tr>
      <th>10</th>
      <td>USC00519397</td>
      <td>1/12/2010</td>
      <td>0.00</td>
      <td>61</td>
    </tr>
    <tr>
      <th>11</th>
      <td>USC00519397</td>
      <td>1/14/2010</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>12</th>
      <td>USC00519397</td>
      <td>1/15/2010</td>
      <td>0.00</td>
      <td>65</td>
    </tr>
    <tr>
      <th>13</th>
      <td>USC00519397</td>
      <td>1/16/2010</td>
      <td>0.00</td>
      <td>68</td>
    </tr>
    <tr>
      <th>14</th>
      <td>USC00519397</td>
      <td>1/17/2010</td>
      <td>0.00</td>
      <td>64</td>
    </tr>
    <tr>
      <th>15</th>
      <td>USC00519397</td>
      <td>1/18/2010</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
    <tr>
      <th>16</th>
      <td>USC00519397</td>
      <td>1/19/2010</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>17</th>
      <td>USC00519397</td>
      <td>1/20/2010</td>
      <td>0.00</td>
      <td>66</td>
    </tr>
    <tr>
      <th>18</th>
      <td>USC00519397</td>
      <td>1/21/2010</td>
      <td>0.00</td>
      <td>69</td>
    </tr>
    <tr>
      <th>19</th>
      <td>USC00519397</td>
      <td>1/22/2010</td>
      <td>0.00</td>
      <td>67</td>
    </tr>
    <tr>
      <th>20</th>
      <td>USC00519397</td>
      <td>1/23/2010</td>
      <td>0.00</td>
      <td>67</td>
    </tr>
    <tr>
      <th>21</th>
      <td>USC00519397</td>
      <td>1/24/2010</td>
      <td>0.01</td>
      <td>71</td>
    </tr>
    <tr>
      <th>22</th>
      <td>USC00519397</td>
      <td>1/25/2010</td>
      <td>0.00</td>
      <td>67</td>
    </tr>
    <tr>
      <th>23</th>
      <td>USC00519397</td>
      <td>1/26/2010</td>
      <td>0.04</td>
      <td>76</td>
    </tr>
    <tr>
      <th>24</th>
      <td>USC00519397</td>
      <td>1/27/2010</td>
      <td>0.12</td>
      <td>68</td>
    </tr>
    <tr>
      <th>25</th>
      <td>USC00519397</td>
      <td>1/28/2010</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
    <tr>
      <th>26</th>
      <td>USC00519397</td>
      <td>1/30/2010</td>
      <td>0.00</td>
      <td>70</td>
    </tr>
    <tr>
      <th>27</th>
      <td>USC00519397</td>
      <td>1/31/2010</td>
      <td>0.03</td>
      <td>67</td>
    </tr>
    <tr>
      <th>28</th>
      <td>USC00519397</td>
      <td>2/1/2010</td>
      <td>0.01</td>
      <td>66</td>
    </tr>
    <tr>
      <th>29</th>
      <td>USC00519397</td>
      <td>2/3/2010</td>
      <td>0.00</td>
      <td>67</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>19520</th>
      <td>USC00516128</td>
      <td>7/24/2017</td>
      <td>0.84</td>
      <td>77</td>
    </tr>
    <tr>
      <th>19521</th>
      <td>USC00516128</td>
      <td>7/25/2017</td>
      <td>0.30</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19522</th>
      <td>USC00516128</td>
      <td>7/26/2017</td>
      <td>0.30</td>
      <td>73</td>
    </tr>
    <tr>
      <th>19523</th>
      <td>USC00516128</td>
      <td>7/27/2017</td>
      <td>0.00</td>
      <td>75</td>
    </tr>
    <tr>
      <th>19524</th>
      <td>USC00516128</td>
      <td>7/28/2017</td>
      <td>0.40</td>
      <td>73</td>
    </tr>
    <tr>
      <th>19525</th>
      <td>USC00516128</td>
      <td>7/29/2017</td>
      <td>0.30</td>
      <td>77</td>
    </tr>
    <tr>
      <th>19526</th>
      <td>USC00516128</td>
      <td>7/30/2017</td>
      <td>0.30</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19527</th>
      <td>USC00516128</td>
      <td>7/31/2017</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>19528</th>
      <td>USC00516128</td>
      <td>8/1/2017</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
    <tr>
      <th>19529</th>
      <td>USC00516128</td>
      <td>8/2/2017</td>
      <td>0.25</td>
      <td>80</td>
    </tr>
    <tr>
      <th>19530</th>
      <td>USC00516128</td>
      <td>8/3/2017</td>
      <td>0.06</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19531</th>
      <td>USC00516128</td>
      <td>8/5/2017</td>
      <td>0.00</td>
      <td>77</td>
    </tr>
    <tr>
      <th>19532</th>
      <td>USC00516128</td>
      <td>8/6/2017</td>
      <td>0.00</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19533</th>
      <td>USC00516128</td>
      <td>8/7/2017</td>
      <td>0.05</td>
      <td>78</td>
    </tr>
    <tr>
      <th>19534</th>
      <td>USC00516128</td>
      <td>8/8/2017</td>
      <td>0.34</td>
      <td>74</td>
    </tr>
    <tr>
      <th>19535</th>
      <td>USC00516128</td>
      <td>8/9/2017</td>
      <td>0.15</td>
      <td>71</td>
    </tr>
    <tr>
      <th>19536</th>
      <td>USC00516128</td>
      <td>8/10/2017</td>
      <td>0.07</td>
      <td>75</td>
    </tr>
    <tr>
      <th>19537</th>
      <td>USC00516128</td>
      <td>8/11/2017</td>
      <td>0.00</td>
      <td>72</td>
    </tr>
    <tr>
      <th>19538</th>
      <td>USC00516128</td>
      <td>8/12/2017</td>
      <td>0.14</td>
      <td>74</td>
    </tr>
    <tr>
      <th>19539</th>
      <td>USC00516128</td>
      <td>8/13/2017</td>
      <td>0.00</td>
      <td>80</td>
    </tr>
    <tr>
      <th>19540</th>
      <td>USC00516128</td>
      <td>8/14/2017</td>
      <td>0.22</td>
      <td>79</td>
    </tr>
    <tr>
      <th>19541</th>
      <td>USC00516128</td>
      <td>8/15/2017</td>
      <td>0.42</td>
      <td>70</td>
    </tr>
    <tr>
      <th>19542</th>
      <td>USC00516128</td>
      <td>8/16/2017</td>
      <td>0.42</td>
      <td>71</td>
    </tr>
    <tr>
      <th>19543</th>
      <td>USC00516128</td>
      <td>8/17/2017</td>
      <td>0.13</td>
      <td>72</td>
    </tr>
    <tr>
      <th>19544</th>
      <td>USC00516128</td>
      <td>8/18/2017</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19545</th>
      <td>USC00516128</td>
      <td>8/19/2017</td>
      <td>0.09</td>
      <td>71</td>
    </tr>
    <tr>
      <th>19546</th>
      <td>USC00516128</td>
      <td>8/20/2017</td>
      <td>0.00</td>
      <td>78</td>
    </tr>
    <tr>
      <th>19547</th>
      <td>USC00516128</td>
      <td>8/21/2017</td>
      <td>0.56</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19548</th>
      <td>USC00516128</td>
      <td>8/22/2017</td>
      <td>0.50</td>
      <td>76</td>
    </tr>
    <tr>
      <th>19549</th>
      <td>USC00516128</td>
      <td>8/23/2017</td>
      <td>0.45</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
<p>19550 rows × 4 columns</p>
</div>




```python
measurement_data.dtypes
```




    station     object
    date        object
    prcp       float64
    tobs         int64
    dtype: object




```python
measurement_data['date'] = pd.to_datetime(measurement_data.date) 


```


```python
measurement_data.dtypes
```




    station            object
    date       datetime64[ns]
    prcp              float64
    tobs                int64
    dtype: object




```python
clean_hawaii_measurements = measurement_data.dropna()
clean_hawaii_measurements.count()


```




    station    19550
    date       19550
    prcp       19550
    tobs       19550
    dtype: int64




```python
clean_hawaii_measurements.to_csv("Resources/clean_hawaii_measurements.csv", index=False)
```

# Cleaning Hawaii Station CSV


```python
station_info = pd.read_csv('Resources/hawaii_stations.csv')
station_info.head(9)


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
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
station_info.shape
```




    (9, 5)




```python
station_info.to_csv("Resources/clean_hawaii_stations.csv", index=False)
```
