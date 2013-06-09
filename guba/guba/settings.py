# Scrapy settings for guba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'guba'

SPIDER_MODULES = ['guba.spiders']
NEWSPIDER_MODULE = 'guba.spiders'
ITEM_PIPELINES = ['guba.pipelines.GubaPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guba (+http://www.yourdomain.com)'
