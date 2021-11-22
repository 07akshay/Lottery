# Lucky Draw Gaming Service
This is an attempt to develop a Lucky Draw gaming Service that allows 
users to participate in a Lucky draw and win exciting prizes.

## Features

- User can request for a lucky draw token to participate in an event
- A user can participate with only one token in one event
- User can request the list of previous winners
- Also, the list of various contests and their rewards can be fetched.

## Design

> The project has been built using **User centric** and **Admin centric APIs**

> User centric APIs include the following : 
- API to get token for participating in a contest
- API to fetch the list of past winners
- API to fetch the contest information - rewards and timings

> Admin centric APIs include the following
- API to add new contests for the users to participate
- API to reschedule a contest
- API to cancel an ongoing contest

> Along with that the result of lottery contest would be determined by running 
the script on the server as a **CRON job** which would be scheduled to run everyday
on a fixed time e.g. at 8:00 am.
This script would also update the winners_table that keeps the record of winners
of past contests.

**The figure demonstrates the structure of the service**

![Alt text](flowchart.png?raw=true "Flowchart")

## Techstack

The project has been built using the following :

- [Python]() - an interpreted high-level general-purpose programming language
- [SQLite3]() - A lightweight replica of MySQL database 
- [Flask]() - To develop the web framework

## API Documentation
- ### To get a token to participate in a contest
    This API returns a hexadecimal equivalent of a unique SHA256 code generated using
    the userID, contest_name and current date.
    This hexadecimal code is used as the token to participate in the Lucky Draw contest
    #### Request
    `POST /allottToken/`
    #### Parameters
    ```sh
    userID
    contest_Name
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
            token : f6071725e7ddeb434fb6b32b8ec4a2b14dd7db0d785347b2fb48f9975126178f
          }
    ```

- ### To get the list of past contest winners
    This API returns the list of past winners along with the corresponding contests and their dates
    #### Request
    `GET /pastWinners/`
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
           contest_name1 : winner_user1,
           contest_name2 : winner_user2,
           ....
          }
    ```

- ### To get the details of contests
    This API returns the list of contests along with their rewards and schedules
    #### Request
    `GET /contestDetails/`
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    Content-Type: application/json
    Body: {
           contest_name1 : [reward1, schedule1],
           contest_name2 : [reward2, schedule2]
           ....
          }
    ```

- ### To add a new contest for the users to participate
    This API lets the admin to add new contest for the users to participate
    #### Request
    `POST /addContest/`
    #### Parameters
    ```sh
    contest_Name
    Reward
    Deadline
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

- ### To modify the deadline of a contest
    This API lets the admin to extend the deadline of a contest
    #### Request
    `POST /extendDeadline/`
    #### Parameters
    ```sh
    contest_Name
    Deadline
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

- ### To remove a contest
    This API lets the admin to remove of an upcoming contest
    #### Request
    `POST /removeContest/`
    #### Parameters
    ```sh
    contest_Name
    Deadline
    ```
    #### Response
    ```
    HTTP/1.1 200 OK
    Status: 200 OK
    ```

## Database Schema
In this project I am currently using SQLite3 as the database due to ease of use 
and demonstration but it can be very easily extended to MySQL. I have created 4 tables
in the database, namely:
- token_tb : stores the token_number, UserID and ContestID
- contest_tb : stores the ContestID, Contest_reward, Contest_date, Contest_name and expired (whether the contest is active or not)
- winners_tb : stores the ContestID, UserID and Rank
- users_tb : stores the UserID and User_name

**The figure demonstrates the database schema of the service**

![Alt text](database.png?raw=true "database")
