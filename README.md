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
    <a href="https://osc-api.fusionsid.repl.co/docs"><strong>Docs / Url »</strong></a>
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

this is api

## How it works / How to use

### Authentication:

This api uses oauth2 but a simplified version. You use a username and password to get an access_token which you will use for your requests.

On every request sent to the api, The api will check the request body to check if it has the "Authorization" header

If you don't have the header it will return that you are unauthorized. If you do it will check the value of the header. This is where the token is supposed to be.

Tokens are encrypted text which contain information about the user. The token will be decrypted with the same secret key that was used to encrypt it and the user info will be extracted from it.  

Then the api will lastly find a user with that info and if it finds a user then you will be authenticated ad can use the endpoint.

So how do you get a token?

1. First of all you must have access to the API, you can create an account at the create_account endpoint and wait for your account to be enabled.

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


<p align="right">(<a href="#top">back to top</a>)</p>

## Roadmap

- [x] Create testing API

- [x] Make sure Dhruv is able to make requests properly

- [x] Make the oauth2 system

- [ ] Create the users endpoints

- [ ] Create database functions

- [ ] Make db endpoints

- [ ] Refactor code

- [ ] Documentation for code

<p align="right">(<a href="#top">back to top</a>)</p>


## Contributing

Contributions are what make the open source community such an amazing place. Any contributions you make are greatly appreciated.

<p align="right">(<a href="#top">back to top</a>)</p>


## License

Distributed under the MIT License. See [LICENSE](/LICENCE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


## Contact

Siddhesh Zantye - [School Email](mailto:st22209@ormiston.school.nz)

<p align="right">(<a href="#top">back to top</a>)</p>

