# [Natas 0](http://overthewire.org/wargames/natas/natas0.html "Natas 0 Web Challenge Page")

When accessing natas 0, we face an HTTP authentication page. 

![Image for HTTP Auth page](https://github.com/ProDigySML/Security-Writeups/Natas/Natas0/Natas0Auth.PNG "HTTP Auth page")

After seeing this page, we add in the authentication details for natas 0 (as given in the natas websiite). 

The challenge prompts us to find a password for the next level on this page. So we open up the source code of the page, to see what kind of code is present (looking into any hidden information). There the find:

`<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->`

![Image for Natas0 Comment page](https://github.com/ProDigySML/Security-Writeups/Natas/Natas0/Natas0Comment.PNG "Natas 0 Comment")

With that password, we can now log into [Natas1](https://github.com/ProDigySML/Security-Writeups/Natas/Natas1 "Natas 1")