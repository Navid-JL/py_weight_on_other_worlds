import requests
import scrapy as scp
from constants.wikipedia_constants import URL

wikipedia_data = requests.get(URL)

sel = scp.Selector(text=wikipedia_data.text)

print(sel.xpath(
    '//table[@class = "wikitable sortable jquery-tablesorter"]/tbody/tr/td/a/text()').extract())
