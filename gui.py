import customtkinter
import tkinter.filedialog as fd
import os
import sys
import time
import threading
import datetime

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logs/gui.log", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass    

sys.stdout = Logger()

date_stamp = str(datetime.datetime.now()).split('.')[0]
print(f'Started instance: {date_stamp}')

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.resizable(False, False)
root.title('IP Office User Parser')

def task():
    print('Async test')
    root.after(2000, task)

def open_file_dialog_event():
    filetypes = (
        ('XML files', '*.xml'),
        ('All files', '*.*')
)
    filename = fd.askopenfilename(
        title='Upload users.xml file from IP Office Web Manager.',
        initialdir='./',
        filetypes=filetypes
)
    return filename

def enableTextSearch():
    combobox_1.forget()
    close_button.pack(pady=12, padx=10)
    text_1.pack(pady=12, padx=10)
    text_1.insert("0.0", "")
    txtbox = text_1.get("1.0", 'end-1c')
    txt_string = str(txtbox).replace("[", "").replace("]", "").replace("'", "").replace(".,", ".").replace('",', '"')
    return txt_string

def submit():
    textbox_tag = text_1.get("1.0", 'end-1c')
    combobox_tag = combobox_1.get()
    print(f'textbox_tag: {textbox_tag} | combobox_tag: {combobox_tag}')
    argument = str(open_file_dialog_event())
    if argument == "()":
        print('Invalid file 1: ', argument)
    elif argument  == "":
        print('Invalid file 2: ', argument)
    else:
        if textbox_tag == "":
            print('Combobox!')
            process_closed.forget()
            print(f'Scanning {argument}')
            cmbbox = combobox_1.get()
            my_string = str(cmbbox).replace("[", "").replace("]", "").replace("'", "").replace(".,", ".").replace('",', '"')
            launch_bot_argument = str('python3 scripts/user_reader.py ' + argument + ' --tags ' + my_string)
            print('CLI argument: ' + launch_bot_argument)
            os.system(launch_bot_argument)
        else:
            print('Textbox!')
            process_closed.forget()
            print(f'Scanning {argument}')
            txtbox = textbox_tag
            my_string = str(txtbox).replace("[", "").replace("]", "").replace("'", "").replace(".,", ".").replace('",', '"')
            launch_bot_argument = str('python3 scripts/user_reader.py ' + argument + ' --tags ' + my_string)
            print('CLI argument: ' + launch_bot_argument)
            os.system(launch_bot_argument)

def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True
    progressbar.pack(pady=12, padx=10)
    progressbar.start()
    submit_thread.start()
    root.after(10, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        root.after(10, check_submit_thread)
    else:
        progressbar.stop()
        label_msg.forget()
        close_button.pack(pady=12, padx=10)
        process_closed.pack(pady=12, padx=10)
        print(f"Stopped instance from: {date_stamp}")

def close_window():
    print(f"Closed instance from: {date_stamp}")
    root.quit()
    sys.exit()

def refresh():
    label.pack(pady=12, padx=10)
    button.pack(pady=12, padx=10)
    combobox_1.forget()
    combobox_1.pack(pady=12, padx=10)
    checkbox.forget()
    checkbox.pack()
    progressbar.forget()
    text_1.forget()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill ="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="IP Office User Parser", font=("Roboto", 22))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Pick a file", command=lambda:start_submit_thread(None))
button.pack(pady=12, padx=10)

close_button = customtkinter.CTkButton(master=frame, text="Close", command=close_window)

combobox_1 = customtkinter.CTkComboBox(master=frame, values=["Tags", "BusyOnHeld", "CoverageTime", "CanControlACW", "DoNotDisturb", "ForwardHuntGroupCalls", "ForwardOnBusy", "ForwardUnconditional", "InboundAutoRecord", "Last-Modified", "LoginCode", "ManualVRL", "NoAnswerTime", "OneXClient", "OutboundAutoRecord", "OutgoingCallBar", "Receptionist", "RemoteWorker", "SoftPhone", "SystemName", "VoicemailOn", "WorkingHoursUserRightsGroup"])
combobox_1.pack(pady=12, padx=10)
combobox_1.set("Tags")

checkbox = customtkinter.CTkCheckBox(master=frame, text="Type your Tag (beta)", command=enableTextSearch)
checkbox.pack(pady=12, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame, width=400, height=30)

label_msg = customtkinter.CTkLabel(master=frame, text="Please download users.xml from IPO Web Manager", font=("Arial", 16))
label_msg.pack(pady=12, padx=10)

process_closed = customtkinter.CTkLabel(master=frame, text="Idle", font=("Arial", 16))
process_open = customtkinter.CTkLabel(master=frame, text="Active.", font=("Arial", 16))

reset = customtkinter.CTkButton(master=frame, text="Refresh search", command=refresh)
reset.pack(pady=12, padx=10)

progressbar = customtkinter.CTkProgressBar(master=frame, mode='indeterminate')

root.mainloop()
