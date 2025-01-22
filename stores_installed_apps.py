import re
import json
from bs4 import BeautifulSoup

with open('response_content.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

script_tags = soup.find_all('script', src=re.compile(r'^(?!https://googleads\.g\.doubleclick\.).*'))

data_application_scripts = [script.get('data-application') for script in soup.find_all('script', attrs={'data-application': True}) if script.get('data-application')]

data_render_region = [script.get('data-render-region') for script in soup.find_all('script', attrs={'data-render-region': True}) if script.get('data-render-region')]

app_urls = re.findall(r'app.*\.com', html)

static_urls = list(set(re.findall(r'https://.*\.com', html)))

static_cdn_urls = re.findall(r'https://static.*cdn\.com', html)

extensions_base_url_scripts = [
    "https://extensions.shopifycdn.com/cdn/shopifycloud/web-pixels-manager"
    for script in soup.find_all('script', string=re.compile(r'extensionsBaseUrl'))
    if re.search(r'extensionsBaseUrl\s*=\s*"([^"]+)"', script.string)
]

extensions_scripts = [script.get('src') for script in soup.find_all('script', src=re.compile(r'.*/extensions/')) if script.get('src')]

shopify_urls = re.findall(r'https://shopify\..*\.io', html)

title_tag = soup.find('title')
title = title_tag.string.strip() if title_tag else None

meta_description_tag = soup.find('meta', attrs={'name': 'description'})
description = meta_description_tag['content'] if meta_description_tag else None

shop_url = None
locale = None
currency = None
country = None
theme = None
shop_id = None

shop_script = soup.find_all('script', string=lambda text: text and re.search(
    r'Shopify\.shop|Shopify\.locale|Shopify\.currency|Shopify\.country|Shopify\.theme', text
))

for script in shop_script:
    script_content = script.string

    if 'Shopify.shop' in script_content:
        shop_url_match = re.search(r'Shopify\.shop\s*=\s*["\'](.*?)["\'];', script_content)
        shop_url = shop_url_match.group(1) if shop_url_match else shop_url

    if 'Shopify.locale' in script_content:
        locale_match = re.search(r'Shopify\.locale\s*=\s*["\'](.*?)["\'];', script_content)
        locale = locale_match.group(1) if locale_match else locale

    if 'Shopify.currency' in script_content:
        currency_match = re.search(r'Shopify\.currency\s*=\s*{.*?"active":\s*"(.*?)".*?}', script_content)
        currency = currency_match.group(1) if currency_match else currency

    if 'Shopify.country' in script_content:
        country_match = re.search(r'Shopify\.country\s*=\s*["\'](.*?)["\'];', script_content)
        country = country_match.group(1) if country_match else country

    if 'Shopify.theme' in script_content:
        theme_match = re.search(r'Shopify\.theme\s*=\s*(.*?);', script_content)
        theme = theme_match.group(1) if theme_match else theme

shop_id_tag = soup.find('script', string=lambda text: text and re.search(r'window\.BOOMR\.shop_id|shop_id[=:]\s*(\d+)', text))
if shop_id_tag:
    match = re.search(r'window\.BOOMR\.shop_id\s*=\s*"(\d+)";|shop_id[=:]\s*(\d+)', shop_id_tag.string)
    if match:
        shop_id = match.group(1) or match.group(2)

result_data = {
    "script_srcs": [script.get('src') for script in script_tags if script.get('src')],
    "data_application": data_application_scripts,
    "data_render_region": data_render_region,
    "app_urls": app_urls,
    "static_urls": static_urls,
    "static_cdn_urls": static_cdn_urls,
    "extensions_scripts": extensions_scripts,
    "extensionsBaseUrl": extensions_base_url_scripts,
    "shopify_urls": shopify_urls,  
    "title": title,
    "description": description,
    "shop_url": shop_url,
    "locale": locale,
    "currency": currency,
    "country": country,
    "theme": theme,
    "shop_id": shop_id
}

json_result = json.dumps(result_data, indent=4)

print(json_result)

with open('output_data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_result)

"""
      https://static.*.com
      https://app.



    https:\/\/js.smile.io\/v1\/smile-shopify.js?shop=laurageller.myshopify.com
    app.retention.com
    https://static.rechargecdn.com

    /extensions/ - src="https://cdn.shopify.com/extensions/d08df1b2-86f5-4b17-b502-ee854863414e/rivo-loyalty-rewards-referrals-400/assets/rivo-app-embed.js"

    extensionsBaseUrl

"""