import tkinter as tk


from pathlib import Path
import yaml
import json




class Window(object):
    def __init__(self):
        self.window = None
        self.structured_data=""
        self.lblList=[]
        self.txtList=[]
        self.buttonSave=None
        self.buttonQuit=None
        self.listForJson=[]


        self.init()


    def show(self):
        self.create_window()
        self.userInterface()
        self.window.mainloop()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Python Homework")
        self.window.geometry('500x400')

    def init(self):
        document_yaml = Path("fields.yaml").read_text()
        self.structured_data = yaml.load(document_yaml, Loader=yaml.FullLoader)

    def userInterface(self):
        self.buttonQuit = tk.Button(self.window, text="QUIT", fg="red", command=self.__quit_handler)
        self.buttonQuit.grid(column=220, row=230)

        self.buttonSave = tk.Button(self.window, text="SAVE", fg="blue", command=self.__save_handler)
        self.buttonSave.grid(column=100, row=230)



        i=1
        for field in self.structured_data["fields"]:
            lbl = tk.Label(self.window, text=field["label"]+"  : ")
            lbl.grid(column=0, row=i*30)

            txt = tk.Entry(self.window, textvariable=field["field_name"], width=20)
            txt.grid(column=100, row=i*30)
            self.txtList.append([txt,field["field_name"]])

            i=i+1

            self.lblList.append(lbl)

    def __quit_handler(self):

        dictionaryEnd={"result":self.listForJson}

       # compact_json = json.dumps(dictionaryEnd, separators=(',', ':'))
       # pretty_json = json.dumps(dictionaryEnd, sort_keys=True, indent=4)


        with open('result.json', 'w') as file:
            json.dump(dictionaryEnd, file)
        print("JSON file created!")
        self.window.destroy()

    def __save_handler(self):
        dictForOneKeyValue = {}
        for value in self.txtList:
            dictForOneKeyValue[value[1]]=value[0].get()
            value[0].delete(0,len(value[0].get()))
        self.listForJson.append(dictForOneKeyValue)









my_window = Window()
my_window.show()

