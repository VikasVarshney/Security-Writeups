# [Natas 4](http://overthewire.org/wargames/natas/natas4.html "Natas 4 Web Challenge Page")


We use the password from the previous challenge to log into Natas 4. After logging in, the challenge says:

`Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/" `

Here the page implies that the user should come only from a specified URL. In the HTTP header, we can specify a `Referer:`. This allows us to show the page, that we are coming from a different URL (or location), than we actually are. 

![Natas 4 Referer Request](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas4/Natas4RefererRequest.PNG "Natas 4 Referer Request")

After sending the request, in the source code, we can see that access has been granted and the password for the next user is given:

`Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

With that password, we can now log into [Natas5](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas5 "Natas 5")