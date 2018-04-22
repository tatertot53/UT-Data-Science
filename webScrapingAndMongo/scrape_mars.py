
# coding: utf-8
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import tweepy
import json
import numpy as np
import pandas as pd
import pymongo

# # Step 1 - Scraping (NASA Mars News, JPL Mars Space Images - Featured Image, Mars Weather, Mars Facts, Mars Hemisperes)

nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

# jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"



mars_weather_url = "https://twitter.com/marswxreport?lang=en"

mars_facts_url = "https://space-facts.com/mars/"

hemisphere_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

consumer_key = "E7dUfrmzrNI0Ed8GhjP7RXvE1"
consumer_secret = "p2aWWu1fUZ05Dx7VMXM0TLWY6eL1q7O3WzlsieuJPZ8KjxJHlq"
access_token = "355054202-sAmlB68y35O78i9qYplRE95G7eEpLisaewU0p31N"
access_token_secret = "p6P9aH8tVMsIttvN1mzJes5G3Xtr8ep55BDlShnoD8Lla"


def init_browser():
	executable_path = {'executable_path':'chromedriver.exe'}
	return Browser('chrome', **executable_path, headless=False)

def scrape():
	browser = init_browser()
	# Create Mars Data Dictionary to insert to MongoDB
	mars_data = {}

	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)
	db = client.mars_db
	collection = db.mars_db

	# Gather Mars News
	response_nasa = requests.get(nasa_url)

	soup_nasa = bs(response_nasa.text, 'html.parser')

	news_title = soup_nasa.find('div', 'content_title', 'a').a.text
	news_p = soup_nasa.find('div', 'rollover_description_inner').text
				# mars_data["Headline"] = build_report(news_title)
				# print(news_p)
	mars_data["content_title"] = news_title
	mars_data["news_p"] = news_p

	# Use Splinter to Capture JPL Image
	url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	browser.visit(url)

	html = browser.html
	soup_featured = bs(html, "html.parser")

	jpl_url = soup_featured.find('img', class_='thumb')
	featured_image_url = 'https://www.jpl.nasa.gov' + jpl_url['src']


	mars_data["Featured_Image"] = featured_image_url


	# Find Current Weather on Mars
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	target_user = '@MarsWxReport'

	tweet = api.user_timeline(target_user, count=1)[0]

	tweet_text = json.dumps(tweet._json, indent=3)
	tweet = json.loads(tweet_text)
	mars_weather = tweet['text']

	mars_data["Mars_Weather"] = mars_weather


	# Collect Mars Facts
	tables = pd.read_html(mars_facts_url)
			# tables

	df = tables[0]
	df.columns = ['','Values']
			# df.head()
	df.set_index('',inplace=True)
			# df.head()

	html_table = df.to_html(header=None, index=False)
			# html_table

	html_table.replace('\n','')

	mars_data["Mars_Facts"] = html_table

	# Images of Mars Hemispheres

	browser.visit(hemisphere_image_url)
	html = browser.html
	soup_hemispheres = bs(html, 'html.parser')

	hemisphere_img_urls = []

	hemispheres = soup_hemispheres.find_all("div", class_ = "item")

	for result in results:
		link = result.find("h3").text
		title = link.replace("Enhanced", "")
		browser.click_link_by_partial_text(link)
		html = browser.html
		soup_hemispheres=bs(html, "html.parser")
		downloads = soup_hemispheres.find("div", class_="wide_image")
		image_url = 'https://astogeology.usgs.gov/' + downloads['src']
		hemisphere_img_urls.append({"title": title, "img_url": image_url})
		browser.back()

	mars_data["mars_hemispheres"] = hemisphere_img_urls

	return mars_data

