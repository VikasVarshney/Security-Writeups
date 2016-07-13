# [Natas 8](http://overthewire.org/wargames/natas/natas8.html "Natas 8 Web Challenge Page")


We use the password from the previous challenge to log into Natas 8. After logging in, the challenge says:

`Input secret: `

This sounds like one of the challenges we have doen before! :D So we view the source code and find:

```
<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

This encodeSecret function base 64 encodes the secret, reverses it and the converts it from binary to hex. Then it checks to see if we have ligitamately submitted the form and the secret matches the encoded secret. Sounds like some fun reverse engineering (barely :p )

I took this into phpfiddle, and started to reverse the order in which the functions are called, and put in the encoded secret. This was my final code:

```
<?php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($secret) {
	return base64_decode(strrev(hex2bin($secret)));
}

echo decodeSecret($encodedSecret);
?>
```

This spit out that the original secret was `oubWYf2kBq`. When puttign the secret into the textbox, we got a message:

`Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`

We got the pasword! :D

With that password, we can now log into [Natas9](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas9 "Natas 9")