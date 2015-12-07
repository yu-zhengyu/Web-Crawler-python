# Web Crawler for CMU 11601

## Using the Crawler

### Project Dependencies
* This project has external dependencies on the following packages:
    1. WordCloud
    2. Image
    3. Matplotlib
    4. BeautifulSoup 4
    5. PrettyTable
    6. MySql
* Prior to building the project, make sure that you have all the external packages installed by running:
```
sudo pip install wordcloud image matplotlib beautifulsoup4 prettytable mysql
```

### Running the Crawler
* To start crawler
    * Type
        ```
        python cralwer.py Keyword Mode
        ```
    * By default, the crawler runs in DFS with keyword "java"
    * User should enter both the keyword and crawling method ("dfs" or "bfs") in order to override default setting
* To pause routine:
    * control + C
    * To resume, press any key
    * To exit, type "quit"

### Important Note About Email Notification Feature
* Since we do not maintain an email server, emails are sent to the Gmail server (other types of email accounts are currently not supported)
* In order to use the email notification feature, users need to have a Gmail account (or sign up for one)
* Users need to allow "less secure apps" in their Gmail settings 

## Project Requirements

According to the project handout, our crawler needs to have the following features at the very least:
* Takes as input keywords that must be present on a web page
* Recursively crawls links on a web page
* User may specify breadth-first or depth-first crawling
* Rests at least two seconds between each recursive step for pages within the same domain (no rest required for pages on other domains)
* Can be terminated at any time by the user
* Has no preset limit to recursion depth
* Stores data in a database
* Provides real-time status to the user about how many pages has been crawled, what is currently being crawled, what is planned, etc. (use some creativity here)
* May be either command line or web-based application.
* Define at least four additional features not listed above

## Database part
* This project uses mysql database
* This project assumes that you have already create a database named "test" in mysql. And you should have a database user named "root", the passwprd should be "root".
the database will store the data in local machine.
* if you do not want to use a new database or new user and new password or you want to store the data in remote machine, you need to change the following code 
* [con = mdb.connect('localhost', 'root', 'root', 'test');]
* as [con = mdb.connect(New_address, New_user, New_password, New_database_name);]
* When user runs the crawler, the database will creates a table name keywordKEYWORD_dfs(bfs). in this table, we record the title, link of website and the insert time.
* When the code quits, the database will create two other tables, one is used to store the websites in visited list named KEYWORDvisited_dfs(bfs), another is used to
store the websites in unvisited list named KEYWORDunvisited_dfs(bfs), in otherwords, we will have threetables if we quit the code. otherwise only one table.
* Every time when the code starts, the code will check if there are responding table in database, if yes, user can choose start from the previous point or restart 
from the beginning.
* There is a file named "saveDate" which contains functions to put one record into database once.