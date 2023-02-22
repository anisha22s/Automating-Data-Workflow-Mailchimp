# -*- coding: utf-8 -*-
"""mailchimp connect (mondavi) .ipynb


"""

pip install mailchimp-marketing

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import pandas as pd

"""**AUTOMATED DATA WORKFLOW PROCESS FOR CUSTOMER FEEDBACK DASHBOARD**

STEP1: Accessing survey response from Mailchimp
"""

#****#
name = '#######'  #****replace with desired audience under which the survey will be stored*****
title = '#######'  #****replace with desired survey title from mailchimp. Further code extracts survey responses only from this title*****

#First we will extract list_id. 
#list ID will be unique for each auudience (The Mondavi Center, Mondavi arts education and event cancellation)
#we need to extract the list ID for the audience under which the survey is stored

#For this instance, our desired audience is 'The Mondavi Center'

client = MailchimpMarketing.Client()
client.set_config({
    "api_key": "#######################", 
    "server": "us11"
  })

all_list = client.lists.get_all_lists()



for listi in all_list['lists']:
    if listi['name'] == name:
        list_id = listi['id']
        break

print(list_id)

#next, we will find out the survey id for a specific survey using the title of the survey
surveysinfo = client.lists.get_all_surveys_for_list(list_id) 



for survey in surveysinfo['surveys']:
    if survey['title'] == title:
        survey_id = survey['id']
        break

print(survey_id) #survey_id for your specified survey title

#extracting all the response ids for that particular survey
data_response = client.reporting.get_survey_responses_all(survey_id)#get all responses meta data 

response_ids = [resp.get('response_id') for resp in data_response.get('responses', []) if resp is not None] #extract all the response ids 
print(response_ids)

#using the response ids to extract all the survey responses

responses = [] # list to store all the responses

for response_id in response_ids:
    response = client.reporting.get_survey_response(survey_id, response_id)
    responses.append(response)

# create a dataframe from the responses
df = pd.DataFrame(responses)

"""In the next piece of codes, we will clean the responses dataframe in a dfesired format, separating response answers in different columns for easy integration with tessitura """

# the values in the contact column are stores as a dictionary. in the next code, we will separate them into different columns
df_contact = pd.json_normalize(df['contact'])

# Join the two DataFrames on the index to keep the other columns in the original DataFrame
dfnew = df.join(df_contact)

# Drop the original 'contact' columns
dfnew = dfnew.drop(['contact'], axis=1)

# Delete columns "avatar_url", "contact_id" and "email_id" from the dataframe as does not give any useful info
#correct email format is already stored under column email
dfnew = dfnew.drop(["avatar_url", "contact_id", "email_id"], axis=1)

# Move the "results" column to the end of the dataframe (not required, just for better visualizing)
cols = list(dfnew.columns)
cols.remove("results")
dfnew = dfnew[cols + ["results"]]


#next we will also format the results column to separate all answers in different columns
#Creating the data frame with a single column 'results'
new_df = dfnew[['results']]

# column names for the new columns from results
dfnew2 = pd.DataFrame(columns=[
    'How satisfied were you with your recent experience at the Mondavi Center?',
    'How likely is it that you would recommend the Mondavi Center to a friend or colleague?',
    'Please feel free to leave any comments about your experience at the Mondavi Center.',
    'Enter your email address:'
])

#next, we will extract only the asnwers from the results column for each of the questions
# Iterating over the rows of the 'results' column
for i in range(len(new_df)):
    row = new_df.loc[i, 'results']
    row_data = {}
    for item in row:
        row_data[item['query']] = item.get('answer', '')
    dfnew2 = dfnew2.append(row_data, ignore_index=True)

#we will format the 'how likely are you to recommend' column to only show score given out of 10 insead of say 8/10
dfnew2['How likely is it that you would recommend the Mondavi Center to a friend or colleague?'] = dfnew2['How likely is it that you would recommend the Mondavi Center to a friend or colleague?'].astype(str).str.extract('(\d+)').astype(int)
 
# Drop the original 'results' columns 
dfnew = dfnew.drop(['results'], axis=1)

# lastly joining the two created dataframes to give the final survey result df
final_surveyresult = dfnew.join(dfnew2)

final_surveyresult.to_csv('final_surveyresult.csv', index=False)

print(final_surveyresult)

                        )
