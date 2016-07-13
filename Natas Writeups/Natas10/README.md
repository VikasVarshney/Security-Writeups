# [Natas 10](http://overthewire.org/wargames/natas/natas10.html "Natas 10 Web Challenge Page")


We use the password from the previous challenge to log into Natas 10. After logging in, the challenge says:

`Find words containing:`

This seems to be just like the last challenge. So we move into the sourcecode, and see the changes to the php code:

```
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
```

There seems to be some blacklisting present. Due to this regular expression, we can no longer use `;` or `|` or `&`, which makes the RCE a bit harder! Since we can't actually end the statement anymore, we should try to change the way it works, to fit our purpose. 

For this challenge, we use `.` to find words containing any character (`.` means any character in regex). Then we try to specify our own file, and comment out the rest of the command.

`. /etc/natas_webpass/natas11 #`

The output of the command is:

`U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK`

With that password, we can now log into [Natas11](https://github.com/ProDigySML/Security-Writeups/Natas/Natas11 "Natas 11")
