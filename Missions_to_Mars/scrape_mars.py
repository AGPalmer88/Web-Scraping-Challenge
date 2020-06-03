{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dependencies \n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#MAC USERS EXECUTABLE PATH TO DRIVER\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'app' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-90b5c84feafd>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"/scrape\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mscrape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mbrowser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minit_browser\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mnasa_mars_news_url\u001b[0m \u001b[0;34m=\u001b[0m  \u001b[0;34m'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0mmars_space_images_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'app' is not defined"
     ]
    }
   ],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    nasa_mars_news_url =  'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
    "  #  mars_space_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "  #  mars_facts = 'https://space-facts.com/mars/'\n",
    "  #  mars_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# @NOTE: Replace the path with your actual path to the chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#WINDOWS USERS EXECUTABLE PATH TO DRIVER\n",
    "\n",
    "#executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "#browser = Browser('chrome', **executable_path, headless=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
