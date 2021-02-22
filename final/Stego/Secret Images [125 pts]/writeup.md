First idea : two images are almost similar. 


Useful link : https://stackoverflow.com/questions/8504882/searching-for-a-way-to-do-bitwise-xor-on-images
(P.s. - I did by reading this one.)

`convert crypted1.png crypted1.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" img_out`

![img](./output.PNG)

## flag{otp_reuse_fail}