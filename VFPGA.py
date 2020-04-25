import tkinter as tk
from tkinter import filedialog
import bin.fpga as fpga
from pathlib import Path

inputs = []
outputs = []
ops = []
ucf = {}
seg = 0
AN_state=[1,1,1,1]
CLK = 0
clk_id = -1
lock = 0
AN0_id = -1
AN1_id = -1
AN2_id = -1
AN3_id = -1

def AN0_timer():
    global AN0_id
    if AN_state[0]:
        app.AN0.configure(image=digit[0])
    AN0_id = -1

def AN1_timer():
    global AN1_id
    if AN_state[1]:
        app.AN1.configure(image=digit[0])
    AN1_id = -1

def AN2_timer():
    global AN2_id
    if AN_state[2]:
        app.AN2.configure(image=digit[0])
    AN2_id = -1

def AN3_timer():
    global AN3_id
    if AN_state[3]:
        app.AN3.configure(image=digit[0])
    AN3_id = -1

def clock_pulse():
    global clk_id
    global lock
    clk_id = app.after(4, clock_pulse)
    if lock == 1: return
    global CLK
    global ops
    CLK ^= 1
    states = {}
    all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
            "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
            "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
    for elem in inputs:
        states[elem]=all_states[ucf[elem]]
    (out_vals, ops) = fpga.execute(inputs, states, outputs, ops, lock)
    rep_output(out_vals, lock)

def open_file():
    global clk_id
    global lock
    if clk_id != -1: app.after_cancel(clk_id)
    global inputs
    global outputs
    global ops
    global ucf
    global seg
    global AN_state
    global CLK
    global AN0_id
    global AN1_id
    global AN2_id
    global AN3_id
    inputs = []
    outputs = []
    ops = []
    ucf = {}
    seg=0
    AN_state=[1,1,1,1]
    CLK=0
    AN0_id = -1
    AN1_id = -1
    AN2_id = -1
    AN3_id = -1
    (inputs, outputs, ops, ucf) = fpga.interpret_file(filedialog.askopenfilename(initialdir=".", title="Open Schematic", filetypes=[("Schematic files", "*.sch")]), "main")
    states = {}
    all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
            "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
            "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
    for elem in inputs:
        states[elem]=all_states[ucf[elem]]
    (out_vals, ops) = fpga.execute(inputs, states, outputs, ops, lock)
    rep_output(out_vals, lock)
    if any(ucf[elem] == "V10" for elem in inputs):
        clk_id = app.after(4, clock_pulse)
    

def hello():
    print("Hello")

def LED0_control(new_state):
    app.LED0.configure(bg='#FFFF00' if new_state else 'gray')

def LED1_control(new_state):
    app.LED1.configure(bg='#FFFF00' if new_state else 'gray')

def LED2_control(new_state):
    app.LED2.configure(bg='#FFFF00' if new_state else 'gray')

def LED3_control(new_state):
    app.LED3.configure(bg='#FFFF00' if new_state else 'gray')

def LED4_control(new_state):
    app.LED4.configure(bg='#FFFF00' if new_state else 'gray')

def LED5_control(new_state):
    app.LED5.configure(bg='#FFFF00' if new_state else 'gray')

def LED6_control(new_state):
    app.LED6.configure(bg='#FFFF00' if new_state else 'gray')

def LED7_control(new_state):
    app.LED7.configure(bg='#FFFF00' if new_state else 'gray')

def refresh_seg():
    AN0_control(AN_state[0])
    AN1_control(AN_state[1])
    AN2_control(AN_state[2])
    AN3_control(AN_state[3])

def AN0_control(new_state):
    global AN_state
    global AN0_id
    if not new_state:
        app.AN0.configure(image=digit[seg])
        if AN0_id != -1:
            app.after_cancel(AN0_id)
        AN0_id = app.after(32, AN0_timer)
    AN_state[0] = new_state

def AN1_control(new_state):
    global AN_state
    global AN1_id
    if not new_state:
        app.AN1.configure(image=digit[seg])
        if AN1_id != -1:
            app.after_cancel(AN1_id)
        AN1_id = app.after(32, AN1_timer)
    AN_state[1] = new_state

def AN2_control(new_state):
    global AN_state
    global AN2_id
    if not new_state:
        app.AN2.configure(image=digit[seg])
        if AN2_id != -1:
            app.after_cancel(AN2_id)
        AN2_id = app.after(32, AN2_timer)
    AN_state[2] = new_state

def AN3_control(new_state):
    global AN_state
    global AN3_id
    if not new_state:
        app.AN3.configure(image=digit[seg])
        if AN3_id != -1:
            app.after_cancel(AN3_id)
        AN3_id = app.after(32, AN3_timer)
    AN_state[3] = new_state

def A_control(new_state):
    global seg
    if new_state: seg &= ~0x80
    else: seg |= 0x80
    refresh_seg()

def B_control(new_state):
    global seg
    if new_state: seg &= ~0x40
    else: seg |= 0x40
    refresh_seg()

def C_control(new_state):
    global seg
    if new_state: seg &= ~0x20
    else: seg |= 0x20
    refresh_seg()

def D_control(new_state):
    global seg
    if new_state: seg &= ~0x10
    else: seg |= 0x10
    refresh_seg()

def E_control(new_state):
    global seg
    if new_state: seg &= ~0x08
    else: seg |= 0x08
    refresh_seg()

def F_control(new_state):
    global seg
    if new_state: seg &= ~0x04
    else: seg |= 0x04
    refresh_seg()

def G_control(new_state):
    global seg
    if new_state: seg &= ~0x02
    else: seg |= 0x02
    refresh_seg()

def DP_control(new_state):
    global seg
    if new_state: seg &= ~0x01
    else: seg |= 0x01
    refresh_seg()

def rep_output(out_vals, lock):
    for key,value in out_vals.items():
        if ucf[key] == "U16": LED0_control(value)
        elif ucf[key] == "V16": LED1_control(value)
        elif ucf[key] == "U15": LED2_control(value)
        elif ucf[key] == "V15": LED3_control(value)
        elif ucf[key] == "M11": LED4_control(value)
        elif ucf[key] == "N11": LED5_control(value)
        elif ucf[key] == "R11": LED6_control(value)
        elif ucf[key] == "T11": LED7_control(value)
        elif ucf[key] == "N16": AN0_control(value)
        elif ucf[key] == "N15": AN1_control(value)
        elif ucf[key] == "P18": AN2_control(value)
        elif ucf[key] == "P17": AN3_control(value)
        elif ucf[key] == "T17": A_control(value)
        elif ucf[key] == "T18": B_control(value)
        elif ucf[key] == "U17": C_control(value)
        elif ucf[key] == "U18": D_control(value)
        elif ucf[key] == "M14": E_control(value)
        elif ucf[key] == "N14": F_control(value)
        elif ucf[key] == "L14": G_control(value)
        elif ucf[key] == "M13": DP_control(value)
    lock = 0

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create Power and random ports
        self.power = tk.Canvas(self, highlightthickness=0, bg="black", width=25, height= 50)
        self.power.grid(row=0, column= 2)
        self.port1 = tk.Canvas(self, highlightthickness=0, bg="black", width=100, height= 50)
        self.port1.grid(row=0, column= 3, columnspan=2)
        self.port2 = tk.Canvas(self, highlightthickness=0, bg="black", width=100, height= 50)
        self.port2.grid(row=0, column= 6, columnspan=2)
        self.port3 = tk.Canvas(self, highlightthickness=0, bg="black", width=100, height= 50)
        self.port3.grid(row=0, column= 9, columnspan=2)
        self.port4 = tk.Canvas(self, highlightthickness=0, bg="black", width=100, height= 50)
        self.port4.grid(row=0, column= 12, columnspan=2)
        # Create on/off switch
        self.power_switch = tk.Label(self, bg='#094D1C', image=switch_on)
        #self.power_switch.bind('<Button-1>', self.SW0_toggle)
        self.power_switch.grid(row=1, column=1, rowspan=2)
        # Create uUSB, XILINX Tag, RESET and DPI
        self.uUSB = tk.Canvas(self, highlightthickness=0, bg="gray", width=50, height= 25)
        self.uUSB.grid(row=3, column= 0)
        self.xilinx = tk.Label(self, bg="#094D1C", image=xilinx_logo, width=296, height=50, bd=0)
        self.xilinx.grid(row=2, column=4, columnspan=6, rowspan=1)
        self.reset = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        #self.PBup.bind('<Button-1>', self.PBup_pressed)
        #self.PBup.bind('<ButtonRelease-1>', self.PBup_released)
        self.reset.grid(row=3, column=12)
        self.space2 = tk.Canvas(self, highlightthickness=0, bg="#094D1C", width=10, height=250)
        self.space2.grid(row=3, column=14, rowspan=5)
        self.dpi = tk.Canvas(self, highlightthickness=0, bg="gray", width=40, height=250)
        self.dpi.grid(row=3, column=15, rowspan=5)
        # Create ethernet, FPGA
        self.ethernet = tk.Canvas(self, highlightthickness=0, bg="gray", width=100, height=100)
        self.ethernet.grid(row=4, column=0, columnspan=2, rowspan=2)
        self.fpga = tk.Canvas(self, highlightthickness=0, bg="black", width=150, height=150)
        self.fpga.grid(row=4, column=6, columnspan=3, rowspan=3)
        # Create Nexys 3 Tag
        self.nexys = tk.Label(self, bg="#094D1C", image=nexys_logo, width=216, height=30, bd=0)
        self.nexys.grid(row=5, column=9, columnspan=5)
        # Create VGA
        self.vga = tk.Canvas(self, highlightthickness=0, bg="black", width=100, height=150)
        self.vga.grid(row=6, column=0, columnspan=2, rowspan=3)
        # Create 7 seg display
        self.AN3 = tk.Label(self, bg="#094D1C", image=digit[0], width=50, height=100, bd=0)
        self.AN3.grid(row=7, column=10, rowspan=2)
        self.AN2 = tk.Label(self, bg="#094D1C", image=digit[0], width=50, height=100, bd=0)
        self.AN2.grid(row=7, column=11, rowspan=2)
        self.AN1 = tk.Label(self, bg="#094D1C", image=digit[0], width=50, height=100, bd=0)
        self.AN1.grid(row=7, column=12, rowspan=2)
        self.AN0 = tk.Label(self, bg="#094D1C", image=digit[0], width=50, height=100, bd=0)
        self.AN0.grid(row=7, column=13, rowspan=2)
        # Create DIGILENT Tag
        self.digilent = tk.Label(self, bg="#094D1C", image=digilent_logo, width=209, height=50, bd=0)
        self.digilent.grid(row=8, column=3, rowspan=1, columnspan=5)
        # Create USB and blank canvas
        self.USB = tk.Canvas(self, highlightthickness=0, bg="gray", width=100, height= 100)
        self.USB.grid(row=9, column= 0, rowspan=2, columnspan=2)
        self.space = tk.Canvas(self, highlightthickness=0, bg="#094D1C", width=50, height=50)
        self.space.grid(row=9, column= 2, rowspan=1, columnspan=1)
        # Create LEDs and BTNU
        self.LED7 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED7.grid(row=10, column=2)
        self.LED6 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED6.grid(row=10, column=3)
        self.LED5 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED5.grid(row=10, column=4)
        self.LED4 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED4.grid(row=10, column=5)
        self.LED3 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED3.grid(row=10, column=6)
        self.LED2 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED2.grid(row=10, column=7)
        self.LED1 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED1.grid(row=10, column=8)
        self.LED0 = tk.Canvas(self, highlightthickness=0, bg="gray", width=15, height= 15)
        self.LED0.grid(row=10, column=9)
        self.BTNU = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        self.BTNU.bind('<Button-1>', self.BTNU_pressed)
        self.BTNU.bind('<ButtonRelease-1>', self.BTNU_released)
        self.BTNU.grid(row=10, column=12)
        # Create switches, BTNL, BTNS, BTNR
        self.SW0 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW0.bind('<Button-1>', self.SW0_toggle)
        self.SW0.grid(row=11, column=9, rowspan=2)
        self.SW1 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW1.bind('<Button-1>', self.SW1_toggle)
        self.SW1.grid(row=11, column=8, rowspan=2)
        self.SW2 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW2.bind('<Button-1>', self.SW2_toggle)
        self.SW2.grid(row=11, column=7, rowspan=2)
        self.SW3 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW3.bind('<Button-1>', self.SW3_toggle)
        self.SW3.grid(row=11, column=6, rowspan=2)
        self.SW4 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW4.bind('<Button-1>', self.SW4_toggle)
        self.SW4.grid(row=11, column=5, rowspan=2)
        self.SW5 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW5.bind('<Button-1>', self.SW5_toggle)
        self.SW5.grid(row=11, column=4, rowspan=2)
        self.SW6 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW6.bind('<Button-1>', self.SW6_toggle)
        self.SW6.grid(row=11, column=3, rowspan=2)
        self.SW7 = tk.Label(self, bg='#094D1C', image=switch_off)
        self.SW7.bind('<Button-1>', self.SW7_toggle)
        self.SW7.grid(row=11, column=2, rowspan=2)
        self.BTNL = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        self.BTNL.bind('<Button-1>', self.BTNL_pressed)
        self.BTNL.bind('<ButtonRelease-1>', self.BTNL_released)
        self.BTNL.grid(row=11, column=11)
        self.BTNS = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        self.BTNS.bind('<Button-1>', self.BTNS_pressed)
        self.BTNS.bind('<ButtonRelease-1>', self.BTNS_released)
        self.BTNS.grid(row=11, column=12)
        self.BTNR = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        self.BTNR.bind('<Button-1>', self.BTNR_pressed)
        self.BTNR.bind('<ButtonRelease-1>', self.BTNR_released)
        self.BTNR.grid(row=11, column=13)
        # Create BTND
        self.BTND = tk.Label(self, bd=0, bg='#094D1C', image=button_off, width=50, height=50)
        self.BTND.bind('<Button-1>', self.BTND_pressed)
        self.BTND.bind('<ButtonRelease-1>', self.BTND_released)
        self.BTND.grid(row=12, column=12)

    def SW0_toggle(self,args):
        global SW0_state
        global lock
        SW0_state ^= 1
        self.SW0.configure(image= switch_on if SW0_state else switch_off)
        self.SW0.image = switch_on if SW0_state else switch_off
        self.SW0.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)
    
    def SW1_toggle(self,args):
        global SW1_state
        global lock
        SW1_state ^= 1
        self.SW1.configure(image= switch_on if SW1_state else switch_off)
        self.SW1.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW2_toggle(self,args):
        global SW2_state
        global lock
        SW2_state ^= 1
        self.SW2.configure(image= switch_on if SW2_state else switch_off)
        self.SW2.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW3_toggle(self,args):
        global SW3_state
        global lock
        SW3_state ^= 1
        self.SW3.configure(image= switch_on if SW3_state else switch_off)
        self.SW3.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW4_toggle(self,args):
        global SW4_state
        global lock
        SW4_state ^= 1
        self.SW4.configure(image= switch_on if SW4_state else switch_off)
        self.SW4.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW5_toggle(self,args):
        global SW5_state
        global lock
        SW5_state ^= 1
        self.SW5.configure(image= switch_on if SW5_state else switch_off)
        self.SW5.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW6_toggle(self,args):
        global SW6_state
        global lock
        SW6_state ^= 1
        self.SW6.configure(image= switch_on if SW6_state else switch_off)
        self.SW6.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def SW7_toggle(self,args):
        global SW7_state
        global lock
        SW7_state ^= 1
        self.SW7.configure(image= switch_on if SW7_state else switch_off)
        self.SW7.grid()
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNU_pressed(self, args):
        global lock
        self.BTNU.configure(image= button_on)
        self.BTNU.grid()
        BTNU_state=1
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNU_released(self, args):
        global lock
        self.BTNU.configure(image= button_off)
        self.BTNU.grid()
        BTNU_state=0
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNL_pressed(self, args):
        global lock
        self.BTNL.configure(image= button_on)
        self.BTNL.grid()
        BTNL_state=1
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNL_released(self, args):
        global lock
        self.BTNL.configure(image= button_off)
        self.BTNL.grid()
        BTNL_state=0
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNS_pressed(self, args):
        global lock
        self.BTNS.configure(image= button_on)
        self.BTNS.grid()
        BTNS_state=1
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNS_released(self, args):
        global lock
        self.BTNS.configure(image= button_off)
        self.BTNS.grid()
        BTNS_state=0
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNR_pressed(self, args):
        global lock
        self.BTNR.configure(image= button_on)
        self.BTNR.grid()
        BTNR_state=1
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTNR_released(self, args):
        global lock
        self.BTNR.configure(image= button_off)
        self.BTNR.grid()
        BTNR_state=0
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTND_pressed(self, args):
        global lock
        self.BTND.configure(image= button_on)
        self.BTND.grid()
        BTND_state=1
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

    def BTND_released(self, args):
        global lock
        self.BTND.configure(image= button_off)
        self.BTND.grid()
        BTND_state=0
        states = {}
        all_states = {"T10":SW0_state, "T9":SW1_state, "V9":SW2_state, "M8":SW3_state, "N8":SW4_state,\
                "U8":SW5_state, "V8":SW6_state, "T5":SW7_state, "A8":BTNU_state, "C4":BTNL_state, "B8":BTNS_state,\
                "D9":BTNR_state, "C9":BTND_state, "V10":CLK}
        for elem in inputs:
            states[elem]=all_states[ucf[elem]]
        (out_vals, null) = fpga.execute(inputs, states, outputs, ops, lock)
        rep_output(out_vals, lock)

root = tk.Tk()
switch_on = tk.PhotoImage(file = Path('img/switch_on.png')).subsample(2,2)
switch_off = tk.PhotoImage(file = Path('img/switch_off.png')).subsample(2,2)
button_on = tk.PhotoImage(file = Path('img/button_on.png')).zoom(4).subsample(10)
button_off = tk.PhotoImage(file = Path('img/button_off.png')).zoom(4).subsample(10)
digit=[tk.PhotoImage(file = Path(f'img/digit/{a}{b}{c}{d}{e}{f}{g}{p}.png')).zoom(5).subsample(22) for a in ['0','1'] for b in ['0','1'] for c in ['0','1'] for d in ['0','1'] for e in ['0','1'] for f in ['0','1'] for g in ['0','1'] for p in ['0','1']]
#digit=[tk.PhotoImage(file = Path(f'img/digit/{a}0000000.png')).zoom(5).subsample(22) for a in ['0','1']]
digilent_logo = tk.PhotoImage(file = Path('img/digilent.png'))
xilinx_logo = tk.PhotoImage(file = Path('img/xilinx.png')).subsample(2)
nexys_logo = tk.PhotoImage(file = Path('img/nexys.png'))
SW0_state=0
SW1_state=0
SW2_state=0
SW3_state=0
SW4_state=0
SW5_state=0
SW6_state=0
SW7_state=0
BTNU_state=0
BTNL_state=0
BTNS_state=0
BTNR_state=0
BTND_state=0
menubar = tk.Menu(root)
app = Application(master=root)
# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)
app.configure(bg='#094D1C')
root.config(menu=menubar)
app.master.title('DrongoSim')
app.mainloop()
