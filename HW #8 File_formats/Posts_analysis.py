import collections
import json
import xml.etree.ElementTree as ET


def read_json(file_path, max_len_word=6, top_words=10):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        print(counter_words.most_common(top_words))


def read_xml(file_path, max_len_word=6, top_words=10):
    with open(file_path, encoding='utf-8') as news_file:
        tree = ET.parse(news_file)
        xml_root = tree.getroot()
        description_words = []
        description_list = xml_root.findall('channel/item/description')
        for item in description_list:
            description = [word for word in item.text.split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        print(counter_words.most_common(top_words))


if __name__ == '__main__':
    read_json('files/newsafr.json')
    read_xml('files/newsafr.xml')
