search_type = input("search type: ")
search_content = input("Content: ")   # using 123-234 show the range between 123 and 234
# 13425 45663 fhgfdj a h 123-57645 24-7548
answer_table =[
    {
        'id': 1001,
        'name': "A",
        'inventory': 0,
        'inventory_cap':1050,
        'purchase_permit': 1,
        'sale_permit': 0,
    },
    {
        'id': 2001,
        'name': "B",
        'inventory': 0,
        'inventory_cap': 850,
        'purchase_permit': 1,
        'sale_permit': 0,
    },
    {
        'id': 3001,
        'name': "C",
        'inventory': 0,
        'inventory_cap':325,
        'purchase_permit': 1,
        'sale_permit': 0,
    },
    {
        'id': 4001,
        'name': "D",
        'inventory': 0,
        'inventory_cap': 300,
        'purchase_permit': 0,
        'sale_permit': 0,
    },
    {
        'id': 5001,
        'name': "E",
        'inventory': 0,
        'inventory_cap': 300,
        'purchase_permit': 0,
        'sale_permit': 1,
    },
    {
        'id': 6001,
        'name': "F",
        'inventory': 0,
        'inventory_cap':400,
        'purchase_permit': 0,
        'sale_permit': 1,
    },
    {
        'id': 7001,
        'name': "G",
        'inventory': 0,
        'inventory_cap': 300,
        'purchase_permit': 0,
        'sale_permit': 1,
    },
    {
        'id': 8001,
        'name': "H",
        'inventory': 0,
        'inventory_cap': 150,
        'purchase_permit': 0,
        'sale_permit': 1,
    },
]
result = {}

for i in answer_table:
    if search_type in ["inventory", "inventory_cap"]:
        _range = search_content.split("-")
        if int(_range[0]) < i[search_type] < int(_range[0]):
            result = i
    elif search_type in ["id", "purchase_permit", "sale_permit"]:
        target = int(search_content)
        if target == i[search_type]:
            result = i
        else:
            continue
    elif search_type in ["name"]:
        if search_content == i[search_type]:
            result = i
    else:
        result = "Known search type"

if __name__ == "__main__":
    print(result)