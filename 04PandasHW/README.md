

```python
import pandas as pd
import json
import os
import numpy as np
import matplotlib.pyplot as plt

%pwd

```




    'C:\\Users\\ckent\\Desktop\\github_repo\\UT-Data-Science\\pandasHomework'




```python
csv_path = os.path.join('..','pandasHomework','students_complete.csv')
csv_path02 = os.path.join('..','pandasHomework','schools_complete.csv')
students_df = pd.read_csv(csv_path)
schools_df = pd.read_csv(csv_path02)


```


```python
students_df.head()

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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#clean up column headers
schools02_df = schools_df.rename(columns={"School ID":"SCHOOL ID", "name":"SCHOOL","type":"SCHOOL TYPE","size":"ALL STUDENTS",
                                             "budget":"BUDGET"})
students02_df = students_df.rename(columns={"Student ID":"STUDENT ID","name":"NAME","gender":"GENDER",
                                               "grade":"GRADE","school":"SCHOOL","reading_score":"READING SCORE",
                                               "math_score":"MATH SCORE"})
schools02_df.head()


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
      <th>SCHOOL ID</th>
      <th>SCHOOL</th>
      <th>SCHOOL TYPE</th>
      <th>ALL STUDENTS</th>
      <th>BUDGET</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CREATE DISTRICT SUMMARY TABLE
```


```python
#find total number of schools
total_schools = len(students02_df["SCHOOL"].unique())

#find total number of students
total_students = students02_df["STUDENT ID"].count()

#calculate total budget
total_budget = schools02_df['BUDGET'].sum()

#calculate average math score
avg_math = students02_df["MATH SCORE"].mean()

#calculate average reading score
avg_read = students02_df["READING SCORE"].mean()

#% students passing math
pass_math = ((students02_df[(students02_df['MATH SCORE']>=70)].count()['MATH SCORE'])/total_students)*100

#% students passing reading
pass_read = ((students02_df[(students02_df['READING SCORE']>=70)].count()["READING SCORE"])/total_students)*100

#% overall passing 

total_pass = (avg_math + avg_read)/2

#create summary table
summary_table = pd.DataFrame({"TOTAL SCHOOLS":[total_schools],"TOTAL STUDENTS":[total_students],"TOTAL BUDGET":[total_budget],
                             "AVERAGE MATH SCORE":[avg_math],"AVERAGE READING SCORE":[avg_read],"% PASSING MATH":[pass_math],
                             "% PASSING READING":[pass_read],"% OVERALL PASSING RATE":[total_pass]})

final_summary_table_df = summary_table[["TOTAL SCHOOLS","TOTAL STUDENTS","TOTAL BUDGET","AVERAGE MATH SCORE",
                                     "AVERAGE READING SCORE","% PASSING MATH","% PASSING READING",
                                     "% OVERALL PASSING RATE"]]

#format output
final_summary_table_df["TOTAL STUDENTS"]=final_summary_table_df["TOTAL STUDENTS"].map("{:,}".format)
final_summary_table_df["TOTAL BUDGET"]=final_summary_table_df["TOTAL BUDGET"].map("${:,.2f}".format)
final_summary_table_df["AVERAGE MATH SCORE"]=final_summary_table_df["AVERAGE MATH SCORE"].map("{:,.2f}".format)
final_summary_table_df["AVERAGE READING SCORE"]=final_summary_table_df["AVERAGE READING SCORE"].map("{:,.2f}".format)
final_summary_table_df["% PASSING MATH"]=final_summary_table_df["% PASSING MATH"].apply('{:.2f}%'.format)
final_summary_table_df["% PASSING READING"]=final_summary_table_df["% PASSING READING"].apply('{:.2f}%'.format)
final_summary_table_df["% OVERALL PASSING RATE"]=final_summary_table_df["% OVERALL PASSING RATE"].apply('{:.2f}%'.format)
final_summary_table_df

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
      <th>TOTAL SCHOOLS</th>
      <th>TOTAL STUDENTS</th>
      <th>TOTAL BUDGET</th>
      <th>AVERAGE MATH SCORE</th>
      <th>AVERAGE READING SCORE</th>
      <th>% PASSING MATH</th>
      <th>% PASSING READING</th>
      <th>% OVERALL PASSING RATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>80.43%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#CREATE SCHOOL SUMMARY TABLE
```


```python
#merge tables  school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

school_merge_df = pd.merge(schools02_df,students02_df,how='outer',on='SCHOOL')

#inspect merged table

school_merge_df.head()
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
      <th>SCHOOL ID</th>
      <th>SCHOOL</th>
      <th>SCHOOL TYPE</th>
      <th>ALL STUDENTS</th>
      <th>BUDGET</th>
      <th>STUDENT ID</th>
      <th>NAME</th>
      <th>GENDER</th>
      <th>GRADE</th>
      <th>READING SCORE</th>
      <th>MATH SCORE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#groupby school name
school_pop = school_merge_df['SCHOOL'].value_counts()

#budget per school
school_budget = school_merge_df.groupby(['SCHOOL']).mean()['BUDGET']

#budget per student for df
budget_per_student = school_budget / school_pop

#avg scores per school calculations
math_school = school_merge_df.groupby(['SCHOOL']).mean()['MATH SCORE']
read_school = school_merge_df.groupby(['SCHOOL']).mean()['READING SCORE']
math_per_school = school_merge_df[school_merge_df['MATH SCORE']>=70].groupby(['SCHOOL']).count()["MATH SCORE"]
reading_per_school = school_merge_df[school_merge_df['READING SCORE']>=70].groupby(['SCHOOL']).count()["READING SCORE"]

#avg scores per school for df
percent_pass_math = (math_per_school/school_pop)*100
percent_pass_reading = (reading_per_school/school_pop)*100
percent_overall_passing = ((percent_pass_math + percent_pass_reading)/2)

#create columns
columns = ['TOTAL STUDENTS','TOTAL SCHOOL BUDGET', 'PER STUDENT BUDGET', 'AVERAGE MATH SCORE',
           'AVERAGE READING SCORE', '% PASSING MATH', '% PASSING READING', '% OVERALL PASSING']

#Create dictionary
school_dict = {"SCHOOL":reading_per_school.index,'TOTAL STUDENTS': school_pop.values, 
               'TOTAL SCHOOL BUDGET': school_budget.values, "PER STUDENT BUDGET": budget_per_student.values,
               'AVERAGE MATH SCORE': math_school.values, 'AVERAGE READING SCORE': read_school.values, 
               '% PASSING MATH': percent_pass_math.values,'% PASSING READING': percent_pass_reading.values, 
               '% OVERALL PASSING': percent_overall_passing.values}

#set index
per_school_summary_df = pd.DataFrame(school_dict).set_index("SCHOOL")

#rearrange columns
per_school_summary_df = per_school_summary_df[['TOTAL STUDENTS','TOTAL SCHOOL BUDGET', 'PER STUDENT BUDGET', 'AVERAGE MATH SCORE',
                                               'AVERAGE READING SCORE', '% PASSING MATH', '% PASSING READING', '% OVERALL PASSING']]

#formatting
per_school_summary_df['PER STUDENT BUDGET']=per_school_summary_df['PER STUDENT BUDGET'].map('${:,.2f}'.format)             
per_school_summary_df['TOTAL SCHOOL BUDGET']=per_school_summary_df['TOTAL SCHOOL BUDGET'].map('${:,.2f}'.format)
per_school_summary_df['AVERAGE MATH SCORE']=per_school_summary_df['AVERAGE MATH SCORE'].apply('{:.2f}%'.format)
per_school_summary_df['AVERAGE READING SCORE']=per_school_summary_df['AVERAGE READING SCORE'].apply('{:.2f}%'.format)
per_school_summary_df['% PASSING MATH']=per_school_summary_df['% PASSING MATH'].apply('{:.2f}%'.format)
per_school_summary_df['% PASSING READING']=per_school_summary_df['% PASSING READING'].apply('{:.2f}%'.format)
per_school_summary_df['% OVERALL PASSING']=per_school_summary_df['% OVERALL PASSING'].apply('{:.2f}%'.format)

#call df
per_school_summary_df.head()
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
      <th>TOTAL STUDENTS</th>
      <th>TOTAL SCHOOL BUDGET</th>
      <th>PER STUDENT BUDGET</th>
      <th>AVERAGE MATH SCORE</th>
      <th>AVERAGE READING SCORE</th>
      <th>% PASSING MATH</th>
      <th>% PASSING READING</th>
      <th>% OVERALL PASSING</th>
    </tr>
    <tr>
      <th>SCHOOL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.05%</td>
      <td>81.03%</td>
      <td>66.68%</td>
      <td>81.93%</td>
      <td>74.31%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>4761</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06%</td>
      <td>83.98%</td>
      <td>94.13%</td>
      <td>97.04%</td>
      <td>95.59%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>4635</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71%</td>
      <td>81.16%</td>
      <td>65.99%</td>
      <td>80.74%</td>
      <td>73.36%</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>3999</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.10%</td>
      <td>80.75%</td>
      <td>68.31%</td>
      <td>79.30%</td>
      <td>73.80%</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>2949</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35%</td>
      <td>83.82%</td>
      <td>93.39%</td>
      <td>97.14%</td>
      <td>95.27%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#TOP PERFORMING SCHOOLS (BY PASSING RATE)
```


```python
best_rank_df = per_school_summary_df.sort_values(by=['% OVERALL PASSING'],ascending=False)
best_rank_df.head()
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
      <th>TOTAL STUDENTS</th>
      <th>TOTAL SCHOOL BUDGET</th>
      <th>PER STUDENT BUDGET</th>
      <th>AVERAGE MATH SCORE</th>
      <th>AVERAGE READING SCORE</th>
      <th>% PASSING MATH</th>
      <th>% PASSING READING</th>
      <th>% OVERALL PASSING</th>
      <th>SPENDING RANGE (PER STUDENT)</th>
    </tr>
    <tr>
      <th>SCHOOL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>4761</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.06%</td>
      <td>83.98%</td>
      <td>94.13%</td>
      <td>97.04%</td>
      <td>95.59%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1468</td>
      <td>$1,043,130.00</td>
      <td>$638.00</td>
      <td>83.42%</td>
      <td>83.85%</td>
      <td>93.27%</td>
      <td>97.31%</td>
      <td>95.29%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>2949</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.35%</td>
      <td>83.82%</td>
      <td>93.39%</td>
      <td>97.14%</td>
      <td>95.27%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>1800</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.84%</td>
      <td>84.04%</td>
      <td>94.59%</td>
      <td>95.95%</td>
      <td>95.27%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>962</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.27%</td>
      <td>83.99%</td>
      <td>93.87%</td>
      <td>96.54%</td>
      <td>95.20%</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#BOTTOM PERFORMING SCHOOLS (BY PASSING RATE)
```


```python
worst_rank_df = per_school_summary_df.sort_values(by=['% OVERALL PASSING'])
worst_rank_df.head()
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
      <th>TOTAL STUDENTS</th>
      <th>TOTAL SCHOOL BUDGET</th>
      <th>PER STUDENT BUDGET</th>
      <th>AVERAGE MATH SCORE</th>
      <th>AVERAGE READING SCORE</th>
      <th>% PASSING MATH</th>
      <th>% PASSING READING</th>
      <th>% OVERALL PASSING</th>
      <th>SPENDING RANGE (PER STUDENT)</th>
    </tr>
    <tr>
      <th>SCHOOL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>1761</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.84%</td>
      <td>80.74%</td>
      <td>66.37%</td>
      <td>80.22%</td>
      <td>73.29%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>4635</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.71%</td>
      <td>81.16%</td>
      <td>65.99%</td>
      <td>80.74%</td>
      <td>73.36%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>2283</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.63%</td>
      <td>81.18%</td>
      <td>65.68%</td>
      <td>81.32%</td>
      <td>73.50%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>1858</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.07%</td>
      <td>80.97%</td>
      <td>66.06%</td>
      <td>81.22%</td>
      <td>73.64%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>3999</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.10%</td>
      <td>80.75%</td>
      <td>68.31%</td>
      <td>79.30%</td>
      <td>73.80%</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#AVERAGE MATH SCORE BY GRADE LEVEL--------------------------------------------------------------------------------------------
```


```python
#convert grade levels from cell value to column headers

students02_df['GRADE'] = (students02_df['GRADE'].replace({'GRADE' : {'9th': 9,'10th': 10,'11th': 11,'12th': 12}},
                                                        regex=True))

#group by to change index to school and grade, with formatted average math score reflected as a percentage

grade_level_df = (students02_df.reset_index().groupby(["SCHOOL","GRADE"], 
                                                      as_index=True)['MATH SCORE'].mean().apply('{:.2f}%'.format)).unstack()

#reorder columns
math_scores_by_grade = grade_level_df[['9th','10th','11th','12th']]
math_scores_by_grade.index.name = None
                                       
#call new df

math_scores_by_grade


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
      <th>GRADE</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.08%</td>
      <td>77.00%</td>
      <td>77.52%</td>
      <td>76.49%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.09%</td>
      <td>83.15%</td>
      <td>82.77%</td>
      <td>83.28%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.40%</td>
      <td>76.54%</td>
      <td>76.88%</td>
      <td>77.15%</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.36%</td>
      <td>77.67%</td>
      <td>76.92%</td>
      <td>76.18%</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.04%</td>
      <td>84.23%</td>
      <td>83.84%</td>
      <td>83.36%</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.44%</td>
      <td>77.34%</td>
      <td>77.14%</td>
      <td>77.19%</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.79%</td>
      <td>83.43%</td>
      <td>85.00%</td>
      <td>82.86%</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.03%</td>
      <td>75.91%</td>
      <td>76.45%</td>
      <td>77.23%</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.19%</td>
      <td>76.69%</td>
      <td>77.49%</td>
      <td>76.86%</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.63%</td>
      <td>83.37%</td>
      <td>84.33%</td>
      <td>84.12%</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.86%</td>
      <td>76.61%</td>
      <td>76.40%</td>
      <td>77.69%</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.42%</td>
      <td>82.92%</td>
      <td>83.38%</td>
      <td>83.78%</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.59%</td>
      <td>83.09%</td>
      <td>83.50%</td>
      <td>83.50%</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.09%</td>
      <td>83.72%</td>
      <td>83.20%</td>
      <td>83.04%</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.26%</td>
      <td>84.01%</td>
      <td>83.84%</td>
      <td>83.64%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#AVERAGE READING SCORE BY GRADE LEVEL-----------------------------------------------------------------------------------------
```


```python
#group by to change index to school and grade, with formatted average reading score reflected as a percentage

grade_level_read_df = (students02_df.reset_index().groupby(["SCHOOL","GRADE"], 
                                                      as_index=True)['READING SCORE'].mean().apply('{:.2f}%'.format)).unstack()

#reorder columns
read_scores_by_grade = grade_level_df[['9th','10th','11th','12th']]
read_scores_by_grade.index.name = None
                                       
#call new df

read_scores_by_grade
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
      <th>GRADE</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.08%</td>
      <td>77.00%</td>
      <td>77.52%</td>
      <td>76.49%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.09%</td>
      <td>83.15%</td>
      <td>82.77%</td>
      <td>83.28%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.40%</td>
      <td>76.54%</td>
      <td>76.88%</td>
      <td>77.15%</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.36%</td>
      <td>77.67%</td>
      <td>76.92%</td>
      <td>76.18%</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.04%</td>
      <td>84.23%</td>
      <td>83.84%</td>
      <td>83.36%</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.44%</td>
      <td>77.34%</td>
      <td>77.14%</td>
      <td>77.19%</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.79%</td>
      <td>83.43%</td>
      <td>85.00%</td>
      <td>82.86%</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.03%</td>
      <td>75.91%</td>
      <td>76.45%</td>
      <td>77.23%</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.19%</td>
      <td>76.69%</td>
      <td>77.49%</td>
      <td>76.86%</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.63%</td>
      <td>83.37%</td>
      <td>84.33%</td>
      <td>84.12%</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.86%</td>
      <td>76.61%</td>
      <td>76.40%</td>
      <td>77.69%</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.42%</td>
      <td>82.92%</td>
      <td>83.38%</td>
      <td>83.78%</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.59%</td>
      <td>83.09%</td>
      <td>83.50%</td>
      <td>83.50%</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.09%</td>
      <td>83.72%</td>
      <td>83.20%</td>
      <td>83.04%</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.26%</td>
      <td>84.01%</td>
      <td>83.84%</td>
      <td>83.64%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#SCORES BY SCHOOL SPENDING
```


```python
#find max & min spending for bins
print(per_school_summary_df["PER STUDENT BUDGET"].max())

print(per_school_summary_df["PER STUDENT BUDGET"].min())

```

    $655.00
    $578.00
    


```python
#create bins   Signature: pd.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False)

bins = [0,585, 615, 645, 675]

group_labels = ["$0-585", "$585-615", "$615-645", "$645-675"]

#slice data series and place into bins


per_school_summary_df["SPENDING RANGE (PER STUDENT)"] = pd.cut(school_budget, bins, labels = group_labels)

#pd.cut(per_school_summary_df["AVERAGE MATH SCORE"],bins,labels=group_labels)

```


```python
#GROUP BY SPENDING
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2441             try:
    -> 2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'AVERAGE MATH SCORE'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-178-b5143c078cad> in <module>()
          1 
    ----> 2 percent_pass_math = per_school_summary_df.groupby(['SPENDING RANGE (PER STUDENT)']).mean()[('AVERAGE MATH SCORE')]
          3 #print(percent_pass_math)
          4 percent_pass_reading = per_school_summary_df.groupby(['SPENDING RANGE (PER STUDENT)']).mean()['AVERAGE READING SCORE']
          5 math_spending_percent = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% PASSING MATH"]
    

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
       1962             return self._getitem_multilevel(key)
       1963         else:
    -> 1964             return self._getitem_column(key)
       1965 
       1966     def _getitem_column(self, key):
    

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\frame.py in _getitem_column(self, key)
       1969         # get column
       1970         if self.columns.is_unique:
    -> 1971             return self._get_item_cache(key)
       1972 
       1973         # duplicate columns & possible reduce dimensionality
    

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\generic.py in _get_item_cache(self, item)
       1643         res = cache.get(item)
       1644         if res is None:
    -> 1645             values = self._data.get(item)
       1646             res = self._box_item_values(item, values)
       1647             cache[item] = res
    

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\internals.py in get(self, item, fastpath)
       3588 
       3589             if not isnull(item):
    -> 3590                 loc = self.items.get_loc(item)
       3591             else:
       3592                 indexer = np.arange(len(self.items))[isnull(self.items)]
    

    ~\Anaconda3\envs\PythonData\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    -> 2444                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2445 
       2446         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'AVERAGE MATH SCORE'



```python
school_merge_df.head(1)
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
      <th>SCHOOL ID</th>
      <th>SCHOOL</th>
      <th>SCHOOL TYPE</th>
      <th>ALL STUDENTS</th>
      <th>BUDGET</th>
      <th>STUDENT ID</th>
      <th>NAME</th>
      <th>GENDER</th>
      <th>GRADE</th>
      <th>READING SCORE</th>
      <th>MATH SCORE</th>
      <th>PER STUDENT BUDGET</th>
      <th>SPENDING RANGE (PER STUDENT)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>66</td>
      <td>79</td>
      <td>&lt;$585</td>
      <td>&lt;$585</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = [0,585, 615, 645, 675]
group_name = ["$0-585", "$585-615", "$615-645", "$645-675"]
school_merge_df['spending_bins'] = pd.cut(school_merge_df['BUDGET']/school_merge_df['ALL STUDENTS'], bins, labels = group_name)

#group by spending
by_spending = school_merge_df.groupby('spending_bins')

#calculations
avg_math = by_spending['MATH SCORE'].mean()
avg_read = by_spending['READING SCORE'].mean()
pass_math = school_merge_df[school_merge_df['MATH SCORE'] >= 70].groupby('spending_bins')['STUDENT ID'].count()/by_spending['STUDENT ID'].count()
pass_read = school_merge_df[school_merge_df['READING SCORE'] >= 70].groupby('spending_bins')['STUDENT ID'].count()/by_spending['STUDENT ID'].count()
overall = school_merge_df[(school_merge_df['READING SCORE'] >= 70) & (school_merge_df['MATH SCORE'] >= 70)].groupby('spending_bins')['STUDENT ID'].count()/by_spending['STUDENT ID'].count()

            
# df build            
scores_by_spend = pd.DataFrame({"Average Math Score": avg_math,"Average Reading Score": avg_read,'% Passing Math': pass_math,
                                '% Passing Reading': pass_read,"Overall Passing Rate": overall})
            
#reorder columns
scores_by_spend = scores_by_spend[["Average Math Score","Average Reading Score",'% Passing Math',
                                   '% Passing Reading',"Overall Passing Rate"]]

scores_by_spend.index.name = "Per Student Budget"
scores_by_spend = scores_by_spend.reindex(group_name)

#formating
scores_by_spend.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})
```




<style  type="text/css" >
</style>  
<table id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Per Student Budget</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058level0_row0" class="row_heading level0 row0" >$0-585</th> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row0_col0" class="data row0 col0" >83.4</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row0_col1" class="data row0 col1" >84.0</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row0_col2" class="data row0 col2" >93.7%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row0_col3" class="data row0 col3" >96.7%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row0_col4" class="data row0 col4" >90.6%</td> 
    </tr>    <tr> 
        <th id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058level0_row1" class="row_heading level0 row1" >$585-615</th> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row1_col0" class="data row1 col0" >83.5</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row1_col1" class="data row1 col1" >83.8</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row1_col2" class="data row1 col2" >94.1%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row1_col3" class="data row1 col3" >95.9%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row1_col4" class="data row1 col4" >90.1%</td> 
    </tr>    <tr> 
        <th id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058level0_row2" class="row_heading level0 row2" >$615-645</th> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row2_col0" class="data row2 col0" >78.1</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row2_col1" class="data row2 col1" >81.4</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row2_col2" class="data row2 col2" >71.4%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row2_col3" class="data row2 col3" >83.6%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row2_col4" class="data row2 col4" >60.3%</td> 
    </tr>    <tr> 
        <th id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058level0_row3" class="row_heading level0 row3" >$645-675</th> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row3_col0" class="data row3 col0" >77.0</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row3_col1" class="data row3 col1" >81.0</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row3_col2" class="data row3 col2" >66.2%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row3_col3" class="data row3 col3" >81.1%</td> 
        <td id="T_e5ad7b68_112a_11e8_863c_9cb6d0eae058row3_col4" class="data row3 col4" >53.5%</td> 
    </tr></tbody> 
</table> 




```python
#GROUP BY SCHOOL SIZE
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
      <th>GRADE</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>SCHOOL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.91%</td>
      <td>80.95%</td>
      <td>80.91%</td>
      <td>81.30%</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.25%</td>
      <td>83.79%</td>
      <td>84.29%</td>
      <td>83.68%</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.41%</td>
      <td>80.64%</td>
      <td>81.38%</td>
      <td>81.20%</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.26%</td>
      <td>80.40%</td>
      <td>80.66%</td>
      <td>80.63%</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.71%</td>
      <td>84.29%</td>
      <td>84.01%</td>
      <td>83.37%</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.66%</td>
      <td>81.40%</td>
      <td>80.86%</td>
      <td>80.87%</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.32%</td>
      <td>83.82%</td>
      <td>84.70%</td>
      <td>83.68%</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.51%</td>
      <td>81.42%</td>
      <td>80.31%</td>
      <td>81.29%</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.77%</td>
      <td>80.62%</td>
      <td>81.23%</td>
      <td>81.26%</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.61%</td>
      <td>84.34%</td>
      <td>84.59%</td>
      <td>83.81%</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.63%</td>
      <td>80.86%</td>
      <td>80.38%</td>
      <td>80.99%</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.44%</td>
      <td>84.37%</td>
      <td>82.78%</td>
      <td>84.12%</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.25%</td>
      <td>83.59%</td>
      <td>83.83%</td>
      <td>83.73%</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.02%</td>
      <td>83.76%</td>
      <td>84.32%</td>
      <td>83.94%</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.81%</td>
      <td>84.16%</td>
      <td>84.07%</td>
      <td>83.83%</td>
    </tr>
  </tbody>
</table>
</div>




```python
# create size bins
bins = [0, 1000, 2000, 5000]
group_name = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
school_merge_df['size_bins'] = pd.cut(school_merge_df['ALL STUDENTS'], bins, labels = group_name)

#group by spending
by_size = school_merge_df.groupby('size_bins')

#calculations 
avg_math = by_size['MATH SCORE'].mean()
avg_read = by_size['MATH SCORE'].mean()
pass_math = school_merge_df[school_merge_df['MATH SCORE'] >= 70].groupby('size_bins')['STUDENT ID'].count()/by_size['STUDENT ID'].count()
pass_read = school_merge_df[school_merge_df['READING SCORE'] >= 70].groupby('size_bins')['STUDENT ID'].count()/by_size['STUDENT ID'].count()
overall = school_merge_df[(school_merge_df['READING SCORE'] >= 70) & (school_merge_df['MATH SCORE'] >= 70)].groupby('size_bins')['STUDENT ID'].count()/by_size['STUDENT ID'].count()

            
# df build            
scores_by_size = pd.DataFrame({
    "Average Math Score": avg_math,
    "Average Reading Score": avg_read,
    '% Passing Math': pass_math,
    '% Passing Reading': pass_read,
    "Overall Passing Rate": overall
            
})
            
#reorder columns
scores_by_size = scores_by_size[[
    "Average Math Score",
    "Average Reading Score",
    '% Passing Math',
    '% Passing Reading',
    "Overall Passing Rate"
]]

scores_by_size.index.name = "Total Students"
scores_by_size = scores_by_size.reindex(group_name)

#formating
scores_by_size.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})
```




<style  type="text/css" >
</style>  
<table id="T_970135dc_112b_11e8_80de_9cb6d0eae058" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Total Students</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_970135dc_112b_11e8_80de_9cb6d0eae058level0_row0" class="row_heading level0 row0" >Small (<1000)</th> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row0_col0" class="data row0 col0" >83.8</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row0_col1" class="data row0 col1" >83.8</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row0_col2" class="data row0 col2" >94.0%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row0_col3" class="data row0 col3" >96.0%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row0_col4" class="data row0 col4" >90.1%</td> 
    </tr>    <tr> 
        <th id="T_970135dc_112b_11e8_80de_9cb6d0eae058level0_row1" class="row_heading level0 row1" >Medium (1000-2000)</th> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row1_col0" class="data row1 col0" >83.4</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row1_col1" class="data row1 col1" >83.4</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row1_col2" class="data row1 col2" >93.6%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row1_col3" class="data row1 col3" >96.8%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row1_col4" class="data row1 col4" >90.6%</td> 
    </tr>    <tr> 
        <th id="T_970135dc_112b_11e8_80de_9cb6d0eae058level0_row2" class="row_heading level0 row2" >Large (2000-5000)</th> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row2_col0" class="data row2 col0" >77.5</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row2_col1" class="data row2 col1" >77.5</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row2_col2" class="data row2 col2" >68.7%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row2_col3" class="data row2 col3" >82.1%</td> 
        <td id="T_970135dc_112b_11e8_80de_9cb6d0eae058row2_col4" class="data row2 col4" >56.6%</td> 
    </tr></tbody> 
</table> 




```python
#GROUP BY SCHOOL TYPE
```


```python
# group by type of school
by_type = school_merge_df.groupby("SCHOOL TYPE")

#calculations 
avg_math = by_type['MATH SCORE'].mean()
avg_read = by_type['MATH SCORE'].mean()
pass_math = school_merge_df[school_merge_df['MATH SCORE'] >= 70].groupby('SCHOOL TYPE')['STUDENT ID'].count()/by_type['STUDENT ID'].count()
pass_read = school_merge_df[school_merge_df['READING SCORE'] >= 70].groupby('SCHOOL TYPE')['STUDENT ID'].count()/by_type['STUDENT ID'].count()
overall = school_merge_df[(school_merge_df['READING SCORE'] >= 70) & (school_merge_df['MATH SCORE'] >= 70)].groupby('SCHOOL TYPE')['STUDENT ID'].count()/by_type['STUDENT ID'].count()

# df build            
scores_by_type = pd.DataFrame({"Average Math Score": avg_math,"Average Reading Score": avg_read,'% Passing Math': pass_math,
                               '% Passing Reading': pass_read,"Overall Passing Rate": overall})
    
#reorder columns
scores_by_type = scores_by_type[["Average Math Score","Average Reading Score",'% Passing Math','% Passing Reading',
                                 "Overall Passing Rate"]]

scores_by_type.index.name = "Type of School"


#formating
scores_by_type.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})
```




<style  type="text/css" >
</style>  
<table id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Math Score</th> 
        <th class="col_heading level0 col1" >Average Reading Score</th> 
        <th class="col_heading level0 col2" >% Passing Math</th> 
        <th class="col_heading level0 col3" >% Passing Reading</th> 
        <th class="col_heading level0 col4" >Overall Passing Rate</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Type of School</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058level0_row0" class="row_heading level0 row0" >Charter</th> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row0_col0" class="data row0 col0" >83.4</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row0_col1" class="data row0 col1" >83.4</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row0_col2" class="data row0 col2" >93.7%</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row0_col3" class="data row0 col3" >96.6%</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row0_col4" class="data row0 col4" >90.6%</td> 
    </tr>    <tr> 
        <th id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058level0_row1" class="row_heading level0 row1" >District</th> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row1_col0" class="data row1 col0" >77.0</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row1_col1" class="data row1 col1" >77.0</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row1_col2" class="data row1 col2" >66.5%</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row1_col3" class="data row1 col3" >80.9%</td> 
        <td id="T_73f614c8_112c_11e8_bceb_9cb6d0eae058row1_col4" class="data row1 col4" >53.7%</td> 
    </tr></tbody> 
</table> 


