#! /usr/bin/env python
#################################################################################
#     File Name           :     mainWindow.py
#     Created By          :     silenzhou
#     Creation Date       :     [2017-11-06 14:02]
#     Last Modified       :     [2017-11-10 21:54]
#     Description         :      
#################################################################################
#/*************************************************************************
#
#	> File Name: mainWindow.py
#	> Author: 
#	> Mail: 
#	> Created Time: 一 11/ 6 14:02:16 2017
# ************************************************************************/

import tkinter
from tkinter import *
from Passwordmaker import *
import tkinter.messagebox

passwordmaker = Passwordmaker()

def create_window():
    win_root = Tk()
    win_root.geometry('460x300')
    win_root.title('Password Generator')

    color = '#F5FFFA'
    win_root['background'] = color

    
    #标签
    Label(win_root, text='Configurations', bg=color).grid(column=0, row=0, columnspan=2, pady=5)
    Label(win_root, text='Pattern', bg=color).grid(column=0, row=1, ipadx=20)
    Label(win_root, text='MaxLength', bg=color).grid(column=0, row=7, ipadx=20)
    Label(win_root, text='Amount', bg=color).grid(column=0, row=8, ipadx=20)

    #最大长度设置
    length_value = StringVar()
    length_input = Entry(win_root, width=12, textvariable=length_value, bg=color)
    length_input.grid(column=1, row=7, pady=10, sticky=W)
    
    #生成总量
    amount_value = StringVar()
    amount_input = Entry(win_root, width=12, textvariable=amount_value, bg=color)
    amount_input.grid(column=1, row=8, sticky=W)

    #模式设置
    #menu_button = Menubutton(win_root, text='choose pattern', relief=RAISED)
    #menu_button.grid(column=1, row=1)
    #menu_button.menu = Menu(menu_button, tearoff=False)
    #menu_button['menu'] = menu_button.menu

    chVarKB = IntVar()
    check_kb = Checkbutton(win_root, text='KeyBoard', variable=chVarKB, bg=color)
    check_kb.deselect()
    check_kb.grid(column=1, row=1, sticky=W)
    #menu_button.menu.add_checkbutton(label='KeyBoard', variable=chVarKB)

    chVarW_K = IntVar()
    check_w_k = Checkbutton(win_root, text='(Word or PinYin) + KeyBoard', variable=chVarW_K, bg=color)
    check_w_k.deselect()
    check_w_k.grid(column=1, row=2, sticky=W)

    chVarW_N = IntVar()
    check_w_n = Checkbutton(win_root, text='(Word or PinYin) + (Number or Date)', variable=chVarW_N, bg=color)
    check_w_n.deselect()
    check_w_n.grid(column=1, row=3, sticky=W)
    #menu_button.menu.add_checkbutton(label='Time', variable=chVarTime)

    chVarW_OL = IntVar()
    check_w_OL = Checkbutton(win_root, text='(Word or PinYin) overlap     (less)', variable=chVarW_OL, bg=color)
    check_w_OL.deselect()
    check_w_OL.grid(column=1, row=4, sticky=W)
    #menu_button.menu.add_checkbutton(label='Word', variable=chVarWord)

    chVarN_S = IntVar()
    check_n_s = Checkbutton(win_root, text='(Number or Date) + Symbol', variable=chVarN_S, bg=color)
    check_n_s.deselect()
    check_n_s.grid(column=1, row=5, sticky=W)
    #menu_button.menu.add_checkbutton(label='PinYin', variable=chVarPY)

    chVarW_N_S = IntVar()
    check_w_n_s = Checkbutton(win_root, text='(Word or PinYin) + (Number or Date) + Symbol', variable=chVarW_N_S, bg=color)
    check_w_n_s.deselect()
    check_w_n_s.grid(column=1, row=6, columnspan=2, sticky=W)


    #button点击事件
    def click():
        intKB = chVarKB.get()
        intW_K = chVarW_K.get()
        intW_N = chVarW_N.get()
        intW_OL = chVarW_OL.get()
        intN_S = chVarN_S.get()
        intW_N_S = chVarW_N_S.get()
        stringLength = length_value.get()
        stringAmount = amount_value.get()

        if  not (intKB or intW_K or intW_N or intW_OL or intN_S or intW_N_S):
            tkinter.messagebox.showerror('error', 'Please choose pattern!')
            return

        try:
            intLength = int(stringLength)
        except:
            tkinter.messagebox.showerror('error', 'MaxLength must be integer!')
            return
        
        try:
            intAmount = int(stringAmount)
        except:
            tkinter.messagebox.showerror('error', 'Amount must be integer!')
            return
        
        if intLength < 15:
            tkinter.messagebox.showerror('error', 'MaxLength must larger than 15!')
            return

        if intAmount <= 0 or intAmount > 100000:
            tkinter.messagebox.showerror('error', 'Amount must between 0 - 100000.')
            return

        print(intKB, intW_K, intW_N, intW_OL, intN_S, intW_N_S, stringLength, stringAmount)
        
        result = passwordmaker.generate_result(intKB, intW_K, intW_N, intW_OL, intN_S, intW_N_S, intLength, intAmount)

        tkinter.messagebox.showinfo('info', result)
        return


    button = Button(win_root, text='generate', command=click, bg=color)
    button.grid(column=0, row=9, columnspan=2, ipadx=20, pady=15, sticky=S)
    
    win_root.mainloop()


if __name__ == '__main__':
    create_window()
