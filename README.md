# GMeetHack
Auto login and end a Google meet  

## Requirements and setup
`python`
```
$ pip install webdriver_manager
```
```
$ pip install selenium
```
## How to run?
1. Fork this repo
2. Clone it in your system
3. Open the path in your terminal
4. In the terminal enter: 
    ```
    $ python action.py
    ```

## Troubleshoot
It may happen by the time we use this code it may not work, here we can try changing the xpath in the code. It looks like -->  ' '  
```
chrome.find_element_by_xpath('//*[@id="identifierId"]')
```

By using the inspect tool we can get the xpath on any element on chrome
<p align="center"> 
    <img src='https://res.cloudinary.com/practicaldev/image/fetch/s--f3GI8Xwk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/cv9yhr3hyhkdofksmcey.gif'>
</p>