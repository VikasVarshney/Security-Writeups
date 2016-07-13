# [Natas 6](http://overthewire.org/wargames/natas/natas6.html "Natas 6 Web Challenge Page")


We use the password from the previous challenge to log into Natas 6. After logging in, the challenge says:

`Input secret: `

Below this input box, there is a link which says `View sourcecode`. Obviously, this is something that will interest us (unless they are trying to mislead us). We open up the link. 

There we can see the php code behind the challenge. When analysing the code, we see something quite interesting:

Line 17: `include "includes/secret.inc";`

This is pointing to a file, where the `$secret` variable is set. We open the file, and see nothing :(. Then we open up the page source and see, there is php code, which is not normally visible (this is because, the file name has `.inc` as its file path, which does not tell the server to execute the file as a php file. 

We copy the secret and go back to the inital natas 6 screen, and put the secret in the text box! There we see:

`Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 `


With that password, we can now log into [Natas7](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas7 "Natas 7")