# interview-booking-for-yahoo
is a script that notifies you if interview time is available.  

Since most Japanese company recruitment systems do not have a notification function,   
this script can be used to notify you if an appointment is available.

Please note that depending on the OS, the executable_path of webdriver is not understood.
in ubantu you may need：  
```sudo apt install chromedriver``` and  
```executable_path='/usr/lib/chromium-browser/chromedriver'```

in Arch Linux as Manjaro:  
```executable_path='/usr/lib/chromium/chromedriver'```  

Set the number of sleep seconds in the *choose_ticket function,  
I don't recommend setting too short a time, because it's not fair to others and will stress the server.  
And this is not an automatic appointment script, it just emails you the latest time.  

If you have Google Gmail 2-step verification turned on, you will need to set an app password.
