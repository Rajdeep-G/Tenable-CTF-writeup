given   
`wAAAAAIwAB4AAABhYmNkZWZnaGppa2xtbm9wcXJzdHV2d3h5el97fQAEMQCTAAAAEDAABQAAABAxAAsAAAAQMgAAAAAAEDMABgAAABA0ABsAAAAQNQASAAAAEDYADgAAABA3AA0AAAAQOAAaAAAAEDkADgAAABAxMAAFAAAAEDExABoAAAAQMTIAAAAAABAxMwAaAAAAEDE0AAEAAAAQMTUAEgAAABAxNgAOAAAAEDE3AA0AAAAQMTgAHAAAAAAA`

Note- Its not a json actually. Its a `BSON`

So any online tool can be used.
eg https://mcraiha.github.io/tools/BSONhexToJSON/bsonbase64tojson.html

Now, converted json: 
```json
{ "0": "abcdefghjiklmnopqrstuvwxyz_{}", "1": [ 5, 11, 0, 6, 27, 18, 14, 13, 26, 14, 5, 26, 0, 26, 1, 18, 14, 13, 28 ] }
```

A simple script can do the rest. 

```py
s="abcdefghjiklmnopqrstuvwxyz_{}"
l= [ 5, 11, 0, 6, 27, 18, 14, 13, 26, 14, 5, 26, 0, 26, 1, 18, 14, 13, 28 ]
ans=""
for i in range(len(l)):
    ans+=s[l[i]]
print(ans)
```
## `flag{son_of_a_bson}`