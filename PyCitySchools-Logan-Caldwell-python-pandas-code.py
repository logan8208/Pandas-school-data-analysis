#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Logan Caldwell pandas hw
# importing dependencies

import pandas as pd
import numpy as np


# In[3]:


# Read in csv file and assign dataframes

school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"

school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


# In[4]:


school_data.head()


# In[5]:


student_data.head()


# In[96]:


#Merge data to one df

school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

school_data_complete.head(10)


# In[182]:


# District summaries

print("District Summary: ")
print()

tot_num_schools = int(len(school_data_complete["School ID"].unique()))
print(f"The total number of schools is: {tot_num_schools}")

tot_num_students = len(school_data_complete["student_name"])
print(f"The total number of students is: {tot_num_students}")

tot_budget = sum(school_data_complete["budget"].unique())
print(f"The total budget is: {tot_budget}")

avg_math_score = round(sum(school_data_complete["math_score"])/tot_num_students, 2)
print(f"The average math score is: {avg_math_score}")

avg_reading_score = round(sum(school_data_complete["reading_score"])/tot_num_students, 2)
print(f"The average reading score is: {avg_reading_score}")

avg_passing_ie_tot_score = round((avg_math_score + avg_reading_score)/2, 2)
print(f"The average passing (i.e., overall average) score is: {avg_passing_ie_tot_score}")

df_passing_math_students = school_data_complete[school_data_complete["math_score"] >= 70]
num_passing_math_students = int(len(df_passing_math_students))
pct_passing_math_students = round(((num_passing_math_students/tot_num_students)*100), 2)
print(f"Percentage of passing math students is: {pct_passing_math_students}%")

df_passing_reading_students = school_data_complete[school_data_complete["reading_score"] >= 70]
num_passing_reading_students = int(len(df_passing_reading_students))
pct_passing_reading_students = round(((num_passing_reading_students/tot_num_students)*100), 2)
print(f"Percentage of passing reading students is: {pct_passing_reading_students}%")


dict_district_summary = {"Num_schools":tot_num_schools, "Num_students":tot_num_students, "Tot_budget":tot_budget, 
                         "Avg_math":avg_math_score, "Avg_reading":avg_reading_score, 
                         "avg_passing":avg_passing_ie_tot_score, "pct_math_pass":pct_passing_math_students, 
                         "pct_reading_pass":pct_passing_reading_students}
df_district_summary = pd.DataFrame(data=dict_district_summary, index = ['Info'], columns = ["Num_schools","Num_students","Tot_budget",
                                                                          "Avg_math","Avg_reading","avg_passing",
                                                                          "pct_math_pass","pct_reading_pass"])
df_district_summary


# In[344]:


school_data_complete["percent_math_pass"] = pct_passing_math_students


# In[347]:


school_data_complete["percent_reading_pass"] = pct_passing_reading_students


# In[348]:


school_data_complete["overall_pass"] = 80.44


# In[349]:


# School summaries

school_data_complete_grouped_by_school = school_data_complete.groupby("school_name")
school_data_complete_grouped_by_school.head()


# In[ ]:





# In[350]:


# School summaries cont.

tot_student = school_data_complete_grouped_by_school["school_name"].value_counts()
tot_student.head()


# In[ ]:





# In[351]:


school_type = school_data_complete_grouped_by_school["type"]
school_type.head()


# In[352]:


tot_student = school_data_complete_grouped_by_school["student_name"].count()
# tot_student.head()


# In[353]:


total_school_budg = float(school_data_complete_grouped_by_school["budget"].mean())
# total_school_budg.head()


# In[354]:


per_student_budg = (total_school_budg/(school_data_complete_grouped_by_school["Student ID"].nunique()))


# In[355]:


avg_math_score = school_data_complete_grouped_by_school["math_score"].mean()


# In[356]:


avg_reading_score = school_data_complete_grouped_by_school["reading_score"].mean()


# In[357]:


# percent_pass_math = ((school_data_complete_grouped_by_school[(school_data_complete_grouped_by_school["math_score"] >= 70), :])/(school_data_complete_grouped_by_school["Student ID"].nunique()))

# df_passing_math_students = school_data_complete[school_data_complete["math_score"] >= 70]
# num_passing_math_students = int(len(df_passing_math_students))
# pct_passing_math_students = round(((num_passing_math_students/tot_num_students)*100), 2)
# print(f"Percentage of passing math students is: {pct_passing_math_students}%")


# In[358]:


school_summary_table = pd.DataFrame({
                                    "school_type": school_type,
                                    "total_students": tot_student,
                                    "total_school_budg": total_school_budg,
                                    "per_student_budg": per_student_budg,
                                    "avg_math_score": avg_math_score,
                                    "avg_reading_score": avg_reading_score,
                                    "%_pass_math": "percent_pass_math",
                                    "%_pass_reading": "percent_pass_reading",
                                    "overall_pass_rate": "overall_pass_rate" 
                                    })
school_summary_table.head(10)


# In[ ]:





# In[ ]:





# In[ ]:




