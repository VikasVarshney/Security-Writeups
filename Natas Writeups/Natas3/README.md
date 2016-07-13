# [Natas 3](http://overthewire.org/wargames/natas/natas3.html "Natas 3 Web Challenge Page")


We use the password from the previous challenge to log into Natas 3. After logging in, the challenge says:

`There is nothing on this page`

In a comment, we can see:

`<!-- No more information leaks!! Not even Google will find it this time... -->`

This implies that no search engine will find the files this time. This straight away brings our attention to the `robots.txt` file. This is a file, which tells search engine spiders, which directories are present, and which ones they should not traverse and list the pages of. 

From the `robots.txt` file, we find that a `s3cr3t` directory exists. Lets go into the directory, and see what we can find! Again we find a poorly configured directory, where we can access the `user.txt` file, and find the user's password:

`natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`


With that password, we can now log into [Natas4](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas4 "Natas 4")