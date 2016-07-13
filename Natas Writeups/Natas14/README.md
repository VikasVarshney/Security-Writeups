# [Natas 14](http://overthewire.org/wargames/natas/natas14.html "Natas 14 Web Challenge Page")


We use the password from the previous challenge to log into Natas 14. After logging in, the challenge shows us an input point for a username and a password. We go straight into looking at the source code.

In the source code, we can see that the challenge is using unsanitised inputs, through `$_REQUEST`. This means we may be able to complete an SQL Injection attack, to make us login without authentication details. Our first job is to analyse how the SQL is working. 

`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";`

The SQL is using `"` (double quotes), which we have to end, and then make all cases true. After that, we must comment out the rest of the query (this is one way of doing it). The payload I used is given below:

`" or 1=1 -- `

This makes all usernames match (as `1=1` will always be true). This gives us the password:

`Successful login! The password for natas15 is AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`

With that password, we can now log into [Natas15](https://github.com/ProDigySML/Security-Writeups/tree/master/Natas%20Writeups/Natas15 "Natas 15")
