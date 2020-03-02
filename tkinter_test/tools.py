import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter_test.phone import Phone
from tkinter_test.idcard import idcard_res
import os
# from tkinter_test.tude_addr_tran import tude_tran
p = Phone()
idc = idcard_res()
# t = tude_tran()

class interface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('信息查询')
        self.window.geometry('800x700')
        gif_loc = idc.get_site()
        self.window.iconbitmap(os.path.join(gif_loc,'aaa.ico'))

        # 加载 wellcome image
        canvas = tk.Canvas(self.window, width=800, height=180, bg='white')
        image_file = tk.PhotoImage(file=os.path.join(gif_loc,'pic.gif'))
        image = canvas.create_image(380, 30, anchor='n', image=image_file)
        canvas.pack()

        self.face_design(self.window)
        self.window.mainloop()

    def face_design(self,window):
        # 修改为全局变量
        global var_phone,phone_text_one ,phone_text_two,phone_text_three,phone_text_four
        # 定义手机号输入区域
        tk.Label(window, text='手机号:', font=('Arial', 12)).place(x=20, y=200)
        # 定义手机号输入框entry
        var_phone = tk.StringVar()
        entry_phone = tk.Entry(window, textvariable=var_phone, font=('Arial', 12))
        entry_phone.place(x=80, y=200)

        # 修改为全局变量
        global var_iden, iden_text_one, iden_text_two, iden_text_three, iden_text_four, iden_text_five
        # 定义身份证输入区域
        tk.Label(window, text='身份证:', font=('Arial', 12)).place(x=300, y=200)
        # 定义定义身份证输入框entry
        var_iden = tk.StringVar()
        entry_phone = tk.Entry(window, textvariable=var_iden, font=('Arial', 12))
        entry_phone.place(x=365, y=200)

        # 修改为全局变量
        global var_tude_one,var_tude_two,loc_text
        # 定义身份证输入区域
        tk.Label(window, text='经度:', font=('Arial', 12)).place(x=580, y=190)
        tk.Label(window, text='纬度:', font=('Arial', 12)).place(x=580, y=210)
        # 定义定义经纬度输入框entry
        var_tude_one = tk.StringVar()
        var_tude_two = tk.StringVar()
        entry_tude_one = tk.Entry(window, textvariable=var_tude_one, font=('Arial', 10))
        entry_tude_one.place(x=630, y=190)
        entry_tude_two = tk.Entry(window, textvariable=var_tude_two, font=('Arial', 10))
        entry_tude_two.place(x=630, y=210)


        ## 新增查询按钮
        phone_bt = tk.Button(window, text='手机号查询', width=10,
                             height=1, command=self.phone_query)
        phone_bt.place(x=120, y=250)

        identity_bt = tk.Button(window, text='身份证查询', width=10,
                             height=1, command=self.iden_query)
        identity_bt.place(x=380, y=250)

        loc_bt = tk.Button(window, text='经纬度反查询', width=10,
                                height=1, command=self.loc_query)
        loc_bt.place(x=640, y=250)


        ## 定义结果输出text
        tk.Label(window, text='手机号:', font=('Arial', 10)).place(x=20, y=335)
        phone_text_one = tk.Text(window, height=1, width=15, font=('Arial', 12))
        phone_text_one.place(x=140, y=335)
        tk.Label(window, text='手机运营商:', font=('Arial', 10)).place(x=350, y=335)
        phone_text_two = tk.Text(window, height=1, width=15, font=('Arial', 12))
        phone_text_two.place(x=435, y=335)
        tk.Label(window, text='手机号归属省份:', font=('Arial', 10)).place(x=20, y=390)
        phone_text_three = tk.Text(window, height=1, width=15, font=('Arial', 12))
        phone_text_three.place(x=140, y=385)
        tk.Label(window, text='手机号归属市:', font=('Arial', 10)).place(x=335, y=390)
        phone_text_four = tk.Text(window, height=1, width=15, font=('Arial', 12))
        phone_text_four.place(x=435, y=385)

        tk.Label(window, text='身份证:', font=('Arial', 10)).place(x=20, y=450)
        iden_text_one = tk.Text(window, height=1, width=20, font=('Arial', 12))
        iden_text_one.place(x=140, y=450)
        tk.Label(window, text='身份证具体地址:', font=('Arial', 10)).place(x=360, y=450)
        iden_text_two = tk.Text(window, height=1, width=20, font=('Arial', 12))
        iden_text_two.place(x=485, y=450)
        tk.Label(window, text='登记省份:', font=('Arial', 10)).place(x=20, y=500)
        iden_text_three = tk.Text(window, height=1, width=15, font=('Arial', 12))
        iden_text_three.place(x=110, y=500)
        tk.Label(window, text='性别:', font=('Arial', 10)).place(x=280, y=500)
        iden_text_four = tk.Text(window, height=1, width=15, font=('Arial', 12))
        iden_text_four.place(x=340, y=500)
        tk.Label(window, text='年龄:', font=('Arial', 10)).place(x=500, y=500)
        iden_text_five = tk.Text(window, height=1, width=15, font=('Arial', 12))
        iden_text_five.place(x=550, y=500)

        tk.Label(window, text='具体地址:', font=('Arial', 10)).place(x=20, y=580)
        loc_text = tk.Text(window, height=3, width=50, font=('Arial', 12))
        loc_text.place(x=110, y=580)

    def phone_query(self):
        '''
        :return: 手机查询按钮事件
        '''
        phone_text_one.delete(0.0 ,'end')
        phone_text_two.delete(0.0, 'end')
        phone_text_three.delete(0.0, 'end')
        phone_text_four.delete(0.0, 'end')
        phone = var_phone.get()
        phone_res = p.find(phone)
        phone_num = phone_res['phone']
        phone_type = phone_res['phone_type']
        phone_province = phone_res['province']
        phone_city = phone_res['city']
        phone_text_one.insert('insert', phone_num)
        phone_text_two.insert('insert', phone_type)
        phone_text_three.insert('insert', phone_province)
        phone_text_four.insert('insert', phone_city)

    def iden_query(self):
        '''
            :return: 身份证查询按钮事件
        '''
        iden_text_one.delete(0.0, 'end')
        iden_text_two.delete(0.0, 'end')
        iden_text_three.delete(0.0, 'end')
        iden_text_four.delete(0.0, 'end')
        iden_text_five.delete(0.0, 'end')
        id_no = var_iden.get()
        iden_address = idc.find(id_no, 'address')
        iden_province = idc.find(id_no, 'province')
        iden_sex = idc.find(id_no, 'sex')
        iden_age = idc.find(id_no, 'age')
        sex_dict = {1:'男性',0:'女性'}
        iden_sex_t = sex_dict[iden_sex]

        iden_text_one.insert('insert', id_no)
        iden_text_two.insert('insert', iden_address)
        iden_text_three.insert('insert', iden_province)
        iden_text_four.insert('insert', iden_sex_t)
        iden_text_five.insert('insert', iden_age)

    def loc_query(self):
        loc_text.delete(0.0, 'end')
        log_tude = var_tude_one.get()
        lat_tude = var_tude_two.get()
        # address = t.addr_judge(log_tude, lat_tude)
        loc_text.insert('insert', (log_tude,idc.get_site()))

w = interface()

