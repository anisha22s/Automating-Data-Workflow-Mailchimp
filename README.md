# **Mailchimp-with-API**

As part of UC Davis MSBA program, I worked as a Data Analyst for a performing arts center.
This repository contains code that allows you to access survey responses from your Mailchimp account in real-time using Mailchimp API's. The responses are then formatted into a Pandas dataframe for easy integration with other tools.

## **Installation**

You will need to have the mailchimp-marketing package installed. You can install it using the following command:

pip install mailchimp-marketing  

## **Usage**

To use the code, first replace the placeholders in the following lines with the desired audience name and survey title from Mailchimp:

name = '#######'  # replace with desired audience under which the survey will be stored.  
title = '#######'  # replace with desired survey title from Mailchimp. Further code extracts survey responses only from this title. 

Then, replace the API key and server values with your own:

client.set_config({
    "api_key": "#######################",  
    "server": "us11"  
  })  

## **Workflow**

The code performs the following steps:

1. Accessing survey response from Mailchimp
2. Extracting list ID for the desired audience
3. Finding the survey ID for the specified survey title
4. Extracting all the response IDs for that particular survey
5. Using the response IDs to extract all the survey responses
6. Cleaning the responses dataframe in a desired format, separating response answers into different columns for easy integration with Tessitura  
7. Accessing the mailchimp customer data to essentially retrieve Customer ID for each customer  
8. Integrating the survey and customer datasets  


## **Reference**

Please refer to Mailchimp API documentation guide

https://mailchimp.com/developer/marketing/api/root/

## **Credits**

Project created entirely by Anisha

