## How does the Salary amongst Data Science Jobs vary according to different Parameters?

{Interactive Data Explorer 1}

The heatmaps above visualize the mean of the Data Science Salaries over the years per field. Along with it, it was also filtered over per experience level to see how much the mean of the Data Science Salaries changed over the years per experience level.

For Entry level Data Scientists at 2020, the role with the highest mean salary seems to Machine Learning and Artificial Intelligence Roles. As 2021 roll by, entry level positions with the highest mean salary starts to shift to Data Scientists working in Research. This is also shown in the year 2022.

For Mid Level Data Scientists, there seems to be a big outlier with an academe position highly paid in 2020. Other than that, the mean salary across roles seem to be fairly even. It also seems to be fairly even across 2021. Over 2022, there is a slight change that we can see which is that the mean salary of Data Scientists and Machine Learning and Artificial Intelligence Roles is darker in the heatmap vs other roles. This could imply a higher importance of the market given to Data Scientist Roles and Machine Learning and Artificial Intelligence Roles.

Looking at the Heatmap from left to right. An interesting pattern can be seen in the Machine Learning and Artificial Intelligence mean salaries. The mean salary of Machine Learning and Artificial Intelligence Roles seems to be trending upwards. 

Another Interesting thing is that there seems to be a Head of Data that was hired in a Mid Level. This may be an outlier or it may show that Head of Data Roles have started appearing for lower experience levels, and we may expect more Head of Data Roles in the future for Mid Level Data Scientists.

For Senior Level Data Scientists, the mean salary seems to be fairly even. This could imply that on a Senior Level, Data Scientists in any role are equally as important as other roles. The only exception is the mean salary of Senior level Head of Data.

Finally on an expert level, the interesting trends seem to come from the missing data. At 2020, there is no entries for expert level Data Analysts, Head of Data, and Machine Learning and Artificial Intelligence Roles. This could imply that the market for these roles is not very large. The biggest importance according to the mean salary is given to the Data Scientist. It could mean that the Data Scientist is more of an umbrella term for expert level positions. On 2021, there is a big outlier in Data Engineering Roles. However, from 2020 to 2022, Data Engineering Experts are steadily gaining importance as seen in their darker mean salaries. It was also only on 2022 where Machine Learning and Artificial Intelligence Roles has appeared. 

----


## Where do Data Scientists go to work coming from a country of origin?

{Interactive Data Explorer 2}

The Network is generated using sample probabilities from the Dataset. The Red Node indicates the country of origin of the data scientist, and it may be connected to itself or other nodes which indicate the countries of the employers of the data scientist. For this analysis, we will focus on the Networks with the top 5 most samples since other countries do not have enough samples to generate proper insights from. The countries with the highest amount of Data Scientist Records are the following:

    * United States (US)
    * United Kingdom (UK/GB)
    * Canada (CA)
    * Germany (DE)
    * India (IN)

A Simple Note: You may find the Network rendered above by selecting the country in the dropdown menu.

Notated below is the proportion of Data Scientists originating from that country that work in/for local companies vs foreign companies.


Country | Local Proportion | Foreign Proportion
---------|-------------------|-------------------
United States (US) | 0.994 | 0.006
United Kingdom (UK/GB) | 0.977 | 0.023
Canada (CA) | 0.966 | 0.034
Germany (DE) | 0.920 | 0.080
India (IN) | 0.800 | 0.200

From the top 5 samples, we can see that majority of the Data Scientists originating from the United States stay there and work for United States Companies with only a little of the US-originating Data Scientists migrate and work for foreign companies. This trend is also seen in the United Kingdom and Canada with greater than 95% of the proportion of Data Scientists staying to work for local companies. Germany has a lower proportion of Data Scientists staying to work for local companies, but is still quite high with a 92% probability of working for local companies. India, however, seems to have the lowest among the top 5 countries with only 80% of the Data Scientist staying to work for local companies and 20% migrating to other countries to work for local companies.

Let's look at it in a different perspective. Graphing the network of the top 5 countries with the highest amount of Data Scientist Records, we can check how much of the country's Data Scientist population is coming from local Data Scientists and Foreign Data Scientists. Notated below is how much of the Country's Data Science Manpower are local and foreign

Country | Local Data Scientist Proportion | Foreign Data Scientist Proportion
---------|-------------------|-------------------
United States (US) | 0.9294 | 0.0706
United Kingdom (UK/GB) | 0.9149 | 0.0851
Canada (CA) | 0.9333 | 0.0667
Germany (DE) | 0.8214 | 0.1786
India (IN) | 1.0000 | 0.0000

Some interesting insights come from these data. First, Germany has the highest foreign Data Science population compared to other countries. Second, India's Data Science Manpower is purely local. Lastly, the other top 5 countries has a high amount of local power (> 90% of the Data Scientist Population). 

Combining the two analysis, we can provide a description of the Data Science Scene in the top 5 most sampled countries according to the data.

Country | Data Science Scene Description
--------|--------------------------------
United States (US) | The United States has a high amount of local Data Scientist that decide to stay and work for local companies which constitutes 99.4% of the US Data Scientist Population. Although majority of the country's Data Science Manpower comes from Local Data Scientists, 7% come from a variety of countries (19 Countries), making the United States' Data Science Manpower quite diverse in culture.
United Kingdom (UK/GB) | Data Scientists in the United Kingdom have a 97.7% probability of staying in the UK and working for local companies in a Data Science Role which is quite high. In terms of its Manpower, it is second to germany in terms of the highest amount of Foreign Data Scientists. In the network, we can see that Data Scientists, in the dataset, come from 4 different countries, which make it quite diverse.
Canada (CA) | Data Scientists in Canada have a 96.6% probability of staying in Canada and working for local companies in a Data Science Role which is quite high. In terms of its Manpower, 93.33% of it comes from local Data Scientists, and 6.67% come from Foreign Data Scientists. Looking at the network, however, we can see that it is not quite diverse, with its foreign Data Scientist population coming from the US and Great Britain only.
Germany (DE) | Data Scientists in Germany have a 92% probability of staying in Germany and working for local companies in a Data Science Role which is high. In terms of its Manpower, 82.14% of it comes from local Data Scientists and 17.86% comes from foreign Data Scientists. Among the 5, Germany is the country with the highest Foreign Data Scientist Proportion. Along with that, Germany has quite a diverse Foreign Data Scientist population which comprises of Data Scientists from 4 different countries. 
India (IN) | Data Scientists in India have a 80% probability of staying in India and working for local comapnies in a Data Science Role, which is considerably lower than the other top 5. Despite this high migration rate, however, India's Data Scientist Manpower is purely local, and no foreign Data Scientist Import exist in the dataset.

