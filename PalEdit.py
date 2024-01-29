import os, webbrowser, json, time, uuid

import SaveConverter

from PalInfo import *

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import ImageTk, Image

global palbox
palbox = []
global unknown
unknown = []
global data
global debug
debug = "false"
global editindex
editindex = -1
global version
version = "0.46"

def toggleDebug():
    global debug
    if debug == "false":
        debug = "true"
        frameDebug.pack(fill=BOTH, expand=False)
    else:
        debug = "false"
        frameDebug.pack_forget()


def isPalSelected():
    global palbox
    if len(palbox) == 0:
        return False
    if len(listdisplay.curselection()) == 0:
        return False
    return True

def getSelectedPalInfo():
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]
    print(f"Get Info: {pal.GetNickname()}")     
    print(f"  - Level: {pal.GetLevel() if pal.GetLevel() > 0 else '?'}")    
    print(f"  - Rank: {pal.GetRank()}")    
    print(f"  - Skill 1:  {skills[0].get()}")
    print(f"  - Skill 2:  {skills[1].get()}")
    print(f"  - Skill 3:  {skills[2].get()}")
    print(f"  - Skill 4:  {skills[3].get()}")
    print(f"  - Melee IV:  {pal.GetAttackMelee()}")
    print(f"  - Range IV:  {pal.GetAttackRanged()}")

def getSelectedPalData():
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]
    print(f"Get Data: {pal.GetNickname()}")    
    print(f"{pal._obj}")  

def setpreset(preset):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i] # seems global palbox is not necessary

    match preset:
        case "worker":
            skills[0].set("工匠精神")
            skills[1].set("认真")
            skills[2].set("稀有")
            skills[3].set("社畜")
        case "runner":
            skills[0].set("神速")
            skills[1].set("传说")
            skills[2].set("运动健将")
            skills[3].set("灵活")
        case "dmg_max":
            skills[0].set("脑筋")
            skills[1].set("传说")
            skills[2].set("凶猛")
            skills[3].set("稀有")
        case "dmg_balanced":
            skills[0].set("脑筋")
            skills[1].set("传说")
            skills[2].set("凶猛")
            skills[3].set("顽强肉体")
        case "dmg_dragon":
            skills[0].set("脑筋")
            skills[1].set("传说")
            skills[2].set("凶猛")
            skills[3].set("神龙")
        case "tank":
            skills[0].set("顽强肉体")
            skills[1].set("传说")
            skills[2].set("受虐狂")
            skills[3].set("坚硬皮肤")
        case _:
            print(f"Preset {preset} not found - nothing changed")
            return

    # exp (if level selected)
    if checkboxLevelVar.get() == 1:
        pal.SetLevel(textboxLevelVar.get())
    # rank (if rank selected)
    if checkboxRankVar.get() == 1:
        changerank(optionMenuRankVar.get())
    # attributes (if attributes selected)
    # TODO: change attributes

    refresh(i)

def makeworker():
    setpreset("worker")
def makerunner():
    setpreset("runner")
def makedmgmax():
    setpreset("dmg_max")
def makedmgbalanced():
    setpreset("dmg_balanced")
def makedmgdragon():
    setpreset("dmg_dragon")
def maketank():
    setpreset("tank")

def changerank(configvalue):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]
    match configvalue:
        case 4:
            pal.SetRank(5)
        case 3:
            pal.SetRank(4)
        case 2:
            pal.SetRank(3)
        case 1:
            pal.SetRank(2)
        case _:
            pal.SetRank(1)
    refresh(i)

def changerankchoice(choice):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]
    changerank(ranksvar.get())

def changeskill(num):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]

    if not skills[num].get() in ["Unknown", "UNKNOWN"]:
        if skills[num].get() in ["None", "NONE"]:
            pal.RemoveSkill(num)
        else:
            pal.SetSkill(num, skills[num].get())

    refresh(i)

def onselect(evt):
    global palbox
    global editindex
    w = evt.widget
    if not isPalSelected():
        return

    if editindex > -1:
        updatestats(editindex)
        
    index = int(w.curselection()[0])
    editindex = index

    pal = palbox[index]
    #palname.config(text=pal.GetName())
    speciesvar.set(pal.GetName())

    g = pal.GetGender()
    palgender.config(text=g, fg=PalGender.MALE.value if g == "Male ♂" else PalGender.FEMALE.value)

    title.config(text=f"{pal.GetNickname()} - Lv. {pal.GetLevel() if pal.GetLevel() > 0 else '?'}")
    portrait.config(image=pal.GetImage())

    ptype.config(text=pal.GetPrimary().GetName(), bg=pal.GetPrimary().GetColour())
    stype.config(text=pal.GetSecondary().GetName(), bg=pal.GetSecondary().GetColour())

    # ⚔🏹
    meleevar.set(pal.GetAttackMelee())
    shotvar.set(pal.GetAttackRanged())
    defvar.set(pal.GetDefence())
    wspvar.set(pal.GetWorkSpeed())

    # rank
    match pal.GetRank():
        case 5:
            ranksvar.set(ranks[4])
        case 4:
            ranksvar.set(ranks[3])
        case 3:
            ranksvar.set(ranks[2])
        case 2:
            ranksvar.set(ranks[1])
        case _:
            ranksvar.set(ranks[0])

    s = pal.GetSkills()[:]
    while len(s) < 4:
        s.append("NONE")

    for i in range(0, 4):
        if not s[i] in [s.name for s in PalSkills]:
            skills[i].set("Unknown")
        else:
            skills[i].set(PalSkills[s[i]].value)
    

def changetext(num):
    if num == -1:
        skilllabel.config(text="将鼠标悬停在技能上即可查看其描述")
        return
    
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i] # seems global palbox is not necessary

    global unknown
    if type(num) == str:
        skilllabel.config(text=pal.GetOwner())
        return


    if skills[num].get() == "Unknown":
        skilllabel.config(text=f"{pal.GetSkills()[num]}{SkillDesc['Unknown']}")
        return
    skilllabel.config(text=SkillDesc[skills[num].get()])

    
def loadfile():
    global palbox
    palbox = []
    skilllabel.config(text="正在加载存档，请耐心等待...")

    file = askopenfilename(filetype=[("All files", "*.sav *.sav.json *.pson"),("Palworld Saves", "*.sav *.sav.json"),("Palworld Box", "*.pson")])
    print(f"正在打开文件: {file}")

    if not file.endswith(".pson") and not file.endswith("Level.sav.json"):
        if file.endswith("Level.sav"):
            answer = messagebox.askquestion("文件格式不正确", "此存档文件尚未被解析, 您想要现在解析吗?")
            if answer == "yes":
                skilllabel.config(text="正在解析存档，请耐心等待...")
                doconvertjson(file)
        else:
            messagebox.showerror("文件格式不正确", "这不是正确的文件, 请选择Level.sav文件.")
        changetext(-1)
        return
    load(file)

def sortPals(e):
    return e.GetName()


def load(file):
    global data
    global palbox
    palbox = []

    f = open(file, "r", encoding="utf8")
    data = json.loads(f.read())
    f.close()

    if file.endswith(".pson"):
        paldata = data
    else:
        paldata = data['properties']['worldSaveData']['value']['CharacterSaveParameterMap']['value']

        f = open("current.pson", "w", encoding="utf8")
        json.dump(paldata, f, indent=4)
        f.close()


    for i in paldata:
        try:
            p = PalEntity(i)
            palbox.append(p)

            n = p.GetFullName()

        except Exception as e:
            unknown.append(i)
            print(f"Error occured: {str(e)}")
            # print(f"Debug: Data {i}")

    updateDisplay()

    print(f"Unknown list contains {len(unknown)} entries")
    #for i in unknown:
        #print (i)
    
    refresh()

    changetext(-1)

def updateDisplay():
    listdisplay.delete(0,END)
    palbox.sort(key=sortPals)

    for p in palbox:
        listdisplay.insert(END, p.GetFullName())

        if p.isBoss:
            listdisplay.itemconfig(END, {'fg': 'red'})
        elif p.isLucky:
            listdisplay.itemconfig(END, {'fg': 'blue'})
    

def savefile():
    global palbox
    global data
    skilllabel.config(text="正在保存中，请耐心等待...（最多可能需要5分钟）")

    if isPalSelected():
        i = int(listdisplay.curselection()[0])
        refresh(i)
    
    file = asksaveasfilename(filetype=[("All files", "*.sav.json *.pson"),("Palworld Saves", "*.sav.json"),("Palworld Box", "*.pson")])
    print(f"Opening file {file}")

    if not file.endswith(".pson") and not file.endswith("Level.sav.json"):
        messagebox.showerror("Incorrect file", "You can only save to an existing Level.sav.json or a new .pson file")

    if file.endswith(".pson"):
        savepson(file)
    else:
        savejson(file)

    changetext(-1)

def savepson(filename):
    f = open(filename, "w", encoding="utf8")
    if 'properties' in data:
        json.dump(data['properties']['worldSaveData']['value']['CharacterSaveParameterMap']['value'], f, indent=4)
    else:
        json.dump(data, f, indent=4)
    f.close()

def savejson(filename):
    f = open(filename, "r", encoding="utf8")
    svdata = json.loads(f.read())
    f.close()

    if 'properties' in data:
        svdata['properties']['worldSaveData']['value']['CharacterSaveParameterMap']['value'] = data['properties']['worldSaveData']['value']['CharacterSaveParameterMap']['value']
    else:
        svdata['properties']['worldSaveData']['value']['CharacterSaveParameterMap']['value'] = data

    f = open(filename, "w", encoding="utf8")
    json.dump(svdata, f)
    f.close()

    changetext(-1)

def generateguid():
    print(uuid.uuid4())

def updatestats(e):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[e]

    pal.SetAttackMelee(meleevar.get())
    pal.SetAttackRanged(shotvar.get())
    pal.SetDefence(defvar.get())
    pal.SetWorkSpeed(wspvar.get())

def takelevel():
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]

    if pal.GetLevel() == 1:
        return
    pal.SetLevel(pal.GetLevel()-1)
    refresh(i)

def givelevel():
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]

    if pal.GetLevel() == 50:
        return
    pal.SetLevel(pal.GetLevel()+1)
    refresh(i)

def changespeciestype(evt):
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]
    
    pal.SetType(speciesvar.get())
    updateDisplay()
    refresh(palbox.index(pal))

def refresh(num=0):
    listdisplay.select_set(num)
    listdisplay.event_generate("<<ListboxSelect>>")

def converttojson():

    skilllabel.config(text="文件转换中...这可能需要一段时间.")
    
    file = askopenfilename(filetype=[("All files", "*.sav")])
    print(f"Opening file {file}")

    doconvertjson(file)

def doconvertjson(file, compress=False):
    SaveConverter.convert_sav_to_json(file, file.replace(".sav", ".sav.json"), compress)

    load(file.replace(".sav", ".sav.json"))

    changetext(-1)

def converttosave():
    skilllabel.config(text="文件转换中...这可能需要一段时间.")
    
    file = askopenfilename(filetype=[("All files", "*.sav.json")])
    print(f"Opening file {file}")

    doconvertsave(file)


def doconvertsave(file):
    SaveConverter.convert_json_to_sav(file, file.replace(".sav.json", ".sav"))

    changetext(-1)

def swapgender():
    if not isPalSelected():
        return
    i = int(listdisplay.curselection()[0])
    pal = palbox[i]

    pal.SwapGender()
    refresh(i)

root = Tk()
purplepanda = ImageTk.PhotoImage(Image.open(f'resources/叶胖达.png').resize((240,240)))
root.iconphoto(True, purplepanda)
root.title(f"帕鲁属性编辑器 v{version}")
root.geometry("") # auto window size
root.minsize("800", "500") # minwidth for better view
#root.resizable(width=False, height=False)

tools = Menu(root)
root.config(menu=tools)

filemenu = Menu(tools, tearoff=0)
filemenu.add_command(label="加载存档", command=loadfile)
filemenu.add_command(label="保存修改", command=savefile)

tools.add_cascade(label="文件", menu=filemenu, underline=0)

toolmenu = Menu(tools, tearoff=0)
toolmenu.add_command(label="生成 GUID", command=generateguid)
toolmenu.add_command(label="调试", command=toggleDebug)

tools.add_cascade(label="工具", menu=toolmenu, underline=0)

convmenu = Menu(tools, tearoff=0)
convmenu.add_command(label="转换存档文件为Json文件", command=converttojson)
convmenu.add_command(label="转换Json文件为存档文件", command=converttosave)

tools.add_cascade(label="文件格式转换", menu=convmenu, underline=0)


scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT, fill=Y)
listdisplay = Listbox(root, width=30, yscrollcommand=scrollbar.set, exportselection=0)
listdisplay.pack(side=LEFT, fill=BOTH)
listdisplay.bind("<<ListboxSelect>>", onselect)
scrollbar.config(command=listdisplay.yview)

infoview = Frame(root, relief="groove", borderwidth=2, width=480, height=480)
infoview.pack(side=RIGHT, fill=BOTH, expand=True)

dataview = Frame(infoview)
dataview.pack(side=TOP, fill=BOTH)

resourceview = Frame(dataview)
resourceview.pack(side=LEFT, fill=BOTH, expand=True)

portrait = Label(resourceview, image=purplepanda, relief="sunken", borderwidth=2)
portrait.pack()

ftsize = 18

typeframe = Frame(resourceview)
typeframe.pack(expand=True, fill=X)
ptype = Label(typeframe, text="电", font=("Arial", ftsize), bg=Elements.ELECTRICITY.value.GetColour(), width=6)
ptype.pack(side=LEFT, expand=True, fill=X)
stype = Label(typeframe, text="暗", font=("Arial", ftsize), bg=Elements.DARK.value.GetColour(), width=6)
stype.pack(side=RIGHT, expand=True, fill=X)

deckview = Frame(dataview, width=320, relief="sunken", borderwidth=2, pady=0)
deckview.pack(side=RIGHT, fill=BOTH, expand=True)

headerframe = Frame(deckview, padx=0, pady=0, bg="darkgrey")
headerframe.pack(fill=X)
headerframe.grid_rowconfigure(0, weight=1)
headerframe.grid_columnconfigure((0,2), uniform="equal")
headerframe.grid_columnconfigure(1, weight=1)

title = Label(headerframe, text=f"帕鲁编辑器 - v{version}", bg="darkgrey", font=("Arial", 24), width=17)
title.bind("<Enter>", lambda evt, num="owner": changetext(num))
title.bind("<Leave>", lambda evt, num=-1: changetext(num))
title.grid(row=0, column=1, sticky="nsew")

minlvlbtn = Button(headerframe, text="➖", borderwidth=1, font=("Arial", ftsize-2), command=takelevel, bg="darkgrey")
minlvlbtn.grid(row=0, column=0, sticky="nsew")

addlvlbtn = Button(headerframe, text="➕", borderwidth=1, font=("Arial", ftsize-2), command=givelevel, bg="darkgrey")
addlvlbtn.grid(row=0, column=2, sticky="nsew")


labelview = Frame(deckview, bg="lightgrey", pady=0, padx=16)
labelview.pack(side=LEFT, expand=True, fill=BOTH)

name = Label(labelview, text="物种", font=("Arial", ftsize), bg="lightgrey")
name.pack(expand=True, fill=X)
gender = Label(labelview, text="性别", font=("Arial", ftsize), bg="lightgrey", width=6)
gender.pack(expand=True, fill=X)
attack = Label(labelview, text="攻击", font=("Arial", ftsize), bg="lightgrey", width=6)
attack.pack(expand=True, fill=X)
defence = Label(labelview, text="防御", font=("Arial", ftsize), bg="lightgrey", width=6)
defence.pack(expand=True, fill=X)
workspeed = Label(labelview, text="工作速度", font=("Arial", ftsize), bg="lightgrey", width=10)
workspeed.pack(expand=True, fill=X)
rankspeed = Label(labelview, text="星级", font=("Arial", ftsize), bg="lightgrey")
rankspeed.pack(expand=True, fill=X)

editview = Frame(deckview)
editview.pack(side=RIGHT, expand=True, fill=BOTH)

species = [e.value.GetName() for e in PalType]
species.sort()
speciesvar = StringVar()
speciesvar.set("物种选择")
palname = OptionMenu(editview, speciesvar, *species, command=changespeciestype)
palname.config(font=("Arial", ftsize), padx=0, pady=0, borderwidth=1, width=5, direction='right')
palname.pack(expand=True, fill=X)

genderframe = Frame(editview, pady=0)
genderframe.pack()
palgender = Label(genderframe, text="未知", font=("Arial", ftsize), fg=PalGender.UNKNOWN.value, width=10)
palgender.pack(side=LEFT, expand=True, fill=X)
swapbtn = Button(genderframe, text="↺", borderwidth=1, font=("Arial", ftsize-2), command=swapgender)
swapbtn.pack(side=RIGHT)

def clamp(var):
    try:
        int(var.get())
    except TclError as e:
        return

    if var.get() > 100:
        var.set(100)
        return

    if var.get() < 0:
        var.set(0)
        return

def ivvalidate(p):
    if len(p) > 3:
        return False
    
    if p.isdigit() or p == "":
        return True

    return False

def fillifempty(var):
    try:
        int(var.get())
    except TclError as e:
        var.set(0)

valreg = root.register(ivvalidate)

attackframe = Frame(editview, width=6)
attackframe.pack(fill=X)
meleevar = IntVar()
shotvar = IntVar()
meleevar.trace("w", lambda name, index, mode, sv=meleevar: clamp(sv))
shotvar.trace("w", lambda name, index, mode, sv=shotvar: clamp(sv))
meleevar.set(100)
shotvar.set(0)
meleeicon = Label(attackframe, text="⚔", font=("Arial", ftsize))
meleeicon.pack(side=LEFT)
shoticon = Label(attackframe, text="🏹", font=("Arial", ftsize))
shoticon.pack(side=RIGHT)
palmelee = Entry(attackframe, textvariable=meleevar, font=("Arial", ftsize), width=6)
palmelee.config(justify="center", validate="all", validatecommand=(valreg, '%P'))
palmelee.bind("<FocusOut>", lambda evt, sv=meleevar: fillifempty(sv))
palmelee.pack(side=LEFT)
palshot = Entry(attackframe, textvariable=shotvar, font=("Arial", ftsize), width=6)
palshot.config(justify="center", validate="all", validatecommand=(valreg, '%P'))
palshot.bind("<FocusOut>", lambda evt, sv=shotvar: fillifempty(sv))
palshot.pack(side=RIGHT)


defvar = IntVar()
defvar.trace("w", lambda name, index, mode, sv=defvar: clamp(sv))
defvar.set(100)
paldef = Entry(editview, textvariable=defvar, font=("Arial", ftsize), width=6)
paldef.config(justify="center", validate="all", validatecommand=(valreg, '%P'))
paldef.bind("<FocusOut>", lambda evt, sv=defvar: fillifempty(sv))
paldef.pack(expand=True, fill=X)


wspvar = IntVar()
wspvar.trace("w", lambda name, index, mode, sv=wspvar: clamp(sv))
wspvar.set(70)
palwsp = Entry(editview, textvariable=wspvar, font=("Arial", ftsize), width=6)
palwsp.config(justify="center", validate="all", validatecommand=(valreg, '%P'))
palwsp.bind("<FocusOut>", lambda evt, sv=wspvar: fillifempty(sv))
palwsp.pack(expand=True, fill=X)

ranks = ('0', '1', '2', '3', '4')
ranksvar = IntVar()
palrank = OptionMenu(editview, ranksvar, *ranks, command=changerankchoice)
palrank.config(font=("Arial", ftsize),  justify='center', padx=0, pady=0, borderwidth=1, width=5)
ranksvar.set(ranks[4])
palrank.pack(expand=True, fill=X)

# PASSIVE ABILITIES
skillview = Frame(infoview, relief="sunken", borderwidth=2)
skillview.pack(fill=BOTH, expand=True)

topview = Frame(skillview)
topview.pack(fill=BOTH, expand=True)
botview = Frame(skillview)
botview.pack(fill=BOTH, expand=True)

skills = [StringVar(), StringVar(), StringVar(), StringVar()]
for i in range(0, 4):
    skills[i].set("Unknown")
    skills[i].trace("w", lambda *args, num=i: changeskill(num))
skills[0].set("词条1")
skills[1].set("词条2")
skills[2].set("词条3")
skills[3].set("词条4")

op = [e.value for e in PalSkills]
op.sort()
op.pop(0)
skilldrops = [
    OptionMenu(topview, skills[0], *op),
    OptionMenu(topview, skills[1], *op),
    OptionMenu(botview, skills[2], *op),
    OptionMenu(botview, skills[3], *op)
    ]

skilldrops[0].pack(side=LEFT, expand=True, fill=BOTH)
skilldrops[0].config(font=("Arial", ftsize), width=6, direction="right")
skilldrops[1].pack(side=RIGHT, expand=True, fill=BOTH)
skilldrops[1].config(font=("Arial", ftsize), width=6, direction="right")
skilldrops[2].pack(side=LEFT, expand=True, fill=BOTH)
skilldrops[2].config(font=("Arial", ftsize), width=6, direction="right")
skilldrops[3].pack(side=RIGHT, expand=True, fill=BOTH)
skilldrops[3].config(font=("Arial", ftsize), width=6, direction="right")

skilldrops[0].bind("<Enter>", lambda evt, num=0: changetext(num))
skilldrops[1].bind("<Enter>", lambda evt, num=1: changetext(num))
skilldrops[2].bind("<Enter>", lambda evt, num=2: changetext(num))
skilldrops[3].bind("<Enter>", lambda evt, num=3: changetext(num))
skilldrops[0].bind("<Leave>", lambda evt, num=-1: changetext(num))
skilldrops[1].bind("<Leave>", lambda evt, num=-1: changetext(num))
skilldrops[2].bind("<Leave>", lambda evt, num=-1: changetext(num))
skilldrops[3].bind("<Leave>", lambda evt, num=-1: changetext(num))

# PRESETS
framePresets = Frame(infoview, relief="groove", borderwidth=0)
framePresets.pack(fill=BOTH, expand=True)

framePresetsTitle = Frame(framePresets)
framePresetsTitle.pack(fill=BOTH)
presetTitle = Label(framePresetsTitle, text='预设:', anchor='w', bg="darkgrey", font=("Arial", ftsize), width=6, height=1).pack(fill=BOTH)

framePresetsButtons = Frame(framePresets, relief="groove", borderwidth=4)
framePresetsButtons.pack(fill=BOTH, expand=True)

framePresetsButtons1 = Frame(framePresetsButtons)
framePresetsButtons1.pack(fill=BOTH, expand=True)
makeworkerBtn = Button(framePresetsButtons1, text="工作速度优先", command=makeworker)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)
makeworkerBtn = Button(framePresetsButtons1, text="移动速度优先", command=makerunner)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)
makeworkerBtn = Button(framePresetsButtons1, text="防御力优先", command=maketank)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)

framePresetsButtons2 = Frame(framePresetsButtons)
framePresetsButtons2.pack(fill=BOTH, expand=True)
makeworkerBtn = Button(framePresetsButtons2, text="最大伤害", command=makedmgmax)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)
makeworkerBtn = Button(framePresetsButtons2, text="平衡伤害", command=makedmgbalanced)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)
makeworkerBtn = Button(framePresetsButtons2, text="龙属性伤害", command=makedmgdragon)
makeworkerBtn.config(font=("Arial", 12))
makeworkerBtn.pack(side=LEFT, expand=True, fill=BOTH)

# PRESETS OPTIONS
framePresetsExtras = Frame(framePresets, relief="groove", borderwidth=4)
framePresetsExtras.pack(fill=BOTH, expand=True)

framePresetsLevel = Frame(framePresetsExtras)
framePresetsLevel.pack(fill=BOTH, expand=True)
presetTitleLevel = Label(framePresetsLevel, text='设置等级:', anchor='center', bg="lightgrey", font=("Arial", 13), width=20, height=1).pack(side=LEFT, expand=False, fill=Y)
checkboxLevelVar = IntVar()
checkboxLevel = Checkbutton(framePresetsLevel, text='预设等级修改', variable=checkboxLevelVar, onvalue='1', offvalue='0').pack(side=LEFT,expand=False, fill=BOTH)
textboxLevelVar = IntVar(value=1)
textboxLevel = Entry(framePresetsLevel, textvariable=textboxLevelVar, justify='center', width=10)
textboxLevel.config(font=("Arial", 10), width=10)
textboxLevel.pack(side=LEFT,expand=True, fill=Y)

framePresetsRank = Frame(framePresetsExtras)
framePresetsRank.pack(fill=BOTH, expand=True)
presetTitleRank = Label(framePresetsRank, text='设置星级:', anchor='center', bg="lightgrey", font=("Arial", 13), width=20, height=1).pack(side=LEFT, expand=False, fill=Y)
checkboxRankVar = IntVar()
checkboxRank = Checkbutton(framePresetsRank, text='预设星级修改', variable=checkboxRankVar, onvalue='1', offvalue='0').pack(side=LEFT,expand=False, fill=BOTH)
optionMenuRankVar = IntVar(value=1)
ranks = ('0', '1', '2', '3', '4')
optionMenuRank = OptionMenu(framePresetsRank, optionMenuRankVar, *ranks)
optionMenuRankVar.set(ranks[0])
optionMenuRank.config(font=("Arial", 10), width=5, justify='center')
optionMenuRank.pack(side=LEFT, expand=True, fill=Y)

framePresetsAttributes = Frame(framePresetsExtras)
framePresetsAttributes.pack(fill=BOTH, expand=False)
presetTitleAttributes = Label(framePresetsAttributes, text='设置属性:', anchor='center', bg="lightgrey", font=("Arial", 13), width=20, height=1).pack(side=LEFT, expand=False, fill=Y)
checkboxAttributesVar = IntVar()
checkboxAttributes = Checkbutton(framePresetsAttributes, text='预设属性修改', variable=checkboxAttributesVar, onvalue='1', offvalue='0').pack(side=LEFT,expand=False, fill=BOTH)
presetTitleAttributesTodo = Label(framePresetsAttributes, text='(功能开发中)', font=("Arial", 10), width=10, justify='center').pack(side=LEFT, expand=True, fill=Y)

# DEBUG
frameDebug = Frame(infoview, relief="flat")
frameDebug.pack()
frameDebug.pack_forget()
presetTitle = Label(frameDebug, text='调试:', anchor='w', bg="darkgrey", font=("Arial", ftsize), width=6, height=1).pack(fill=BOTH)
button = Button(frameDebug, text="获取信息", command=getSelectedPalInfo)
button.config(font=("Arial", 12))
button.pack(side=LEFT, expand=True, fill=BOTH)
button = Button(frameDebug, text="获取数据", command=getSelectedPalData)
button.config(font=("Arial", 12))
button.pack(side=LEFT, expand=True, fill=BOTH)

# FOOTER
frameFooter = Frame(infoview, relief="flat")
frameFooter.pack(fill=BOTH, expand=False)
skilllabel = Label(frameFooter, text="将鼠标悬停在技能上即可查看其描述")
skilllabel.pack()



root.mainloop()
