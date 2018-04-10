

```python
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float, Date
import pandas as pd
import os
from datetime import datetime


```


```python
measurements = pd.read_csv("Resources/clean_hawaii_measurements.csv")
measurements.head()

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
      <td>2010-01-01</td>
      <td>0.08</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00519397</td>
      <td>2010-01-02</td>
      <td>0.00</td>
      <td>63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00519397</td>
      <td>2010-01-03</td>
      <td>0.00</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00519397</td>
      <td>2010-01-04</td>
      <td>0.00</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00519397</td>
      <td>2010-01-06</td>
      <td>0.00</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>




```python
measurements['date'] = pd.to_datetime(measurements.date) 

```


```python
measurements.dtypes
```




    station            object
    date       datetime64[ns]
    prcp              float64
    tobs                int64
    dtype: object




```python
stations = pd.read_csv("Resources/clean_hawaii_stations.csv")
stations.head()

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
      <td>21.2716</td>
      <td>-157.8168</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.4234</td>
      <td>-157.8015</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.5213</td>
      <td>-157.8374</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.3934</td>
      <td>-157.9751</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.4992</td>
      <td>-158.0111</td>
      <td>306.6</td>
    </tr>
  </tbody>
</table>
</div>



# START ENGINES


```python
engine = create_engine("sqlite:///hawaii.sqlite")
```


```python
conn = engine.connect()
```

### CREATE MEASUREMENTS TABLE


```python
Base = declarative_base()

class Measurements(Base):
    __tablename__ = 'measurements'
    
    id = Column(Integer,primary_key=True)
    station=Column(Text)
    date=Column(String)
    prcp=Column(Float)
    tobs=Column(Float)
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}"
    


```


```python
Base.metadata.create_all(engine)
```


```python
measurements_data=measurements.to_dict(orient='records')
print(measurements_data[:5])
      
      
```

    [{'station': 'USC00519397', 'date': Timestamp('2010-01-01 00:00:00'), 'prcp': 0.08, 'tobs': 65}, {'station': 'USC00519397', 'date': Timestamp('2010-01-02 00:00:00'), 'prcp': 0.0, 'tobs': 63}, {'station': 'USC00519397', 'date': Timestamp('2010-01-03 00:00:00'), 'prcp': 0.0, 'tobs': 74}, {'station': 'USC00519397', 'date': Timestamp('2010-01-04 00:00:00'), 'prcp': 0.0, 'tobs': 76}, {'station': 'USC00519397', 'date': Timestamp('2010-01-06 00:00:00'), 'prcp': 0.0, 'tobs': 73}]
    


```python
metadata=MetaData(bind=engine)
metadata.reflect()

```


```python
measurements_table = sqlalchemy.Table('measurements', metadata, autoload=True)
```


```python
conn.execute(measurements_table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x1fad5fa9518>




```python
conn.execute(measurements_table.insert(), measurements_data)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1fad5be30b8>




```python
conn.execute("select * from measurements limit 5").fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65.0),
     (2, 'USC00519397', '2010-01-02', 0.0, 63.0),
     (3, 'USC00519397', '2010-01-03', 0.0, 74.0),
     (4, 'USC00519397', '2010-01-04', 0.0, 76.0),
     (5, 'USC00519397', '2010-01-06', 0.0, 73.0)]



### CREATE STATIONS TABLE


```python
class Stations(Base):
    __tablename__ = 'stations'
    
    id = Column(Integer,primary_key=True)
    station=Column(Text)
    name=Column(Text)
    latitutde=Column(Float)
    longitude=Column(Float)
    elevation=Column(Float)
    
```


```python
Base.metadata.create_all(engine)
```


```python
stations_data=stations.to_dict(orient='records')
print(stations_data[:5])


```

    [{'station': 'USC00519397', 'name': 'WAIKIKI 717.2, HI US', 'latitude': 21.2716, 'longitude': -157.8168, 'elevation': 3.0}, {'station': 'USC00513117', 'name': 'KANEOHE 838.1, HI US', 'latitude': 21.4234, 'longitude': -157.8015, 'elevation': 14.6}, {'station': 'USC00514830', 'name': 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7.0}, {'station': 'USC00517948', 'name': 'PEARL CITY, HI US', 'latitude': 21.3934, 'longitude': -157.9751, 'elevation': 11.9}, {'station': 'USC00518838', 'name': 'UPPER WAHIAWA 874.3, HI US', 'latitude': 21.4992, 'longitude': -158.0111, 'elevation': 306.6}]
    


```python
metadata=MetaData(bind=engine)
metadata.reflect()

```


```python
stations_table = sqlalchemy.Table('stations', metadata, autoload=True)
```


```python
conn.execute(stations_table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x1fad5fbfdd8>




```python
conn.execute(stations_table.insert(), stations_data)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1fad17c1c88>




```python
conn.execute("select * from stations limit 5").fetchall()
```




    [(1, 'USC00519397', 'WAIKIKI 717.2, HI US', None, -157.8168, 3.0),
     (2, 'USC00513117', 'KANEOHE 838.1, HI US', None, -157.8015, 14.6),
     (3, 'USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', None, -157.8374, 7.0),
     (4, 'USC00517948', 'PEARL CITY, HI US', None, -157.9751, 11.9),
     (5, 'USC00518838', 'UPPER WAHIAWA 874.3, HI US', None, -158.0111, 306.6)]


