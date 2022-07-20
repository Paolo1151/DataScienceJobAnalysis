## Introduction

Being a Data Scientist is heavily coveted in this society where being data-driven has had a huge impact in the way various industries make decisions. According to Davenport and Patil, Data Science is "The Sexiest Job of the 21st Century" for the job being highly in demand due to the qualities that a Data Scientist can provide for a company. 

Despite Data Scientists being a valuable asset to many companies, the field of Data Science is not an exception from the phenomenon known as "Brain Drain". According to its definition in Merriam Webster:

> ### Brain Drain
> "The departure of educated or professional people from one country, economic sector, or field for another usually for better pay or living conditions"
>
> Source: https://www.merriam-webster.com/dictionary/brain%20drain


This phenomena is a major concern for the local job market as this limits local company's opportunities to hire Data Scientists and find the best talent for their company. 

Sources:

https://jakevdp.github.io/blog/2013/10/26/big-data-brain-drain/

https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century

----

## Research Questions and Objectives

With this, this project aims to answer the following questions:

* How does the Salary amongst Data Science Jobs change throughout the years?
* Where do Data Scientists go to work coming from a country of origin?


The purpose of this study is to be able to:

* Understand the trends in the Data Science Salaries in terms of different parameters
* Understand Data Scientist Migration Patterns
----

## Scope and Limitations

The Data used in this study is limited to the dataset provided from Kaggle. (https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries). 


----

## Methodology

{METHOD PICTURE}

This study will follow a simple procedure to answer the questions. As with any dataset, the dataset is preprocessed and new features based on domain knowledge are added before any analysis is done. Once the dataset is cleaned, basic graphs are created and examined in order to understand the dataset and the trends in the Data Science Market. Lastly, to understand Data Scientist Migration Patterns, a Markov Chain is graphed and analyzed to determine the probability of a Data Scientist migrating from one country to another. 

## Characteristics of the Dataset

The Dataset is retrieved from Kaggle as a CSV with the following columns:

Column      | Description
-------     | -----------------
work_year   | The year the salary was paid
experience_level | The experience level in the job during the year with the following possible values: EN Entry-level / Junior MI Mid-level / Intermediate SE Senior-level / Expert EX Executive-level / Director
employment_type | The type of employement for the role: PT Part-time FT Full-time CT Contract FL Freelance
job_title | The role worked in during the year
salary | The total gross salary amount paid
salary_currency | The currency of the salary paid as an ISO 4217 currency code
salary_in_usd | The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com)
employee_residence | Employee's primary country of residence in during the work year as an ISO 3166 country code
remote_ratio | The overall amount of work done remotely, possible values are as follows: 0 No remote work (less than 20%) 50 Partially remote 100 Fully remote (more than 80%)
company_location | The country of the employer's main office or contracting branch as an ISO 3166 country code
company_size | The average number of people that worked for the company during the year: S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250 employees (large)

According to the poster, the dataset was retrieved from ai-jobs.net as an aggregate.


After this, new columns were created:

New Column      | Description
-------     | -----------------
arrangement_type | The work arrangement for the job: Hybrid, Remote, or On-site
field | The field of the job: Data Science, Data Analysis, Data Engineering, Machine Learning and Artificial Intelligence, Academe, Head of Data, and Other
brain_drain | Whether the company location is not equals to the employee's residence



The Salary used will only be using the salary_in_usd column in order for the salary to be in the same value.