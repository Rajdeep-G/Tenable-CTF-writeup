Try to complete the qr code. (may be physically)

Important tool to decode the qr 
https://merricx.github.io/qrazybox/

we get the data block ar 
Data blocks :


a=["11110001","10100100","00010111","01100110","01101100","01100001","01101101","01111110","01100100","00110100","01101101","01101110","01011111","01101001","01110100","01011111","01110111","00110000","01101110","01110100","01011111","01110011","01101011","00110100","01101110","01111101","00000001","00101100","00010001","11101100","00010001","11101100","00010001","11101100","00011000","11011011","11100111","11001011","01001011","10110001","01111100","00111110","01100011","11111110"]

Its enough now to complete the question

```py
print([ chr(int(x, 2)) for x in a])
```

## flag{d4mn_it_w0nt_sk4n}


Additional : https://medium.com/@nteezy/how-to-decode-a-partially-visible-or-damaged-qr-code-a-ctf-writeup-for-stack-the-flags-2020-4ef0eb6a018f