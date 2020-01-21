# news-classification



Sample Usage : 


```terminal
Go to news-classification directory 
>> python model.py <FILE_PATH>.txt
#In project test file exists
>> python model.py news.txt
You will see the result.
```


<h3>If you have not Mozilla Firefox browser</h3>
First of all you have to download webdriver for your browser. <br>
For Google Chrome <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">Chrome webdriver</a><br>
For Opera <a href="https://github.com/operasoftware/operachromiumdriver/releases">Opera webdriver</a><br>
For any other browser you can easily find webdriver if you search at google. <br>
After you downloaded your webdriver, move your webdriver's exe file to project directory. Then open news_parser.py file and change start_connection method's driver_path parameter to your exe file name and same methods body you have to change webdriver.Firefox to webdriver.YourBrowser(Chrome,Opera etc.). Now all is set enjoy it !.
