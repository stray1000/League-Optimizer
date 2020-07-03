import ddragon as lol
import os
from tkinter import *
from PIL import Image, ImageTk

#Create Window Object

app = Tk()

def item_window():
    global item_list

    item_list = Toplevel()
    item_list.title('Items')
    item_list.geometry('1360x820')

    files = [i for i in os.listdir("C:/Users/stray/Desktop/League Optimizer/item") if i.endswith("png")]
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    item_icons = []

    for x in files:
        if counter2 == 20:
            counter3 += 10
            counter1 -= 20
            counter2 = 0

        canvas = Canvas(item_list, width = 64, height = 64)
        canvas.grid(row = 10 + counter3, column = 0 + counter1)
        image = Image.open('C:/Users/stray/Desktop/League Optimizer/item/' + x)
        photo = ImageTk.PhotoImage(image=image, master=item_list)
        canvas.create_image(0, 0, image=photo,anchor=NW)
        canvas.photo = photo

        button = Button(item_list, image = canvas.photo, borderwidth=0, highlightthickness=0,
                      command=lambda x=x: button_click_item(x))
        button.grid(row = 10 + counter3, column = 0 + counter1)

        counter1 += 1
        counter2 += 1
        counter4 += 1

    print(item_icons)

def button_click_item(x):
    print(x)

def button_click(x):
    name = x.rsplit( ".", 1 )[ 0 ]

    base_stats = lol.champion_data['data'][name]['stats']
    Base_HP = base_stats['hp']
    Base_MP = base_stats['mp']
    Hp_per_level = base_stats['hpperlevel']
    Mp_per_level = base_stats['mpperlevel']
    Base_Armor = base_stats['armor']
    Armor_per_level = base_stats['armorperlevel']
    Base_MR = base_stats['spellblock']
    MR_per_level = base_stats['spellblockperlevel']
    Base_movespeed = base_stats['movespeed']
    Base_attack_range = base_stats['attackrange']
    Base_HP_Regen = base_stats['hpregen']
    HP_Regen_per_level = base_stats['hpregenperlevel']
    Base_MP_Regen = base_stats['mpregen']
    MP_Regen_per_level = base_stats['mpregenperlevel']
    Base_Crit = 0
    Crit_per_level = 0
    Base_AP = 0
    Base_AD = base_stats['attackdamage']
    AD_per_level = base_stats['attackdamageperlevel']
    Base_ASPD = base_stats['attackspeed']
    ASPD_per_level = base_stats['attackspeedperlevel']

    # global newwindow
    # newwindow = Toplevel()
    # newwindow.title(name)
    # newwindow.geometry('308x560')

    global stats
    stats = Toplevel()
    stats.title(name)
    # stats.geometry('500x720')
    stats.geometry('1920x960')

    champion_label = Label(stats, text="Champion: " + name, font=("bold", 22))
    champion_label.grid(row=0, column=0, stick=W)

    champion_HP = Label(stats, text="Base HP: " + str(Base_HP), font=("bold", 22))
    champion_HP.grid(row=1, column=0, sticky=W)

    champion_MP = Label(stats, text="Base MP: " + str(Base_MP), font=("bold", 22))
    champion_MP.grid(row=2, column=0, sticky=W)

    champion_HP_per_level = Label(stats, text="HP per level: " + str(Hp_per_level), font=("bold", 22))
    champion_HP_per_level.grid(row=3, column=0, sticky=W)

    champion_MP_per_level = Label(stats, text="MP per level: " + str(Mp_per_level), font=("bold", 22))
    champion_MP_per_level.grid(row=4, column=0, sticky=W)

    champion_AD = Label(stats, text="Base Attack Damage: " + str(Base_AD), font=("bold", 22))
    champion_AD.grid(row=5, column=0, sticky=W)

    champion_AP = Label(stats, text="Base Ability Power: " + str(Base_AP), font=("bold", 22))
    champion_AP.grid(row=6, column=0, sticky=W)

    champion_MOV = Label(stats, text="Movespeed: " + str(Base_movespeed), font=("bold", 22))
    champion_MOV.grid(row=7, column=0, sticky=W)

    champion_Armor = Label(stats, text="Base Armor: " + str(Base_Armor), font=("bold", 22))
    champion_Armor.grid(row=8, column=0, sticky=W)

    champion_MR = Label(stats, text="Base Magic Resistance: " + str(Base_MR), font=("bold", 22))
    champion_MR.grid(row=9, column=0, sticky=W)

    champion_ASPD = Label(stats, text="Base Attack Speed: " + str(Base_ASPD), font=("bold", 22))
    champion_ASPD.grid(row=10, column=0, sticky=W)

    champion_Crit = Label(stats, text="Base Crititcal Chance: " + str(Base_Crit), font=("bold", 22))
    champion_Crit.grid(row=11, column=0, sticky=W)

    champion_HPRegen = Label(stats, text="Base HP Regeneration: " + str(Base_HP_Regen), font=("bold", 22))
    champion_HPRegen.grid(row=12, column=0, sticky=W)

    champion_MRRegen = Label(stats, text="Base MP Regeneration: " + str(Base_MP_Regen), font=("bold", 22))
    champion_MRRegen.grid(row=13, column=0, sticky=W)

    champion_AD_per_level = Label(stats, text="Attack Damage per level: " + str(AD_per_level), font=("bold", 22))
    champion_AD_per_level.grid(row=14, column=0, sticky=W)

    champion_Range = Label(stats, text="Base Attack Range: " + str(Base_attack_range), font=("bold", 22))
    champion_Range.grid(row=15, column=0, sticky=W)

    champion_ASPD_per_level = Label(stats, text="Attack Speed per level: " + str(ASPD_per_level), font=("bold", 22))
    champion_ASPD_per_level.grid(row=16, column=0, sticky=W)

    champion_Armor_per_level = Label(stats, text="Armor per level: " + str(Armor_per_level), font=("bold", 22))
    champion_Armor_per_level.grid(row=17, column=0, sticky=W)

    champion_MR_per_level = Label(stats, text="Magic Resistance per level: " + str(MR_per_level), font=("bold", 22))
    champion_MR_per_level.grid(row=18, column=0, sticky=W)

    #1280x720
    # canvas = Canvas(newwindow, width = 308, height = 560)
    # canvas.grid(row = 0, column = 0)
    # image = Image.open('C:/Users/stray/Desktop/League Optimizer/loading/' + name + '_0.jpg')
    # photo = ImageTk.PhotoImage(image = image, master = newwindow)
    # canvas.create_image(0, 0, image = photo, anchor = NW)
    # canvas.photo = photo

    canvas = Canvas(stats, width = 308, height = 560)
    canvas.grid(row = 0, column = 0)
    image = Image.open('C:/Users/stray/Desktop/League Optimizer/loading/' + name + '_0.jpg')
    photo = ImageTk.PhotoImage(image = image, master = stats)
    canvas.create_image(0, 0, image = photo, anchor = NW)
    canvas.photo = photo


app.title('LeagueOptimizer 1.0')
app.geometry('1920x960')

#Champion
files = [i for i in os.listdir("C:/Users/stray/Desktop/League Optimizer/champion") if i.endswith("png")]
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
champion_icons = []

for x in files:

    if counter2 == 20:
        counter3 += 10
        counter1 -= 20
        counter2 = 0

    # canvas = Canvas(app, width = 120, height = 120)
    # canvas.grid(row = 10 + counter3, column = 0 + counter1)
    # image = Image.open('C:/Users/stray/Desktop/League Optimizer/champion/' + x)
    # photo = ImageTk.PhotoImage(image=image, master=app)
    # canvas.create_image(0, 0, image=photo,anchor=NW)
    # canvas.photo = photo

    image = Image.open('C:/Users/stray/Desktop/League Optimizer/champion/' + x)
    photo = ImageTk.PhotoImage(image=image, master=app)
    champion_icons.append(photo)
    button = Button(app, image = champion_icons[counter4], borderwidth=0, highlightthickness=0,
                 command=lambda x=x: button_click(x))
    button.grid(row = 10 + counter3, column = 0 + counter1)

    # def on_click(event=None):
    #     # `command=` calls function without argument
    #     # `bind` calls function with one argument
    #     print("image clicked")
    #
    # canvas.bind('<Button-1>', on_click)

    counter1 += 1
    counter2 += 1
    counter4 += 1

next = Button(app, text = 'Items', borderwidth= 5,  font=("bold", 22), highlightthickness= 0, command=item_window)
next.grid(row = 80, column = 3)

#Start Program
app.mainloop( )
