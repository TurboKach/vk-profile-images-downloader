import ast
import os
import json

if __name__ == "__main__":
    # with open('wall_photos_17022022.txt', 'r') as f:
    #     full_file = f.read()
    #
    # splitted_file = full_file.splitlines()
    #
    # i = 0
    # for line in splitted_file:
    #     with open(f'processed_files/wall_photos_{i}.json', mode='w') as f:
    #         i += 1
    #         f.write(line)
    #     json_line = json.loads(line)
    #     # первый приоритет на w. если w нет, то берем по алфавиту с наиболее порядковым номером
    # print(f'finished successfully. lines performed: {i}')
    # del i

    # отбор из json'a ссылок на картинки в самом большом размере
    list_buffer = []
    files_list = os.listdir('processed_files')
    files_list.sort()
    for filename in files_list:
        with open(f'processed_files/{filename}', 'r') as f:
            file = f.read()

        json_file = ast.literal_eval(file)
        parsed_file_items = json_file['response']['items']

        i = 0

        for item in parsed_file_items:
            buffer_dict_item = {
                'date': item.get('date'),
                'post_id': item.get('post_id')
            }
            for size in item['sizes']:
                buffer_dict_item['url'] = size.get('url')
                if size['type'] == 'w':
                    break
            i += 1
            list_buffer.append(buffer_dict_item)

        print(i)

    with open(f'cleaned_data/cleaned_images.json', mode='w') as f:
        f.write(str(list_buffer))


