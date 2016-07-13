# [Natas 2](http://overthewire.org/wargames/natas/natas2.html "Natas 2 Web Challenge Page")


We use the password from the previous challenge to log into Natas 2. After logging in, the challenge says:

`There is nothing on this page`

We look into the source code, and find that the developers haven't left any clues for us :(. 

![Natas 2 Source](https://github.com/ProDigySML/Security-Writeups/Natas/Natas2/Natas2Source.PNG "Natas 2 Source")

There we can see that there is an image (cannot see on the GUI end). The image is stored in a directory called files (a little suspicious). We open the image (it's a 1x1 pixel image). We adjust the url to open the files directory:

`http://natas2.natas.labs.overthewire.org/files`

Due to a poor .htaccess file, and the absence of an index file, we can view which files are present in the directory. We open the user file and find the passwords:

`natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14`

With that password, we can now log into [Natas3](https://github.com/ProDigySML/Security-Writeups/Natas/Natas3 "Natas 3")