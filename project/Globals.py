def initialize():
    global id
    id = None
    global listbox
    listbox = None
    global id_list
    id_list = []
    global name_list
    name_list = []

    # 儲存搜尋結果的dict name ->id
    global channels_dict
    channels_dict = {}
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
