import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

# Load api-key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Exception for invalid url
class InvalidGoodreadsURL(Exception):
    pass

class GoodreadsAPIClient(object):
    def __init__(self, url):
        self.url = url 

    def get_book_details(self, url):
        try:
            resp = ET.fromstring(requests.get(url).content)

            # Check if the xml response is valid
            if ET.iselement(resp):

                # DictSchema-> {  
                #                   title string
                #                   average_rating : float
                #                   ratings_count : int
                #                   num_pages : int
                #                   image_url : string
                #                   publication_year : string
                #                   authors : string
                #               }

                bookDict = {}
                for element in resp[1]:
                    if element.tag == "title":
                        bookDict["title"] = str(element.text)

                    if element.tag == "average_rating":
                        bookDict["average_rating"] = float(element.text)

                    if element.tag == "ratings_count":
                        bookDict["ratings_count"] = int(element.text)
                        
                    if element.tag == "num_pages":
                        bookDict["num_pages"] = int(element.text)
            
                    if element.tag == "image_url":
                        bookDict["image_url"] = str(element.text)

                    if element.tag == "publication_year":
                        bookDict["publication_year"] = int(element.text)

                    if element.tag == "authors":
                        author_list = []
                        for author in element:
                            for child in author:
                                if child.tag == "name":
                                    author_list.append(child.text)
                                    bookDict["authors"]= (",").join(author_list)
            else:
                # Return empty string if the xml response is invalid
                return {}

        # Exception for invalid url       
        except requests.exceptions.RequestException:
            raise InvalidGoodreadsURL
        
        # Exception for xml ParseError
        except ET.ParseError:
            raise InvalidGoodreadsURL

        return bookDict

# Prep url to use the api url format
url = input("Please enter the url of the book: ") + ".xml?key="+ api_key

my_book = GoodreadsAPIClient(url)
print(my_book.get_book_details(url))       