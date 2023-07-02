from twitter_scraper_selenium import scrape_topic

data = scrape_topic(filename="brtAmarelo2", url='https://twitter.com/search?q=%22brt%20amarelo%22&src=typed_query',
                     browser="Chrome", tweets_count=1000, output_format="csv",headless=False)
print(data)
