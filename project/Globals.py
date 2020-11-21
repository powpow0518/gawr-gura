def initialize():
    global id
    id = None
    global listbox
    listbox = None
    global id_list
    id_list = []
    global name_list
    name_list = []

    # 儲存搜尋結果的dict id:name
    global channels_dict
    channels_dict = {}

    # 為了把各個index 有其對應的頻道ID, 生成searched_dict[i] 作為區別listbox每個item的用法
    global searched_dict
    searched_dict = {}

    global selected_name
    selected_name = None
    global selected_subs
    selected_subs = None
    global selected_desc
    selected_desc = None

    global gurabox1
    gurabox1 = None
    global gurabox2
    gurabox2 = None
    global guralabel
    guralabel = None

    # 容納數量
    global gurabox2size
    gurabox2size = 8

    global plural_searched_dict
    plural_searched_dict = {}

    global plural_left_list_dict
    plural_left_list_dict = {}

    global plural_searched_list
    plural_searched_list = []

    global plural_searcd_code

    plural_searcd_code = 0
