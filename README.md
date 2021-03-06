# Alex's Functions
## https://github.com/agieson/Alex-s-Functions

This repository includes some functions and useful code I've made that might make your life easier!

## notifications.py

This file contains an Email class, which is primarily used for sending an email. In order to send an email using this
class, an instance must first be created. Here's an example:

`email = Email('google.com', 'password')`

Now that we have an email object with the email and password entered, we can send an email to alex@gmail.com with the
following command:

`email.send('alex@gmail.com', 'Have a good day!')`

I have not inluded a way to send multiple emails at the same time because I do not like email spam. If you wish to do
so, please consider using a for loop like this:

```
for address in email_list:
    email.send(address, 'Hi I'm sending spam email out to lots of people :(')
```

## storezip.py

This file contains functions that can read the binary from zipfile (which can be stored somewhere such as a database), 
and convert the binary back to a file, unzip it, and return the location of the contents. 

A use case for code like this would be storing files into an SQL database. Avoiding a file structure with multiple folders
might be an attractive solution that could avoid a headache. Instead, consider using these functions to store the binary
of the files, which can then be converted back when the contents of the zip file are needed. 


