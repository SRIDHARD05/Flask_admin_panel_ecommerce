from bs4 import BeautifulSoup
from collections import Counter
import json
import re

with open('response_content.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

with open("products_data.json", "r", encoding="utf-8") as json_file:
    product_data = json.load(json_file)

def process_html_content(html_content):
    def clean_text(text):
        text = re.sub(r'\s{4,}', '   ', text)
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        return text.strip()

    def format_title(title):
        return re.sub(r'\s+', ' ', title)  

    soup = BeautifulSoup(html_content, 'html.parser')
    class_combinations = []
    id_combinations = []
    class_dict = {}

    for element in soup.find_all(True):
        if element.get('class'):
            class_combination = ' '.join(element.get('class'))
            class_combinations.append(class_combination)
        if element.get('id'):
            id_combinations.append(element.get('id'))

    class_combination_counter = Counter(class_combinations)
    id_combination_counter = Counter(id_combinations)

    repeated_class_combinations = {combination: count for combination, count in class_combination_counter.items() if count > 1}
    unique_repeated_class_combinations = {k: v for k, v in repeated_class_combinations.items()}
    filtered_classes_with_product = {k: v for k, v in unique_repeated_class_combinations.items() if 'product' in k}
    max_classes_with_product = Counter(filtered_classes_with_product).most_common(2)

    if not max_classes_with_product:
        return {"error": "No class combinations with 'product' found."}

    parent_class = max_classes_with_product[0][0]
    parent_elements = soup.find_all(class_=parent_class)

    for idx, element in enumerate(parent_elements):
        title_element = element.find('h2')
        href = element.find('a', href=True)
        all_text = element.get_text(separator="|||")

        assets = [img['src'] for img in element.find_all('img', src=True)]
        

        text_elements = [clean_text(t) for t in all_text.split("|||") if t.strip()]

        max_length_text = max(text_elements, key=len) if text_elements else ""
        title = clean_text(title_element.get_text()) if title_element else ""
        if title != max_length_text:
            title = max_length_text

        class_dict[idx] = {
            "title": title,
            "href": href['href'] if href else "",
            "assets": assets
        }
    return class_dict



result = process_html_content(html_content)
json_result = json.dumps(result, indent=4)
with open("parent_classes.json", "w") as json_file:
    json_file.write(json_result)
print("JSON data has been saved to 'parent_classes.json'.")




['//www.beeinspiredclothing.com/cdn/shop/files/luca_update9_700x.png?v=1728460486', '//www.beeinspiredclothing.com/cdn/shop/files/luca_update10_700x.png?v=1728460486', '//www.beeinspiredclothing.com/cdn/shop/files/luca_update11_700x.png?v=1728460486', '//www.beeinspiredclothing.com/cdn/shop/files/luca_update12_700x.png?v=1728460486', '//www.beeinspiredclothing.com/cdn/shop/files/LUCA-UPDATE4_700x.png?v=1722520584', '//www.beeinspiredclothing.com/cdn/shop/files/LUCA-UPDATE3_700x.png?v=1722520585', '//www.beeinspiredclothing.com/cdn/shop/t/464/assets/close.svg?v=43906234831021821841734599800', '//www.beeinspiredclothing.com/cdn/shop/files/luca_update9_150x.png?v=1728460486', '//www.beeinspiredclothing.com/cdn/shop/t/464/assets/plus.svg?v=165110017422457486771734599800']