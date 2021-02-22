All you need to do is create a perfect command with the correct regex. 



`grep -Eo 'flag{[a-z_]{10,16}}' haystack.txt | sort | uniq -u`

You will find the flag at the last line.

## flag{thy_flag_is_this}