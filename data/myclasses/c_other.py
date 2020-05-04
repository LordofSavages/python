# other classes

# imports
from Tkinter import Toplevel, Frame, Canvas, Label, Button, Scale, Entry, \
    LEFT, HORIZONTAL, FLAT, RIDGE, SOLID, StringVar, N
from data.myfunctions import GrayScale
from data.myvariables import MyFonts, canvas_relx, canvas_rely, canvas_width, canvas_height, scale_relwidth, \
    scale_relheight, frame_bottom_pad1, frame_bottom_pad2


# Defining Object ToolTip
# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    # showtip method for ToolTip class
    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 30
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = Label(tw, text=self.text)
        label.configure(justify=LEFT)
        label.configure(relief=SOLID, bd=1)
        label.configure(bg=GrayScale(60), fg=GrayScale(220), font=MyFonts['Default'])
        label.pack(ipadx=1)

    # hidetip method for ToolTip class
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


# Creating MyFrame
class MyFrame(Frame):
    relx = 0
    rely = 0
    relwidth = 1
    relheight = 1

    def __init__(self, parent, bgcolor):
        Frame.__init__(self, parent)

        self.configure_(bgcolor)
        self.place_()

    def configure_(self, bgcolor):
        self.configure(bg=bgcolor)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)


# Creating MyFrameWBP1
class MyFrameWBP1(MyFrame):
    relheight = 1 - frame_bottom_pad1

    def __init__(self, parent, bgcolor):
        MyFrame.__init__(self, parent, bgcolor)


# Creating MyFrameWBP2
class MyFrameWBP2(MyFrame):
    relheight = 1 - frame_bottom_pad2

    def __init__(self, parent, bgcolor):
        MyFrame.__init__(self, parent, bgcolor)


# Creating MyInputFrame
class MyInputFrame(MyFrame):
    relwidth = 0.30
    relheight = 0.80

    def __init__(self, parent, bgcolor):
        MyFrame.__init__(self, parent, bgcolor)


# Creating MyOutputFrame
class MyOutputFrame(MyFrame):
    relx = 0.70
    relwidth = 0.30
    relheight = 0.80 / 0.90

    def __init__(self, parent, bgcolor):
        MyFrame.__init__(self, parent, bgcolor)


# Creating MyCanvas
class MyCanvas(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(bg=GrayScale(20))
        self.configure(width=canvas_width, height=canvas_height)
        self.configure(relief=RIDGE, bd=2)

    def place_(self):
        self.place(relx=canvas_relx, rely=canvas_rely)


# Creating MyButton
class MyButton(Button):
    bgcolor = GrayScale(40)
    fgcolor = GrayScale(220)

    # default active colors are the same as idle colors
    abgcolor = bgcolor
    afgcolor = fgcolor

    relwidth = 0.10
    relheight = 0.05

    def __init__(self, parent, text, command, relx, rely):
        self.text = text
        self.command = command
        self.relx = relx
        self.rely = rely

        Button.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(text=self.text, command=self.command)
        self.configure(font=MyFonts['DefaultBold'])
        self.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.configure(activebackground=self.abgcolor, activeforeground=self.afgcolor)
        self.configure(relief=RIDGE, highlightthickness=0, bd=0)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)


# Creating MyImageButton
class MyImageButton(Button):
    relwidth = 0.05 / (16.0 / 9.0)
    relheight = 0.05

    def __init__(self, parent, bgcolor, img, command, relx, rely):
        self.bgcolor = bgcolor
        self.img = img
        self.command = command
        self.relx = relx
        self.rely = rely

        Button.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(image=self.img)
        self.image = self.img
        self.configure(command=self.command)
        self.configure(bg=self.bgcolor, activebackground=self.bgcolor)
        self.configure(relief=RIDGE, highlightthickness=0, bd=0)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)


# Creating MyToggleButton
class MyToggleButton(object):
    def __init__(self, parent, text, relx, rely):
        # assigning parameters to attributes
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        self.relwidth = 0.20
        self.relheight = 0.20 / 2

        self.enabled = False

        self.create_title_label()
        self.create_frames()

    def create_title_label(self):
        self.title_label = MyLabel(self.parent, self.text, self.relx, self.rely - 0.05)
        self.title_label.configure(font=MyFonts['LargeBold'])

    def create_frames(self):
        self.pf = Frame(self.parent)
        self.pf.configure(bg=GrayScale(0))
        self.pf.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.f1 = MyFrame(self.pf, GrayScale(80))
        self.f2 = MyFrame(self.pf, GrayScale(60))

        self.b1 = MyButton(self.f1, 'Disabled', self.func1, 0, 0)
        self.b2 = MyButton(self.f2, 'Enabled', self.func2, 0, 0)

        self.b1.configure(bg=GrayScale(40), activebackground=GrayScale(180))
        self.b2.configure(bg=GrayScale(180), activebackground=GrayScale(40), fg=GrayScale(20))

        self.b1.place(relwidth=1, relheight=1)
        self.b2.place(relwidth=1, relheight=1)

    def func1(self):
        self.f2.tkraise()
        self.enabled = True

    def func2(self):
        self.f1.tkraise()
        self.enabled = False


# Creating MyCycleButton3
class MyCycleButton3(object):
    def __init__(self, parent, options_list, frames_list, relx, rely):
        # assigning parameters to attributes
        self.parent = parent
        self.o_list = options_list
        self.f_list = frames_list
        self.relx = relx
        self.rely = rely

        self.relwidth = 0.10
        self.relheight = 0.05

        # creating frames
        self.create_frames()

    def create_frames(self):
        self.pf = Frame(self.parent)
        self.pf.configure(bg=GrayScale(0))
        self.pf.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

        self.f1 = MyFrame(self.pf, GrayScale(80))
        self.f2 = MyFrame(self.pf, GrayScale(60))
        self.f3 = MyFrame(self.pf, GrayScale(40))

        self.b1 = MyButton(self.f1, self.o_list[0], self.func1, 0, 0)
        self.b2 = MyButton(self.f2, self.o_list[1], self.func2, 0, 0)
        self.b3 = MyButton(self.f3, self.o_list[2], self.func3, 0, 0)

        self.b1.configure(bg=GrayScale(80), activebackground=GrayScale(80))
        self.b2.configure(bg=GrayScale(60), activebackground=GrayScale(60))
        self.b3.configure(bg=GrayScale(40), activebackground=GrayScale(40))

        self.b1.place(relwidth=1, relheight=1)
        self.b2.place(relwidth=1, relheight=1)
        self.b3.place(relwidth=1, relheight=1)

        self.f1.tkraise()

    def func1(self):
        self.f2.tkraise()
        self.f_list[2].tkraise()
        self.f_list[0].tkraise()

    def func2(self):
        self.f3.tkraise()
        self.f_list[3].tkraise()
        self.f_list[0].tkraise()

    def func3(self):
        self.f1.tkraise()
        self.f_list[1].tkraise()
        self.f_list[0].tkraise()


# Creating MyScale
class MyScale(Scale):
    bgcolor = GrayScale(20)
    fgcolor = GrayScale(220)

    lowrange = 1.0
    highrange = 100.0
    resolution = 0.1

    s_relwidth = scale_relwidth
    s_relheight = scale_relheight

    def __init__(self, parent, text, relx, rely):
        # making parameters into attributes
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        # creating Tkinter variables
        self.l_val = StringVar()

        Scale.__init__(self, self.parent)

        self.scale_configure_()
        self.scale_place_()
        self.label_create_()

    def scale_configure_(self):
        self.configure(command=self.update)
        self.configure(from_=self.lowrange, to=self.highrange)
        self.configure(orient=HORIZONTAL, showvalue=0, resolution=self.resolution)
        self.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.configure(relief=RIDGE, highlightthickness=0, bd=0)

    def scale_place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.s_relwidth, relheight=self.s_relheight)

    def label_create_(self):
        self.label = Label(self.parent)

        self.label_configure_()
        self.label_place_()

    def label_configure_(self):
        self.label.configure(textvariable=self.l_val)
        self.label.configure(font=MyFonts['Default'])
        self.label.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.label.configure(relief=FLAT)
        self.label.configure(padx=2, pady=2)

    def label_place_(self):
        label_rely = self.rely - 0.050
        self.label.place(relx=self.relx, rely=label_rely)

    def update(self, *args):
        self.l_val.set(' ' + self.text + ' = ' + str(Scale.get(self)) + ' ')


# Creating MyInputScale
class MyInputScale(MyScale):
    s_relwidth = scale_relwidth * 1.35 / 0.3
    s_relheight = scale_relheight * 1.35 / 0.8

    def __init__(self, parent, text, relx, rely):
        MyScale.__init__(self, parent, text, relx, rely)


class MyLabel(Label):
    bgcolor = GrayScale(20)
    fgcolor = GrayScale(220)

    def __init__(self, parent, text, relx, rely):
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        Label.__init__(self, self.parent)

        self.configure_()
        self.place_()

    def configure_(self):
        self.configure(text=self.text)
        self.configure(font=MyFonts['Default'])
        self.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.configure(relief=FLAT, anchor=N)
        self.configure(padx=2, pady=2)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely)


# Creating MyEntry
class MyEntry(Entry):
    charwidth = 20
    bgcolor = GrayScale(20)
    fgcolor = GrayScale(220)

    def __init__(self, parent, text, relx, rely):
        self.parent = parent
        self.text = text
        self.relx = relx
        self.rely = rely

        Entry.__init__(self, self.parent)

        self.entry_configure_()
        self.entry_place_()

        self.label_rely = self.rely - 0.045
        self.label_create_()

    def entry_configure_(self):
        self.configure(width=self.charwidth)
        self.configure(bg=self.bgcolor, fg=self.fgcolor)
        self.configure(relief=RIDGE, highlightthickness=2, bd=0)

    def entry_place_(self):
        self.place(relx=self.relx, rely=self.rely)

    def label_create_(self):
        self.label = MyLabel(self.parent, self.text, self.relx, self.label_rely)


# Creating MyOutputEntry
class MyOutputEntry(MyEntry):
    def __init__(self, parent, text, relx, rely):
        MyEntry.__init__(self, parent, text, relx, rely)
        self.label_rely = rely - 0.050
