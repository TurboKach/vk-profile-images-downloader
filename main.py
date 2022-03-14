import math

from vk_request import VkRequest

if __name__ == "__main__":
    wall_photos = VkRequest.photos_get_wall_photos()
    wall_photos_cnt = wall_photos.get('response').get('count')
    print("Всего изображений на стене:", wall_photos_cnt)
    limit = 1000
    offset = 0

    # За i циклов перебираем все изображения на стене пользователя
    for i in range(1, math.ceil(wall_photos_cnt / limit) + 1):
        print(i)
        print(limit, offset)
        wall_photos = VkRequest.photos_get_wall_photos(limit=limit, offset=offset)
        with open('wall_photos_17022022.txt', mode='a') as file:
            file.write(str(wall_photos))
            file.write('\n')
        offset += limit
