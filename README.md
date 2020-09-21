### About

- This script gets the book details from [Goodreads](https://www.goodreads.com/) and displays a dictionary of key,value pairs on terminal

#### API
- The Goodreads API used can be found [here](https://www.goodreads.com/api/index#book.show)
- Get your API key from [here](https://www.goodreads.com/api/keys)
- Save the API keys inside a `.env` file as 
    - API_KEY= YOUR_API_KEY

#### Steps to use

- Install requirements using `pip install -r requirements.txt`. It is recommended that you use a `virtualenv`
- Run `python app.py` on your terminal
- Enter URL of the book whose details need to be fetched
- The details are printed on the terminal