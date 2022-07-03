import _tkinter
import threading
import time
from tkinter.ttk import *
from tkinter import Tk, Toplevel, IntVar, DoubleVar, StringVar, BooleanVar, PhotoImage
from tkinter.colorchooser import askcolor
from pynput.keyboard import GlobalHotKeys


def Mouse(): # M=Mouse
    main_win = Tk()
    main_win.title('Mouse')
    ICON_data = """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"""
    icon = PhotoImage(data=ICON_data)
    main_win.call('wm', 'iconphoto', main_win._w, icon)

    screen_w = main_win.winfo_screenwidth()
    screen_h = main_win.winfo_screenheight()
    main_win.geometry('%sx%s+%s+%s' % (int(screen_w // 6), int(screen_h // 3.7), int(screen_w // 2.4), int(screen_h // 3.4)))

    Child_All_Frame = Frame(main_win)

    ToolBar_Frame = Frame(Child_All_Frame)
    ToolBar_Frame.pack(side='top', fill='x')
    Restore_size = Label(ToolBar_Frame, text='\u26F6', font=("' 15"), foreground='#2b2b2b', cursor='hand2')
    Restore_size.pack(side='right', anchor='e', padx=10)
    Restore_size.bind('<Button-1>', lambda a:main_win.geometry('%sx%s+%s+%s' % (int(screen_w // 1.2), int(screen_h // 1.5), int(screen_w // 12), screen_h // 6)))
    Back_btn_from_child = Label(ToolBar_Frame, text='🔙', font=("' 20"), foreground='#2b2b2b', cursor='hand2')
    Back_btn_from_child.pack(side='left', anchor='e', padx=10)
    def Child_GoBack():
        Main_Mouse_Frame.pack(fill='both', expand=True)
        main_win.geometry('%sx%s+%s+%s' % (int(screen_w // 6), int(screen_h // 3.7), int(screen_w // 2.4), int(screen_h // 3.4)))
        Child_All_Frame.pack_forget()
        child.destroy()
    Back_btn_from_child.bind('<Button-1>', lambda a:Child_GoBack())
    Separator(Child_All_Frame, orient='horizontal').pack(fill='x', side='top')


    tool_name = Label(ToolBar_Frame, text='Mouse Child', font=("Arial 20"))
    tool_name.pack(side='top')
    mouse_position = Label(ToolBar_Frame, text='X: ?, Y: ?', font=("Arial 10"))
    mouse_position.pack()

    Right_frame = Frame(Child_All_Frame)
    Right_frame.pack(side='right', expand=True, fill='both', pady=10)

    controller_frame = LabelFrame(Right_frame, text='Control panel')
    controller_frame.pack(side='right', expand=True, fill='both')

    columns = ('#', 'Type', 'Content', 'Justify', 'Foreground', 'Background', 'X size', 'Y size', 'X margin', 'Y margin')
    Widgets_table = Treeview(controller_frame, columns=columns, show='headings', selectmode='browse')
    Widgets_table.pack(fill='both', expand=True, pady=3, padx=3)

    def Add_table_headers():
        for c in columns:
            Widgets_table.heading(c, text=c, anchor='center')
        Widgets_table.column('#', width=2, anchor='center')
        Widgets_table.column('Type', width=9, anchor='center')
        Widgets_table.column('Content', width=12, anchor='center')
        Widgets_table.column('Justify', width=12, anchor='center')
        Widgets_table.column('Foreground', width=12, anchor='center')
        Widgets_table.column('Background', width=12, anchor='center')
        Widgets_table.column('X size', width=7, anchor='center')
        Widgets_table.column('Y size', width=7, anchor='center')
        Widgets_table.column('X margin', width=7, anchor='center')
        Widgets_table.column('Y margin', width=7, anchor='center')
    Add_table_headers()
    def Insert_widget_in_table(data:tuple or list):
        Widgets_table.insert('', index='end', values=data)

    Text_Frame = LabelFrame(controller_frame, text='Text')
    Text_Frame.pack(fill='both', expand=True)
    ##
    y_text_marginVar = IntVar(value=0)
    y_text_marginFrame = Frame(Text_Frame)
    y_text_marginFrame.pack(expand=True, fill='x')
    Label(y_text_marginFrame, text='Margin Y:').pack(side='left', padx=5)
    y_text_margin = Scale(y_text_marginFrame, cursor='hand2', value=0, variable=y_text_marginVar, state='disabled')

    All_Widgets = []

    def Change_text_Y_margin():
        try:
            y = y_text_marginVar.get()
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            All_Widgets[current_widget].place(y=y)
            selected = Widgets_table.selection()[0]
            vals = Widgets_table.item(Widgets_table.selection()[0])['values']
            Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7], vals[8], y))
            y_text_margin_lbl.config(text=y)
        except IndexError:
            pass
    y_text_margin.bind('<B1-Motion>', lambda a:Change_text_Y_margin())
    y_text_margin.pack(expand=True, fill='x', side='left')
    y_text_margin_lbl = Label(y_text_marginFrame, width=5, text=y_text_marginVar.get())
    y_text_margin_lbl.pack(side='right', padx=5)
    ##
    x_text_marginVar = IntVar(value=0)
    x_text_marginFrame = Frame(Text_Frame)
    x_text_marginFrame.pack(expand=True, fill='x')
    Label(x_text_marginFrame, text='Margin X:').pack(side='left', padx=5)
    x_text_margin = Scale(x_text_marginFrame, cursor='hand2', value=0, variable=x_text_marginVar, state='disabled')
    def Change_text_X_margin():
        try:
            x = x_text_marginVar.get()
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            All_Widgets[current_widget].place(x=x)
            selected = Widgets_table.selection()[0]
            vals = Widgets_table.item(Widgets_table.selection()[0])['values']
            Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7], x, vals[9]))
            x_text_margin_lbl.config(text=x)
        except IndexError:
            pass
    x_text_margin.bind('<B1-Motion>', lambda a: Change_text_X_margin())
    x_text_margin.pack(expand=True, fill='x', side='left')
    x_text_margin_lbl = Label(x_text_marginFrame, width=5, text=x_text_marginVar.get())
    x_text_margin_lbl.pack(side='right', padx=5)
    ##
    y_text_sizeVar = IntVar(value=0)
    y_text_sizeFrame = Frame(Text_Frame)
    y_text_sizeFrame.pack(expand=True, fill='x')
    Label(y_text_sizeFrame, text='Size Y:').pack(side='left', padx=5)
    y_text_size = Scale(y_text_sizeFrame, cursor='hand2', value=0, from_=1, to=25, variable=y_text_sizeVar, state='disabled')

    def Change_text_Y_size():
        try:
            y = y_text_sizeVar.get()
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            All_Widgets[current_widget].place(height=y)
            selected = Widgets_table.selection()[0]
            vals = Widgets_table.item(Widgets_table.selection()[0])['values']
            Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], y, vals[8], vals[9]))
            y_text_size_lbl.config(text=y)
        except IndexError:
            pass
    y_text_size.bind('<B1-Motion>', lambda a: Change_text_Y_size())
    y_text_size.pack(expand=True, fill='x', side='left')
    y_text_size_lbl = Label(y_text_sizeFrame, width=5, text=y_text_sizeVar.get())
    y_text_size_lbl.pack(side='right', padx=5)
    ##
    x_text_sizeVar = IntVar(value=0)
    x_text_sizeFrame = Frame(Text_Frame)
    x_text_sizeFrame.pack(expand=True, fill='x')
    Label(x_text_sizeFrame, text='Size X:').pack(side='left', padx=5)
    x_text_size = Scale(x_text_sizeFrame, cursor='hand2', value=0, from_=1, to=25, variable=x_text_sizeVar, state='disabled')

    def Change_text_X_size():
        try:
            x = x_text_sizeVar.get()
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            All_Widgets[current_widget].config(width=x)
            selected = Widgets_table.selection()[0]
            vals = Widgets_table.item(Widgets_table.selection()[0])['values']
            Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], x, vals[7], vals[8], vals[9]))
            x_text_size_lbl.config(text=x)
        except IndexError:
            pass
    x_text_size.bind('<B1-Motion>', lambda a: Change_text_X_size())
    x_text_size.pack(expand=True, fill='x', side='left')
    x_text_size_lbl = Label(x_text_sizeFrame, width=5, text=x_text_sizeVar.get())
    x_text_size_lbl.pack(side='right', padx=5)
    ##
    Text_justify_Frame = Frame(Text_Frame)
    Text_justify_Frame.pack(fill='x', side='top')
    Label(Text_justify_Frame, text='Justify:').pack(side='left')
    Text_justifyVar = StringVar(value='left')
    Text_justify = Combobox(Text_justify_Frame, textvariable=Text_justifyVar, values=['left', 'center', 'right'], state='disabled')
    Text_justify.pack(side='right')
    def Change_text_justify():
        try:
            justify = Text_justifyVar.get()
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            anchor = 'w' if justify == 'left' else 'center' if justify == 'center' else 'e' if justify == 'right' else 'w'
            All_Widgets[current_widget].config(justify=justify, anchor=anchor)
            selected = Widgets_table.selection()[0]
            vals = Widgets_table.item(Widgets_table.selection()[0])['values']
            Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], justify, vals[4], vals[5], vals[6], vals[7], vals[8], vals[9]))
        except IndexError:
            pass
    Text_justify.bind('<<ComboboxSelected>>', lambda a:Change_text_justify())
    ##
    Text_background_color_Frame = Frame(Text_Frame)
    Text_background_color_Frame.pack(fill='x', side='top')
    Label(Text_background_color_Frame, text='Background:').pack(side='left')
    Text_background_color = Label(Text_background_color_Frame, background='#ffffff', text='#ffffff', state='disabled')
    Text_background_color.pack(side='right')
    def Change_Background_text_color():
        try:
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            color = askcolor(color=All_Widgets[current_widget]['background'])
            if color != (None, None):
                All_Widgets[current_widget].config(background=color[-1])
                Text_background_color.config(background=color[-1], text=color[-1])
                selected = Widgets_table.selection()[0]
                vals = Widgets_table.item(Widgets_table.selection()[0])['values']
                Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], vals[4], color[-1], vals[6], vals[7], vals[8], vals[9], vals[10]))
        except IndexError:
            pass
    Text_background_color.bind('<Button-1>', lambda a:Change_Background_text_color())
    ##
    Text_Foreground_color_Frame = Frame(Text_Frame)
    Text_Foreground_color_Frame.pack(fill='x', side='top')
    Label(Text_Foreground_color_Frame, text='Foreground:').pack(side='left')
    Text_Foreground_color = Label(Text_Foreground_color_Frame, foreground='#000000', text='#000000', state='disabled')
    Text_Foreground_color.pack(side='right')
    def Change_Foreground_text_color():
        try:
            current_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
            color = askcolor(color=All_Widgets[current_widget]['foreground'])
            if color != (None, None):
                All_Widgets[current_widget].config(foreground=color[-1])
                Text_Foreground_color.config(foreground=color[-1], text=color[-1])
                selected = Widgets_table.selection()[0]
                vals = Widgets_table.item(Widgets_table.selection()[0])['values']
                Widgets_table.item(selected, text=Widgets_table.item(selected)['text'], values=(vals[0], vals[1], vals[2], vals[3], color[-1], vals[5], vals[6], vals[7], vals[8], vals[9], vals[10]))
        except IndexError:
            pass

    Text_Foreground_color.bind('<Button-1>', lambda a: Change_Foreground_text_color())
    ##

    Widget_State = BooleanVar(value=True)
    def Selected_widget():
        if Widgets_table.selection():
            y_text_margin.config(state='normal')
            x_text_margin.config(state='normal')
            y_text_size.config(state='normal')
            x_text_size.config(state='normal')
            Text_justify.config(state='readonly')
            Text_background_color.config(state='normal')
            Text_Foreground_color.config(state='normal')
            ##
            current_widget_y_margin = int(Widgets_table.item(Widgets_table.selection()[0])['values'][9])
            current_widget_x_margin = int(Widgets_table.item(Widgets_table.selection()[0])['values'][8])
            current_widget_y_size = int(Widgets_table.item(Widgets_table.selection()[0])['values'][7])
            current_widget_x_size = int(Widgets_table.item(Widgets_table.selection()[0])['values'][6])
            current_widget_background = str(Widgets_table.item(Widgets_table.selection()[0])['values'][5])
            current_widget_foreground = str(Widgets_table.item(Widgets_table.selection()[0])['values'][4])
            current_widget_justify = str(Widgets_table.item(Widgets_table.selection()[0])['values'][3])
            y_text_sizeVar.set(current_widget_y_size)
            x_text_sizeVar.set(current_widget_x_size)
            y_text_marginVar.set(current_widget_y_margin)
            x_text_marginVar.set(current_widget_x_margin)
            Text_justifyVar.set(current_widget_justify)
            y_text_size.config(value=current_widget_y_size)
            x_text_size.config(value=current_widget_x_size)
            y_text_margin.config(value=current_widget_y_margin)
            x_text_margin.config(value=current_widget_x_margin)
            Text_background_color.config(text=current_widget_background, background=current_widget_background)
            Text_Foreground_color.config(text=current_widget_foreground, foreground=current_widget_foreground)
        else:
            y_text_margin.config(state='disabled')
            x_text_margin.config(state='disabled')
            y_text_size.config(state='disabled')
            x_text_size.config(state='disabled')
            Text_justify.config(state='disabled')
            Text_background_color.config(state='disabled')
            Text_Foreground_color.config(state='disabled')
    Widgets_table.bind('<<TreeviewSelect>>', lambda a:Selected_widget())

    def DoAdd_text():
        data = Add_Text_entry.get()
        new_lbl = Label(child, text=data, background='#ffffff')
        new_lbl.place(x=0, y=0)
        Insert_widget_in_table(
            (
                len(Widgets_table.get_children()) + 1,
                'Text',
                data,
                'left',
                '#000000',
                '#ffffff',
                y_text_sizeVar.get(),
                x_text_sizeVar.get(),
                y_text_marginVar.get(),
                x_text_marginVar.get(),
                'Active' if Widget_State.get() else 'Inactive'
            )
        )
        All_Widgets.append(new_lbl)
        Add_Text_entry.delete(0, 'end')

    def DoDelete_text():
        if Widgets_table.selection():
            if len(All_Widgets) > 0:
                selected_widget = int(Widgets_table.item(Widgets_table.selection()[0])['values'][0]) - 1
                All_Widgets[selected_widget].place_forget()
                del All_Widgets[selected_widget]
            Widgets_table.delete(Widgets_table.selection()[0])
            index = len(Widgets_table.get_children())
            for id in Widgets_table.get_children():
                vals = Widgets_table.item(id)['values']
                Widgets_table.item(id, text=Widgets_table.item(id)['text'], values=(index, vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7], vals[8], vals[9]))
                index += 1
    Delete_text = Button(Text_Frame, text='Delete', width=7, command=lambda: DoDelete_text())
    Delete_text.pack(side='right')
    ##
    Add_text = Button(Text_Frame, text='Add', width=5, command=lambda :DoAdd_text())
    Add_text.pack(side='right')
    ##
    Add_Text_entry = Entry(Text_Frame)
    Add_Text_entry.pack(side='right', fill='x', expand=True)
    ####

    Left_frame = Frame(Child_All_Frame)
    Left_frame.pack(side='left', expand=True, fill='both')



    child_size_frame = LabelFrame(Left_frame, text='Size')
    child_size_frame.pack(ipady=2, ipadx=10, padx=10, pady=10, expand=True, fill='both')
    ##
    child_margin_frame = LabelFrame(Left_frame, text='Margin')
    child_margin_frame.pack(ipady=2, ipadx=10, padx=10, pady=10, expand=True, fill='both')

    child_settings_frame = LabelFrame(Left_frame, text='Settings')
    child_settings_frame.pack(ipady=2, ipadx=10, padx=10, pady=10, expand=True, fill='both')

    child_reset_frame = LabelFrame(Left_frame, text='Reset')
    child_reset_frame.pack(ipady=2, ipadx=10, padx=10, pady=10, expand=True, fill='both')

    ###
    ###
    ###

    y_sizerVar = IntVar(value=25)
    y_sizerFrame = Frame(child_size_frame)
    y_sizerFrame.pack(expand=True, fill='x')
    Label(y_sizerFrame, text='Y:').pack(side='left', padx=5)
    Label(y_sizerFrame, text='Change vertical size of the child (depend on monitor size, default max value %s)' % screen_h).pack(side='bottom', padx=5)
    y_sizer = Scale(y_sizerFrame, cursor='hand2', value=25, variable=y_sizerVar, from_=1, to=main_win.winfo_screenheight())
    def y_sizer_updated():
        y_text_margin_lbl.config(text=y_text_marginVar.get())
        y_text_margin.config(from_=-y_sizerVar.get(), to=y_sizerVar.get())
        y_text_size.config(to=y_sizerVar.get())
    y_sizer.bind('<B1-Motion>', lambda a:y_sizer_updated())
    y_text_margin_lbl.config(text=y_text_marginVar.get())
    y_text_margin.config(from_=-y_sizerVar.get(), to=y_sizerVar.get())
    y_sizer.pack(expand=True, fill='x', side='left')
    y_sizer_lbl = Label(y_sizerFrame, width=5, text=y_sizerVar.get())
    y_sizer_lbl.pack(side='right', padx=5)

    x_sizerFrame = Frame(child_size_frame)
    x_sizerFrame.pack(expand=True, fill='x')
    Label(x_sizerFrame, text='X:').pack(side='left', padx=5)
    Label(x_sizerFrame, text='Change horizontal size of the child (depend on monitor size, default max value %s)' % screen_w).pack(side='bottom', padx=5)
    x_sizerVar = IntVar(value=25)
    x_sizer = Scale(x_sizerFrame, cursor='hand2', value=25, variable=x_sizerVar, from_=1, to=main_win.winfo_screenwidth())
    def x_sizer_updated():
        x_text_margin_lbl.config(text=x_text_marginVar.get())
        x_text_margin.config(from_=-x_sizerVar.get(), to=x_sizerVar.get())
        x_text_size.config(to=x_sizerVar.get())
    x_sizer.bind('<B1-Motion>', lambda a:x_sizer_updated())
    x_sizer.pack(expand=True, fill='x', side='left')
    x_text_margin_lbl.config(text=x_text_marginVar.get())
    x_text_margin.config(from_=-x_sizerVar.get(), to=x_sizerVar.get())
    x_sizer_lbl = Label(x_sizerFrame, width=5, text=x_sizerVar.get())
    x_sizer_lbl.pack(side='right', padx=5)

    y_marginFrame = Frame(child_margin_frame)
    y_marginFrame.pack(expand=True, fill='x')
    Label(y_marginFrame, text='Y:').pack(side='left', padx=5)
    Label(y_marginFrame, text='Change vertical margin of the child near/away from the mouse cursor (depend on monitor size, default max value %s)' % screen_h).pack(side='bottom', padx=5)
    y_marginVar = IntVar(value=10)
    y_margin = Scale(y_marginFrame, cursor='hand2', value=-main_win.winfo_screenheight()//2, variable=y_marginVar, from_=-main_win.winfo_screenheight(), to=main_win.winfo_screenheight())
    y_margin.pack(expand=True, fill='x', side='left')
    y_margin_lbl = Label(y_marginFrame, width=5, text=y_marginVar.get())
    y_margin_lbl.pack(side='right', padx=5)

    x_marginFrame = Frame(child_margin_frame)
    x_marginFrame.pack(expand=True, fill='x')
    Label(x_marginFrame, text='X:').pack(side='left', padx=5)
    Label(x_marginFrame, text='Change horizontal margin of the child near/away from the mouse cursor (depend on monitor size, default max value %s)' % screen_w).pack(side='bottom', padx=5)
    x_marginVar = IntVar(value=10)
    x_margin = Scale(x_marginFrame, cursor='hand2', value=-main_win.winfo_screenwidth()//2, variable=x_marginVar, from_=-main_win.winfo_screenwidth(), to=main_win.winfo_screenwidth())
    x_margin.pack(expand=True, fill='x', side='left')
    x_margin_lbl = Label(x_marginFrame, width=5, text=x_marginVar.get())
    x_margin_lbl.pack(side='right', padx=5)

    AppearanceFrame = Frame(child_settings_frame)
    AppearanceFrame.pack(expand=True, fill='x')

    AlphaFrame = Frame(AppearanceFrame)
    AlphaFrame.pack(pady=5, padx=5, side='top', fill='x')
    Label(AlphaFrame, text='Transparency:').pack(side='left', padx=3)
    AlphaVar = DoubleVar(value=1.000)
    AlphaSpinBox = Spinbox(AlphaFrame, increment=0.001, from_=0.001, to=1.000, textvariable=AlphaVar, justify='center', width=6, state='readonly')
    AlphaSpinBox.pack(side='right')

    ####
    BackgroundFrame = Frame(AppearanceFrame)
    BackgroundFrame.pack(pady=5, padx=5, side='top', fill='x')
    ##
    Label(BackgroundFrame, text='Background color:').pack(side='left', padx=3)
    ##
    BackgroundColorVar = StringVar(value='#ffffff')
    BackgroundColor_lbl = Label(BackgroundFrame, textvariable=BackgroundColorVar, text='#ffffff', width=9, justify='center', foreground='black', background=BackgroundColorVar.get())
    def ChangeBackground_Color():
        color = askcolor(color=BackgroundColorVar.get())
        if color != (None, None):
            BackgroundColorVar.set(value=color[1])
            BackgroundColor_lbl.config(background=BackgroundColorVar.get(), text=color[1])
    BackgroundColor_lbl.bind('<Button-1>', lambda a:ChangeBackground_Color())
    BackgroundColor_lbl.pack(side='right')
    ##
    BorderFrame = Frame(AppearanceFrame)
    BorderFrame.pack(pady=5, padx=5, side='top', fill='x')
    ##
    ChildBorderWidth_Frame = Frame(BorderFrame)
    ChildBorderWidth_Frame.pack(side='top', fill='x', pady=5)
    ##
    Label(ChildBorderWidth_Frame, text='Border width:').pack(side='left', padx=3)
    ##
    ChildBorderWidth_Var = IntVar(value=1)
    ChildBorderWidth_SpinBox = Spinbox(ChildBorderWidth_Frame, increment=1, from_=0, to=999, textvariable=ChildBorderWidth_Var, justify='center', width=3, state='readonly')
    ChildBorderWidth_SpinBox.pack(side='right')
    ##
    ChildColor_Frame = Frame(BorderFrame)
    ChildColor_Frame.pack(side='top', fill='x', pady=5)
    ##
    Label(ChildColor_Frame, text='Border color:').pack(side='left', padx=3)
    ##
    ChildBorderColorVar = StringVar(value='#000000')
    ChildBorderColor_lbl = Label(ChildColor_Frame, textvariable=ChildBorderColorVar, text='#000000', width=9, justify='center', foreground='black', background=ChildBorderColorVar.get())
    def ChangeChildBorder_Color():
        color = askcolor(color=ChildBorderColorVar.get())
        if color != (None, None):
            ChildBorderColorVar.set(value=color[1])
            ChildBorderColor_lbl.config(background=ChildBorderColorVar.get(), text=color[1])
    ChildBorderColor_lbl.bind('<Button-1>', lambda a: ChangeChildBorder_Color())
    ChildBorderColor_lbl.pack(side='right')
    ##
    Checkbuttons_Frame = Frame(AppearanceFrame)
    Checkbuttons_Frame.pack(side='top', fill='x', pady=15)
    isTopMostVar = BooleanVar(value=True)
    isTopMost = Checkbutton(Checkbuttons_Frame, text='Make child on top of all windows?', cursor='hand2', variable=isTopMostVar)
    isTopMost.pack(fill='x', side='top', padx=7)
    ##
    def DoReset():
        y_sizerVar.set(25)
        x_sizerVar.set(25)
        y_marginVar.set(10)
        x_marginVar.set(10)
        AlphaVar.set(1.000)
        UpdateChildVar.set(0.001)
        BackgroundColorVar.set('#ffffff')
        ChildBorderColorVar.set('#000000')
        isTopMostVar.set(True)
        isKeyBinderVar.set(True)
        SafeModeVar.set(False)

        UpdateChildVar.set(0.001)
        ChildBorderWidth_Var.set(1)
    ##
    isKeyBinderVar = BooleanVar(value=True)
    def KeyBinder():
        if isKeyBinderVar.get():
            def Take_top():
                y_marginVar.set(y_marginVar.get() - 1)
            def Take_right():
                x_marginVar.set(x_marginVar.get() + 1)
            def Take_down():
                y_marginVar.set(y_marginVar.get() + 1)
            def Take_left():
                x_marginVar.set(x_marginVar.get() - 1)
            def increase_top():
                y_sizerVar.set(y_sizerVar.get() - 1)
                y_sizer_updated()
            def decrease_top():
                y_sizerVar.set(y_sizerVar.get() + 1)
                y_sizer_updated()
            def increase_right():
                x_sizerVar.set(x_sizerVar.get() + 1)
                x_sizer_updated()
            def decrease_right():
                x_sizerVar.set(x_sizerVar.get() - 1)
                x_sizer_updated()


            with GlobalHotKeys(
                    {
                        '<ctrl>+r': DoReset,
                        '<ctrl>+w': Take_top,
                        '<ctrl>+d': Take_right,
                        '<ctrl>+a': Take_left,
                        '<ctrl>+s': Take_down,

                        '<shift>+w': increase_top,
                        '<shift>+s': decrease_top,
                        '<shift>+d': increase_right,
                        '<shift>+a': decrease_right,
                    }
            ) as listener:
                listener.join()

    threading.Thread(target=KeyBinder).start()
    isKeyBinder = Checkbutton(Checkbuttons_Frame, text='Begin the key listener for bindings', cursor='hand2', variable=isKeyBinderVar)
    isKeyBinder.pack(fill='x', side='top', padx=7)
    ##
    SafeModeVar = BooleanVar(value=False)
    def SetSafeMode():
        if SafeModeVar.get():
            child.bind('<Enter>', lambda a:DoReset())
        else:
            child.unbind('<Enter>')
    SafeMode = Checkbutton(Checkbuttons_Frame, text='Safe mode (on entering child reset)', cursor='hand2', variable=SafeModeVar, command=lambda :SetSafeMode())
    SafeMode.pack(fill='x', side='top', padx=7)
    ####
    update_interval_time_frame = Frame(child_reset_frame)
    update_interval_time_frame.pack(side='top', fill='x')
    Label(update_interval_time_frame, text='Update interval:').pack(side='left')
    Label(update_interval_time_frame, text='Delay time for the child tracking parent (mouse)').pack(side='bottom')
    UpdateChildVar = DoubleVar(value=0.001)
    UpdateChild_SpinBox = Spinbox(update_interval_time_frame, increment=0.001, from_=0.001, to=5.000, textvariable=UpdateChildVar, justify='center', width=5, state='readonly')
    UpdateChild_SpinBox.pack(side='right')
    ResetBtn = Button(child_reset_frame, text='Reset', takefocus=False, cursor='hand2', command=lambda :DoReset())
    ResetBtn.pack(side='bottom')

    def Start_moving():
        while True:
            try:
                child.geometry('%sx%s+%s+%s' % (x_sizerVar.get(), y_sizerVar.get(), (main_win.winfo_pointerx() + x_marginVar.get()), (main_win.winfo_pointery() + y_marginVar.get())))
                child.attributes('-alpha', AlphaVar.get())
                child.attributes('-topmost', isTopMostVar.get())
                #####
                x_sizer_lbl.config(text=x_sizerVar.get())
                y_sizer_lbl.config(text=y_sizerVar.get())
                x_margin_lbl.config(text=x_marginVar.get())
                y_margin_lbl.config(text=y_marginVar.get())

                child.config(background=BackgroundColorVar.get(), highlightcolor=ChildBorderColorVar.get(), highlightbackground=ChildBorderColorVar.get(), highlightthickness=ChildBorderWidth_Var.get())
                mouse_position.config(text='X: %s, Y: %s' % (main_win.winfo_pointerx(), main_win.winfo_pointery()))
                time.sleep(UpdateChildVar.get())
            except _tkinter.TclError:
                continue

    # child.destroy()
    def Go2_Child_Func():
        global child
        child = Toplevel()
        child.overrideredirect(True)
        main_win.geometry('%sx%s+%s+%s' % (int(screen_w // 1.2), int(screen_h // 1.5), int(screen_w // 12), screen_h // 6))
        Main_Mouse_Frame.pack_forget()
        Child_All_Frame.pack(fill='both', expand=True)
        threading.Thread(target=Start_moving).start()
        child.mainloop()

    Main_Mouse_Frame = Frame(main_win)
    Main_Mouse_Frame.pack(fill='both', expand=True)

    Child_icon = PhotoImage(data='iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAAXNSR0IArs4c6QAAAVNJREFUWEftljFOw0AQRV8AIfpcgJSUwFHocoJ04SbQ5Qh0nAQJSkpOQEuRRIkGeaXVasczy5gQIbuy5PWft3/+jj3hiK7JEbEwwmjdaHVmBSwysdb3e1PRKrarqLVqqEAtQuKIOFNeLRr/0xnZVdmmwVwR8UHFojPLC3MGrHuKeXXCmXkElo5dh4E8ArXjXGPzaIWdsWAEIq0JAXleHmFq/TwFNkZ4tTbljno6YM6Ze+ABkBMl91pwU+Eb4LUyHGUsnFsn0iLOg6llJ2nI8/w+r/0GXEdhboGXrogFswVOFCBr09+crkXdjiyY/Nt1BzxbTkQ+/2UgtdmiQZut+qkz1qDzuBj6MfI6U/vV+AAugSvgXWvfoZxJML05PTTMFPj8K2dStsSZmXW6ftuZEabsQPkZGbxNF8BXV9U7Z9K6OfA0ZGYsrfDzlgCHi1kCI4zm0B5uHlEkpA2uygAAAABJRU5ErkJggg==')
    Go2_Child = Button(Main_Mouse_Frame, text='Child', image=Child_icon, compound='right', takefocus=False, cursor='hand2', command=lambda :Go2_Child_Func())
    Go2_Child.pack(ipady=15, fill='x', side='top', padx=15, pady=5)
    Blockers_icon = PhotoImage(data='iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAAXNSR0IArs4c6QAAA9ZJREFUWEetmLerVUsUxn/3iam1sBELE2ZFMT5zAgsVLEQEUcEEIvof2PgfWOoTDAiWhkbBjFlRzFkbK3vBfOU7zDqsu+7M7OP17WqfPSt8s8I3a04XfXveAyMqqh+AkR2Y7nYyXV0dKJjIW2BU+nEC2FjRPQhsT+uvgbEZWQFZClwGBgBfOwFzGlgD/AL6FQD8k9Zzy9+A/sBhYFsSEJCZwH2n0N0ExsLo5V4WdhqBKJUWSa35lEwHHjoFRehiDYyUtaMfbjd6fQFM6CC9j4HJSc78yOYy4JLTnwHcA4o1IyUPVL9PAWsrID4BQzPrR4DN6bvAPXUy04AH5isXGQ/kOTA+AIv+PgLDgAPAnoKsbM4HbsTUePkIxqfmCTCpAqRHW7pU5mwuAq45ILIr+3ra8l7xDLDaLcZU+YhobTDwJRWmr4kYOTl+5j7OA64nP7Lzn9FArIum7jKbHmh83w/sSyCNR0xPEbqSKeqWX3MuQhOjikdk/CSwIWzRp8Xr5oDp22zgbiY18nkU2JT8i4dEA+N8eHPvMTVN8gZ4KqDW9s8c4Lb70GsT0bg4REw7MdOitdR4OyuAC05fEdoBbA02VcCDgDFWdzKiEN1MZ01T0dYiI93II1OARw0dKZuHRIZ6Ke04BqcWGcn+C9xySmJaRaiJ5dsb/L/ALHFdIjzGIyuB85mUZ7vyb8EoWpFH5qa0K/27+gpGY8DPDvKrXVnXxIgsTvOJNvnOgZH8gkR2sUNFJ2qa1gjR15qJNWKpsRowMOcc2/ag/+i7L2AEXl1iZ4scGLP6YhUYjZ41lu8RiD8FI8dxHrEayR2QEUhjZFRoakERUxPPRGaNqcl1ia+xEmDN1DMjiSm0n1MaYqGJzu+4j61RsYFHJK6mUHNEIBrUNUVqamwFoemssV0tT44Ni5hWZ0/TKW9dl5Mrnk2v0qmtK4OEdKpuSe+RR3TW6MBrAqJRQYWdkzsLrEprio5Gz1mlSrcdiTeuutR4HqkQa2tJNpSeOHrYWq+seDA6rHSvsQ6LM2upWEugSs0Q05Od9HzVx9N3oYuQBvDhDWERo2pTue5Rrakrez054cgjfmb1gPW+Lljcneok8onpeSC9IhdrJt70/BR/zN1/ZHwIoCj55ziwM3zzxVriodZ3X0Tx7ht5xApRlzC7KdayJR7RFOf9yJ+lMJsmOYlTvN30TMFH8A0wuqmVMtfgGue0Ecfcte++yaF12ff010UOR+1fCPGIxgTdOPfWNmFtPBDQlaFG8f7fh3Y7FozrqrM+rWkU1bjR+PiayaWkZMDGg9J66Q+iKqDfKOYo4dP8TEAAAAAASUVORK5CYII=')
    Go2_Blockers = Button(Main_Mouse_Frame, text='Blockers', image=Blockers_icon, compound='right', takefocus=False, cursor='', state='disabled')
    Go2_Blockers.pack(ipady=15, fill='x', side='top', padx=15, pady=20)
    Macro_icon = PhotoImage(data='iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAAXNSR0IArs4c6QAAAWlJREFUWEftl8FNBDEMRd8cVoILB9pAcKYFtBXQAD1tA5RABzQAVIKQQCskkFeTlRUlcRyP0AI7l9lRHPv75/tHO3FAz7QAlgfgBpD3OpIvCuYLeAEu5/cFMJxzeOPMgIDROfJvF1FRME/Alar4PLPkApGCo2AOipkVsFU0yPfnEC0RsamCiZ2QXiRf9Jgkx4+DkYLRx2zcDFCdR8GYx9gCo9nQcXfAG3DfQHcLnAGbTFvNKbbAyLruSH6L7Z8D1xXNScwj8DpfE6mGqa0RMHnynKAc/P8Ak0bZsoWkt9K9VRWy95giExXWTEv9Le8pNVmbzn2Dv8ZnEuIT4D14dQgrp8BH65x7mEn7I1dCV52uoEo3takwbb/GjgUmwoa7Zs9oR8a5tDfsM5bJWYC1Cf4dMFbX3vUQM95iVvxiYEamKx+SRcFYdqCZKRU+gtF/Yyy2dute0/Na/aLHZE3G6HqRBI8YRwt37/sGHK5qJDQHhvUAAAAASUVORK5CYII=')
    Go2_Macro = Button(Main_Mouse_Frame, text='Macro',  image=Macro_icon, compound='right', takefocus=False, cursor='', state='disabled')
    Go2_Macro.pack(ipady=15, fill='x', side='top', padx=15, pady=5)



    main_win.mainloop()

if __name__ == '__main__':
    Mouse()