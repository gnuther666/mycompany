
class PageQuery:
    def __init__(self, request):
        self.page_num = request.GET.get('page_num', 1)
        self.page_size = request.GET.get('page_size', 10)
        self.type = request.GET.get('type', None)
        self.page_num = self.check_input_is_int(self.page_num, 1)
        self.page_size = self.check_input_is_int(self.page_size, 10)
        self.type = self.check_input_is_int(self.type, None)
        self.field_filter_list = list()


    def get_data(self, data_list):
        all_page = len(data_list)/self.page_size
        all_page = all_page if int(all_page) == all_page else int(all_page) + 1
        use_data = list()
        if all_page <= self.page_num:
            start_index = (self.page_num - 1) * self.page_size
            use_data =  data_list[start_index:start_index + self.page_size]
        if len(self.field_filter_list) != 0:
            tmp_data = list()
            for one_data in use_data:
                tmp_dict = dict()
                for one_id in self.field_filter_list:
                    tmp_dict[one_id] = one_data.get(one_id, None)
                tmp_data.append(tmp_dict)
            use_data = tmp_data
        return {'page_count': all_page, 'data': use_data}

    def check_input_is_int(self, check_num, default_num):
        if isinstance(check_num, str):
            if check_num.isdigit():
                return int(check_num)
            else:
                return default_num
        elif isinstance(check_num, int):
            return check_num
        else:
            return default_num

    def set_field_filter(self, field_filter_list):
        self.field_filter_list = field_filter_list
