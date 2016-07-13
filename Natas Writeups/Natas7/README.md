# [Natas 7](http://overthewire.org/wargames/natas/natas7.html "Natas 7 Web Challenge Page")


We use the password from the previous challenge to log into Natas 7. After logging in, the challenge has two links namely `Home` and `About`, which lead to an included page (will show how I found that out soon). 

Once we click on the `Home` link, we find that the url changes into:

`http://natas7.natas.labs.overthewire.org/index.php?page=home`

From that, we can see that the page parameter is changing the content of the page. We can add in a `/` and the page will display an error (sayign it could not include the file, as it does not exist). It took me a bit to remember that a clue was given on the homepage of natas:

`All passwords are also stored in /etc/natas_webpass/. E.g. the password for natas5 is stored in the file /etc/natas_webpass/natas5 and only readable by natas4 and natas5.`

Seeing this, it was simple. I changed the url to become:

`http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8`

This gave me a password:

`DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`


With that password, we can now log into [Natas8](https://github.com/ProDigySML/Security-Writeups/Natas/Natas8 "Natas 8")

PS. We can also leak the source code of the pages! :D