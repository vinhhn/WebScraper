# WebScraper

  This piece of work comes outside of computer science and is more business oriented. The motivation for 
this project was my interest in stocks, specifically, crypto. Due to the high volatility of some cypto 
I was interested if there was a way I can keep track of any pattern or see when the price would escape a 
particular range.

  At the time I was working a lot with Python and wanted to see if I could somehow fulfull this curiousity
I had for stocks. After some research I found that what I wanted to make was a web scraper. A program that,
as the name implies, scrapes data off a website. There are a few steps in how I wanted this web scraper to 
work for me in this context.
  1. Scrape the cost of a certain stock from a website, preferably from a brokerage I was using 
  2. Return me the cost every so often to see if the value changes
  3. If the value of that stock/coin escapes a set range, alert me
  
  How this Python program actually works is by taking advantage of a Python package. The package that this
program uses is called "Beautiful Soup", this package is used to parse HTML and XML documents. What this
means is that it takes in a website and breaks it down to components that I can use for my program. By
looking at the HTML code provided by Chromes developers extension, I can roughly see how the website is
encoded. Through this I found the snippet of code that holds that value of the stock price. Grabbing this
snippet I call it to a function of the packaged mentioned early and there I have it, the value of the stock
price as an integer variable. With this integer variable I am free to use it however I want to, in this case,
display it back to the user.
