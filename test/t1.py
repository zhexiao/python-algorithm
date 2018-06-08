# coding: utf-8
book_level_dict = {
    "1": [
        {
            "id": "5aecc8a54e3240a8a3900a9042b75f0a",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001",
            "name": "1序章",
            "parent_id": None,
            "title_order": 1
        }
    ],
    "2": [
        {
            "id": "f79197f8bb154fcd8807fd45a603c0ec",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.002",
            "name": "1.1第一节",
            "parent_id": "5aecc8a54e3240a8a3900a9042b75f0a",
            "title_order": 2
        },
        {
            "id": "f839322513a64d789fbc8db5cf7f4d70",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.001",
            "name": "1.1第一节",
            "parent_id": "5aecc8a54e3240a8a3900a9042b75f0a",
            "title_order": 1
        }
    ],
    "3": [
        {
            "id": "1c5b7391b1304aab9435bfc00d766db2",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.002.002",
            "name": "1.1.1 第一小节",
            "parent_id": "f79197f8bb154fcd8807fd45a603c0ec",
            "title_order": 2
        },
        {
            "id": "58dab47d19894dbb88da9d681227371d",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.002.001",
            "name": "1.1.1 第一小节",
            "parent_id": "f79197f8bb154fcd8807fd45a603c0ec",
            "title_order": 1
        },
        {
            "id": "a14334ebf8964222aad35f574019dfbe",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.001.001",
            "name": "1.1.1 第一小节",
            "parent_id": "f839322513a64d789fbc8db5cf7f4d70",
            "title_order": 1
        }
    ],
    "4": [
        {
            "id": "282a199dc58646ab8e0d311e03198675",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.002.001.001",
            "name": "1.1.1 第四级小节",
            "parent_id": "58dab47d19894dbb88da9d681227371d",
            "title_order": 1
        },
        {
            "id": "36d09d00acab44c9a26f9c5560e61672",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.001.001.001",
            "name": "1.1.1 第四级小节",
            "parent_id": "a14334ebf8964222aad35f574019dfbe",
            "title_order": 1
        },
        {
            "id": "7f46e7ec1be9448f9226f33bbfc4048a",
            "create_time": 1528338267074,
            "update_time": 1528338267074,
            "book_id": "e47f32cae3244d24b3cca99065771ec9",
            "level": "001.002.002.001",
            "name": "1.1.1 第四级小节",
            "parent_id": "1c5b7391b1304aab9435bfc00d766db2",
            "title_order": 1
        }
    ]
}


def get_parent_book(level, parent_book, bk_dt):
    level_depth = level.split('.')
    dep = len(level_depth) - 1
    for i in range(dep):
        l_val = ".".join(level_depth[:i + 1])
        if i == 0:
            parent_book = parent_book[l_val]
        else:
            parent_book = parent_book['children'][l_val]
    parent_book['children'][bk_dt['level']] = bk_dt


res = {}
max_level = 4
for i in range(max_level):
    book_list = sorted(
        book_level_dict[str(i + 1)],
        key=lambda x: x['title_order']
    )

    for bk_dt in book_list:
        bk_dt['children'] = {}
        level = bk_dt['level']

        if i == 0:
            res[level] = bk_dt
        else:
            get_parent_book(level, res, bk_dt)

import json

print(json.dumps(res))
