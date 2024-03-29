# Delays/Cancellations

## Group Members

|   Info      |        Description     |
| ----------- | ---------------------- |
| TeamID      |        Team-112        |
| TeamName    | Delays/Cancellations   |
| Captain     |       Brandon Baez     |
| Captain     |    baez5@illinois.edu  |
| Member1     |   Janina Mangulabnan   |
| Member1     |    jsm7@illinois.edu   |
| Member2     |       Sakshi Rane      |
| Member2     |  ssrane2@illinois.edu  |
| Member3     |      Kuangji Chen      |
| Member3     | kuangji2@illinois.edu  |

## Course Information
|   Info      |        Description     |
| ----------- | ---------------------- |
| Instructor  |      Abdu Alawini      |
| Instructor  |  alawini@illinois.edu  |
| Project TA  |      Yadniki Pawar     |
| Project TA  |  ympawar2@illinois.edu |


## Project Information

|   Info      |        Description     |
| ----------- | ---------------------- |
|  Title      |Flights and Cancellations|
| System URL  |           TBD          |
| Video Link  |           TBD          |

## Project Summary


We want to make sure that, given a flight between two places, if there exists a flight to another location that can be considered 'connecting,' that there would be a low probability that the flight is either cancelled or delayed. If one location is known for having higher than average cancellations or delays, then we don't want a person to book that airport as a connecting flight. Our program aims to determine the data surrounding the cancellation or delays of flights, using data from 2015, and relating it to the other information of each flight, such as the airline and date. The dataset includes start and destination airports, as well as the status of completion of the light. 
  The user will be able to select an airport and return the number of cancelled and delayed flights, as well as the frequency of a flight being cancelled or delayed. The user will also be able to see a breakdown of how often each delay occurred with a visualization generated by the program. The user is able to choose the information given a specific airport or city, or they can choose to see the airports with the most or least delays. 
  Our second function is able to predict how likely a cancellation or delay is given two airports, not including the destination. If calculates the result using the probabilty of the source and connecting airport. The probability is calculated using the amount of times that the flight is delayed divided by the total amount of flights using the specified paramenter (such as locaiton, airline).
  The final part of the project will allow the user to be able to view graphs and plots generated from the data set. This can be used more by people who prefer physical representations of data. 


## Task Breakdown

### Frontend
Frontend will focus on creating and designing the User Interface of the application, as well as connecting the backend code.
#### Members:
|   Info      |        Description     |
| ----------- | ---------------------- |
| Frontend    |       Sakshi Rane      |
| Frontend    |  ssrane2@illinois.edu  |
| Frontend    |   Janina Mangulabnan   |
| Frontend    |    jsm7@illinois.edu   |

### Backend
Backend will focus on the logistics of the application, including database design, visualization, and storage. Such tasks would include figuring out what structures to use to store the data, what libraries should be used to create graphs and visualizations, and how the database will INSERT, UPDATE, and DELETE data and user input.
#### Members:
|   Info      |        Description     |
| ----------- | ---------------------- |
| Backend     |       Brandon Baez     |
| Backend     |    baez5@illinois.edu  |
| Backend     |      Kuangji Chen      |
| Backend     | kuangji2@illinois.edu  |
