# [Natas 12](http://overthewire.org/wargames/natas/natas12.html "Natas 12 Web Challenge Page")


We use the password from the previous challenge to log into Natas 12. After logging in, the challenge says:

`Choose a JPEG to upload (max 1KB):`

When we look into the source code, there is no protection, or any way the challenge maker has enforced file types. So we are free to upload our own shell to gain RCE on the challenge server.

[Shell uploaded to the server](https://github.com/ProDigySML/Security-Writeups/tree/master/Natas%20Writeups/Natas12/shell.php)

There is still one major problem in the exploit. The way the challenge is written, a hidden input element defines the file's name. We can alter this value, and attempt to upload the file as a php file

![Natas 12 changing element value](https://github.com/ProDigySML/Security-Writeups/tree/master/Natas%20Writeups/Natas12/Natas12ChangeElement.PNG "Change Element")

I changed the value to `shell.php`, and then uploaded the file to the challenge server. The output I got was:

`The file upload/xf521ra4hi.php has been uploaded`

I followed the link, and used the RCE to leak the password.

`jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`

With that password, we can now log into [Natas13](https://github.com/ProDigySML/Security-Writeups/tree/master/Natas%20Writeups/Natas13 "Natas 13")
