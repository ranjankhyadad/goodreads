import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

# Load api-key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

def get_book_details(url):

    resp = ET.fromstring(requests.get(url).content)

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

    print(bookDict)

    # Can be done using findall() method as well
        # print(resp[1].findall('title')[0].text)
        # print(resp[1].findall('average_rating')[0].text)
        # print(resp[1].findall('ratings_count')[0].text)
        # print(resp[1].findall('num_pages')[0].text)
        # print(resp[1].findall('image_url')[0].text)
        # print(resp[1].findall('publication_year')[0].text)
        # # print(resp[1].findall('authors')[0].text)
        # for author in resp[1].findall('authors')[0]:
        #     print(author[1].text)

# Prep url to use the api url format
url = "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire" + ".xml?key="+ api_key

get_book_details(url)       