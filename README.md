# **P4 - TBD but nicknamed Will Friend in my head currently**
## Developer: Arielle Gironza

[**Link to GitHub**](https://github.com/akgironza/P4-Backend)
[**Link to Deployed Site**](https://will-friend-backend.onrender.com)
[**Link to Trello**](https://trello.com/invite/b/afFTPZvC/ATTIcb04bf921b28367ebd650746bc9e8cf4809C3687/p4-ga-seir)

### Project Description
An app for users to easily create a will, log their assets, and manage the inheritance of their assets during every day life in an accessible way. 

### Technologies Used
HTML, CSS, SASS, Python, JavaScript, PostgreSQL, Django, ReactJS, Neon, Express.js

## List of Django Backend API Routes
**For the purposes of this project, WILL and ASSET models will be the focus**

### WILL
|ENDPOINT|METHOD|PURPOSE|
|--------|------|-------|
|/will|GET|Index - Show all wills|
|/will/:id|DELETE|Destroy - Delete a will|
|/will/:id|PUT|Update - Update a will|
|/will|POST|Create - Create a new will|
|/will/:id|GET|Show - Show one will with full details|

### ASSET
|ENDPOINT|METHOD|PURPOSE|
|--------|------|-------|
|/asset|GET|Index - Show all assets|
|/asset/:id|DELETE|Destroy - Delete an asset|
|/asset/:id|PUT|Update - Update an asset|
|/asset|POST|Create - Create a new asset|
|/asset/:id|GET|Show - Show one asset|

### INHERITOR
|ENDPOINT|METHOD|PURPOSE|
|--------|------|-------|
|/inheritor|GET|Index - Show all inheritors|
|/inheritor/:id|DELETE|Destroy - Delete an inheritor|
|/inheritor/:id|PUT|Update - Update an inheritor|
|/inheritor|POST|Create - Create a new inheritor|
|/inheritor/:id|GET|Show - Show one inheritor|

### INHERITOR GROUP
|ENDPOINT|METHOD|PURPOSE|
|--------|------|-------|
|/inheritor-group|GET|Index - Show all inheritor groups|
|/inheritor-group/:id|DELETE|Destroy - Delete an inheritor group|
|/inheritor-group/:id|PUT|Update - Update an inheritor group|
|/inheritor-group|POST|Create - Create a new inheritor group|
|/inheritor-group/:id|GET|Show - Show one inheritor group|

### DISTRIBUTION
|ENDPOINT|METHOD|PURPOSE|
|--------|------|-------|
|/distribution/:id|DELETE|Destroy - Delete a distribution|
|/distribution/:id|PUT|Update - Update a distribution|
|/distribution|POST|Create - Create a new distribution|


### Entity-Relationship Diagram
![Picture of ERD](willapp/P4_ERD.png)