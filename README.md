# Voice-Controlled-IoT-Devices-with-Amazon-Lex
This project will allow you to control IoT devices using voice commands via a chatbot built with Amazon Lex

---------------------------------------------------------------------------------------------------------------------------

This project enables you to control IoT devices using voice commands. We’ll create a chatbot using Amazon Lex that recognizes voice commands like turning devices on or off, and it will trigger actions via AWS IoT Core using AWS Lambda. The device states will be saved and retrieved using DynamoDB.

AWS Services Used:
Amazon Lex (for chatbot and voice command recognition)
AWS Lambda (for processing the voice commands)
AWS IoT Core (to manage and control IoT devices)
Amazon DynamoDB (to store and retrieve device states)
AWS IAM (for managing permissions)


High-Level Steps:
Set up an IoT device in AWS IoT Core.
Create a DynamoDB table to store device state information.
Create a Lex chatbot to recognize voice commands.
Create a Lambda function to control the IoT device and manage the state in DynamoDB.
Test the voice-controlled IoT device using the Lex chatbot.
