we simulated users (10 concurrent usrs) using python, selenium ..
Their is a demo website (SauceDemo) where we perform this testing.
logging in, interacting with products, managing the cart, and then loging off,all
tests have been written in python and tested .
Later execution metrics have also been added for more better understanding

## so this is how work test happens in sequence:
```
Start Test
Open Website
Wait for Page to Load
Find Username Box
Type Username
Find Password Box
Type Password
Click Login Button
Wait for Dashboard to Open
Click Product
Add Item to Cart
Open Cart
Remove Item
Close Browser
End Test
```
