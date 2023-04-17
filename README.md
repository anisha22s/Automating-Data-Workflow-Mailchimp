# **Mailchimp-with-API**

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

Accessing survey response from Mailchimp
Extracting list ID for the desired audience
Finding the survey ID for the specified survey title
Extracting all the response IDs for that particular survey
Using the response IDs to extract all the survey responses
Cleaning the responses dataframe in a desired format, separating response answers into different columns for easy integration with Tessitura

**Feel free to modify this README file to fit your specific needs. The survey questions will be different**

## **Reference**

Please refer to Mailchimp API documentation guide

https://mailchimp.com/developer/marketing/api/root/

