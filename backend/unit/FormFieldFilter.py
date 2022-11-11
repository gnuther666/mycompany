
def FromFieldFilter(data, filter_list: list) :
    '''
    :param data: 输入数据 dict, 或者list[dict1, dict2, ..] 这种格式
    :param filter_list: [field1, field2, field3 ..]
    :return: 对输入数据筛选后data再输出
    '''
    if not (isinstance(data, list) or isinstance(data, dict)):
        return None
    if isinstance(data, list):
        for one_item in data:
            if not isinstance(one_item, dict):
                return None
    if isinstance(data, list) and len(data) == 0:
        return data
    if isinstance(data, dict):
        input_key = data.keys()
    else:
        input_key = data[0].keys()
    del_key = [one_key for one_key in input_key if one_key not in filter_list]
    if isinstance(data, list):
        for one_dict in data:
            for one_del_key in del_key:
                del one_dict[one_del_key]
        return data
    else:
        for one_del_key in del_key:
            del data[one_del_key]
        return data

if __name__ == '__main__':
    ret1 = FromFieldFilter({'a':1, 'b': 2, 'c': 3}, ['a', 'b'])
    print(ret1)
    ret2 = FromFieldFilter([{'a':1, 'b': 2, 'c': 3}, {'a':4, 'b': 5, 'c': 6}], ['a', 'b'])
    print(ret2)