<div id="top"></div>
<br />
<div align="center">
  <!-- <a href="">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h2 align="center">OSC Inventory API</h3>

  <p align="center">
    An api to work with the database and return info to the frontend
    <br />
    <a href="https://osc-api.fusionsid.repl.co/docs"><strong>FastAPI Docs / Url »</strong>
    <a href="https://thisisbraindamage.github.io/OSC-API/"><strong>Code DocsUrl »</strong></a>
    <br />
    <br />
  </p>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About The Project

This is an api that was gonna be used for school. 
This api never ended up getting used because we weren't able to get the inventory list :(
But i learnt alot making it so yea it's fine.

## How it works / How to use

### Authentication

**OAuth2:**

This api uses a simplified version of OAuth2. You use a username and password to get an access_token which you will use for your requests.

On every request sent to the api, The api will check the request body to check if it has the "Authorization" header

If you don't have the header it will return that you are unauthorized. If you do it will check the value of the header. This is where the token is supposed to be.

Tokens are encrypted text which contain information about the user. The token will be decrypted with the same secret key that was used to encrypt it and the user info will be extracted from it.  

Then the api will lastly find a user with that info and if it finds a user then you will be authenticated ad can use the endpoint.

So how do you get a token?

1. First of all you must have access to the API, you can't currently make an account and since this project is archived I won't be adding more account either 

2. Next you must make a POST request to the token endpoint. In the request data you attach your Username and Password.  

Example in Python:
```py
import requests

url = "https://osc-api.fusionsid.repl.co/token"
data = {
    "username" : "Your Username",
    "password" : "Your Password"
}
response = requests.post(url, data=data).json()

token = response["access_token"]
```

Yay now you have a token, Now for all future requests put that token in the "Authorization" header, If you loose the token just make another request to the token endpoint

**Users**:

Users are creates and stored in a local sqlite database.  
The `User` class has 3 attributes: username, hashed_password and disabled

User passwords are stored hashed and encrypted using the `pbkdf2_hmac` and `sha256` algorithms which is impossible to reverse. Basicaly it encrypts the password+salt and then encrypts it again and again and again - How many times? definitely more that 150,000 iterations.

The password is never actualy stored. It is encrypted using a process that will always return the same result so when you enter a password it will encrypt that and check if that result is the same as the encrypted one that is stored in the db.

Currently theres no way to create an account apart from using the function which only i can do.

<!-- ### Endpoints / API

**Insert**

Insert:



New Item:



**Delete**

Delete:



Delete All:



**Get**

Get All:



Find Item:


 -->
### Database

Database is hosted somewhere and uses postgresql. I use asyncpg to send SQL commands to the database.


<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

- [x] Create testing API

- [x] Make sure Dhruv is able to make requests properly

- [x] Make the oauth2 system

- [x] Create the users endpoints

- [x] Create database functions

- [x] Make db endpoints

- [x] Reformat code

- [x] Documentation for code

<p align="right">(<a href="#top">back to top</a>)</p>


## Contributing

Contributions are what make the open source community such an amazing place. Any contributions you make are greatly appreciated.


## License

Distributed under the MIT License. See [LICENSE](/LICENCE) for more information.


## Contact

Siddhesh Zantye - [School Email](mailto:st22209@ormiston.school.nz)

<p align="right">(<a href="#top">back to top</a>)</p>
