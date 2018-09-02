# Item_Catalog
This is a website that allows users to browse items in different catgories. The items are maintained by admins (users who have been authorized and authenticated by Google OAuth APIs). 

- Users can add items (title, description, category).
- An item can only be updated/deleted by the user who created it.

## Website info
1. **IP address**
- 52.35.137.157 (hosted on **Amazon Lightsail**)

2. **URL**
- http://itsawesomeweb.tk/

3. **Summary of software/modules installed**
- WSGI (Apache/Python interface)
- itsdangerous (Python token signing module)
- PostgreSQL (database)
- sqlalchemy (Python SQL toolkit)
- passlib.apps (Python password hashing library)
- requests (Python HTTP requests handling module)
- Flask (Python web server framework)
- Flask-HTTPAuth (Python HTTP authentication extension)
- oauth2client (Google OAuth client-side library)

4. **Summary of configurations made**
- Allowed only connection from port 80(HTTP), 2200(SSH) and 123(NTP) using UFW (uncomplicated fire wall) and Lightsail networking.
- Switched ssh port from 22 to 2200.
- Disabled login as `root`.
- Allowed only Key-based authentication for remote login to the server.
- Created a ubuntu user `grader` which was granted `sudo` access (a rsa key locates in ~/.ssh/authorized_keys).
- Turned `WSGIPassAuthorization` on to allow user authentication via Flask `@auth.verify_password`

5. **List of third-party resources used to complete this project**
- Google OAuth 2.0 APIs

## Skills Applied
1. PostgreSQL database for data storage
2. Python server side back-end scripts running on Flask
3. Client side front-end web pages using Bootstrap JS framework for UI
4. A JSON endpoint that serves the same information as displayed in the HTML endpoints
4. RESTful APIs for CRUD implementations
5. Third party OAuth 2.0 service (Google) for user authentication
6. User token signing using Python module itsdangerous
7. Cross-Site Request Forgery (CSRF) protection using session state
8. Post-Redirect-Get (PRG) pattern to prevent false submission

## Database Schema
User

| Column        | Type          |
| ------------- |:-------------:|
| id            | Integer       |
| username      | String        |
| email         | String        |
| picture       | String        |
| passwor_hash  | String        |

Category

| Column        | Type          |
| ------------- |:-------------:|
| id            | Integer       |
| name          | String        |

Item

| Column        | Type          |
| ------------- |:-------------:|
| id            | Integer       |
| name          | String        |
| description   | String        |
| category_name | FK(Category)  |
| user_id       | FK(User)      |

## Access JSON endpoint using curl

**Get the app JSON data using credential**
```
$ curl -i -u "testuser":"testps" "http://itsawesomeweb.tk/categories.json"
```

**Get the app JSON data using token**

Generate signed tokens (Note: token expires after 10 mins)
```
$ curl -X POST -i -u "testuser":"testps" "http://itsawesomeweb.tk/tokens"

Response:
{
  "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzMTg5NDY1OSwiaWF0IjoxNTMxODk0MDU5fQ.eyJpZCI6MX0.66mzV4LW6t3BsQMY2tYuBQ3xx8zZiNlPRf5M6IB5uro"
}
```
And then apply the token as the credential

```
$ curl -i -u tokenString:blank "http://itsawesomeweb.tk/categories.json"
```



## Website Screenshots
Show latest items (http://itsawesomeweb.tk/categories)
![alt text](figures/show_latest.png "Show latest items")

Show latest items (logged in) 
![alt text](figures/show_latest_logged_in.png "Show latest items logged in")

Show category items (http://itsawesomeweb.tk/categories/Soccer/items)
![alt text](figures/show_category.png "show category")

Show item description (http://itsawesomeweb.tk/categories/Baseball/Helmet)
![alt text](figures/show_description_hide.png "show description hide")

Show item description (the user who created it) (http://itsawesomeweb.tk/categories/Rock%20Climbing/Glasses)
![alt text](figures/show_description.png "show description")

Login screen (http://itsawesomeweb.tk/login)
![alt text](figures/login.png "login")

Add item (http://itsawesomeweb.tk/categories/items/add)
![alt text](figures/add.png "add")

JSON endpoint (http://itsawesomeweb.tk/categories.json)
![alt text](figures/json_endpoint.png "json endpoint")
