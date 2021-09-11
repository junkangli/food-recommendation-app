# junkang's Food Recommendation App

## Technology

The application is mainly written in Python since it is dictated that for 
> API call shall be made via python

And uses [Flask](https://flask.palletsprojects.com/) because it seems to be a popular Python-based web framework. 
[Poetry](https://python-poetry.org/) is used for dependency management because of familiarity with the tool.
[Bootstrap](https://getbootstrap.com/) is used for styling the web site.
For deployment to Amazon Web Services, AWS Elastic Beanstalk is used due to its ease of use.
In addition, Amazon Rekognition is used to add image analysis based on photo uploaded by user to search for meal description.

## Infrastructure

The application is hosted in Singapore region on an Amazon Linux EC2 instance to adhere to the requirements that states to 
> Set up your own AWS free tier VM

The instance is a `t2.micro` instance type that is in an Auto Scaling group (ASG) to keep it available.
The ASG is configured to automatically add 1 instance when outbound network traffic is high.
A Load Balancer (ELB) is configured to handle the traffic and route it to the ASG.