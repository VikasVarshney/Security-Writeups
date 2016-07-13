# [Natas 11](http://overthewire.org/wargames/natas/natas11.html "Natas 11 Web Challenge Page")


We use the password from the previous challenge to log into Natas 11. After logging in, the challenge says:

`Cookies are protected with XOR encryption. ` 

Also, we can edit the background colour of the page. 

A XOR cipher is basically where `A XOR B = C`. However, there is a weakness in the cipher. `A XOR C = B` and `B XOR C = A`. Using this weakness, we will be attempting to find the key. We will be using the XOR function given in the source code, to do so:

```
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

I changed the color to black, to differ from the default value. First we can find the cookie value `ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw%3D`

From this line, we can see that the cookie value is actually base64 encoded.

`$tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);`

Now we need a key. This line gives us where we can get it:

`setcookie("data", base64_encode(xor_encrypt(json_encode($d))));`

This means we can use the default data value, with our cookie value to find the original key. This is the code I used:

```
<?php
function xor_encrypt($in) {
	$d = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    $key = json_encode($d);
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo xor_encrypt(base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw%3D'));
?>
```

This spits out `qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq`, where we can see some reoccuring characters (the characters are the key)! The key is `qw8J`. Now we can create a new value for the cookie, to show the password (after encrypting).

```
<?php
function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo base64_encode(xor_encrypt(json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"))));
?>
```

This spits out an encrypted array, which we can add into out cookie, to make the challenge spit out the password. 

`The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`

With that password, we can now log into [Natas12](https://github.com/ProDigySML/Security-Writeups/Natas/Natas12 "Natas 12")
