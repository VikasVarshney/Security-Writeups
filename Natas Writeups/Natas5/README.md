# [Natas 5](http://overthewire.org/wargames/natas/natas5.html "Natas 5 Web Challenge Page")


We use the password from the previous challenge to log into Natas 5. After logging in, the challenge says:

`Access disallowed. You are not logged in`

We can look into the source code, however, for this level, it is of no use. I looked over the response I got from the server, and saw that a cookie was set:

`Set-Cookie: loggedin=0`

After seeing that, I was confirmed that all I had to do was change the value of the cookie and log into the system. I sent a request from my system, after altering the cookie value to 1, and the challenge responded with the following:

`Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`

With that password, we can now log into [Natas6](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas6 "Natas 6")