# [Natas 13](http://overthewire.org/wargames/natas/natas13.html "Natas 13 Web Challenge Page")


We use the password from the previous challenge to log into Natas 13. After logging in, the challenge says:

```
For security reasons, we now only accept image files!

Choose a JPEG to upload (max 1KB):
```

The line that has changed to ensure that the file header is that of a jpg is:

```
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    }
```

To create the jpg web shell, I wrote the following python script:

[Python Script](https://github.com/ProDigySML/Security-Writeups/tree/master/Natas%20Writeups/Natas13/makeImageShell.py)

We made the php file look like a JPG file, and we received the following response:

```
For security reasons, we now only accept image files!

The file upload/9qbkvqwqnv.php has been uploaded
```

After visiting this URL, we can leak the password, using our RCE!

`Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`

With that password, we can now log into [Natas14](https://github.com/ProDigySML/Security-Writeups/blob/master/Natas%20Writeups/Natas14 "Natas 14")
