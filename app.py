import json

import scrapper_insta


def insert_into_txt(content):
    with open('instagram_content.txt', 'w') as f:
        json.dump(content, f)


def show_json_content():
    with open('instagram_content.txt') as json_file:
        data = json.load(json_file)
        for p in data['Data']:
            print('id: ' + str(p['id']))
            print('date: ' + p['date'])
            print('likes: ' + str(p['likes']))
            print('description' + p['description'])
            print('')


if __name__ == '__main__':
    scrapper_insta.enter_into_account()
    scrapper_insta.accessing_gallery()
    data_from_instagram = scrapper_insta.scrapping_content()

    insert_into_txt(data_from_instagram)