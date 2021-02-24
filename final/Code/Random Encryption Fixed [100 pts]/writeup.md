
Since we already had the seeds for the Python random function, we can generate the same sequence of numbers, by just setting the seed. Also we are using the property of XOR which is if `c = a^b` then we can get `a` from `b` and `c` in this way `a = c^b`. Same goes if we swap a with b. 

```py
import random
flag = []
seeds = [9925, 8861, 5738, 1649, 2696, 6926, 1839, 7825, 6434, 9699, 227,
         7379, 9024, 817, 4022, 7129, 1096, 4149, 6147, 2966, 1027, 4350, 4272]

res = [184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76,
       10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]

for i in range(0, len(seeds)):
    # setting the seed value
    random.seed(seeds[i])
    rands = []
    for j in range(0, 4):
        rands.append(random.randint(0, 255))
    
    # XORing the final res with the generated rand to get the flag value
    flag.append((res[i]) ^ rands[i % 4])
    del rands[i % 4]
    # print(str(rands))

print(''.join([chr(x) for x in flag]))
# print(seeds)
 ```

## flag{Oppsie_LULZ_fixed}

### Follow Up

At this point there is no importance of `print(str(rands))`. Cause we are already given the seeds value. A better version of the question could have been, if the initial seed was in the definite range. Actually, it won't be better it will still be basic brute forcing. 
