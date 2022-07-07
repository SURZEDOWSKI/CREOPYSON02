# %%
import creopyson
import time

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)

# %%
def start_creo():
    import subprocess
    subprocess.Popen('"c://Program Files/PTC/Creo 7.0.1.0/Parametric/bin/parametric.bat"')

# %%
if c.is_creo_running():
    c = creopyson.Client()
    c.connect()
    c.creo_set_creo_version(7)
    creopyson.file_open(c, file_="projekt2.prt", dirname="C:/Users/Public/Documents/API_CAD/projekt2")
else:
    start_creo()
    wU = True
    while wU == True:
        if c.is_creo_running(): #checks the condition
            c = creopyson.Client()
            c.connect()
            c.creo_set_creo_version(7)
            creopyson.file_open(c, file_="projekt2.prt", dirname="C:/Users/Public/Documents/API_CAD/projekt2")
            wU = False
        time.sleep(5) #waits 60s for preformance
    

# %%
def changedimCA(val):
    c.dimension_set("dimCA", val)
    return val

def changedimCB(val):
    c.dimension_set("dimCB", val)
    return val

# %%
def changedimA(val, CA):
    changedimCA(CA)
    c.dimension_set("dimA", val)
    c.dimension_set("length_dimC", (val-CA))

def changedimB(val, CB):
    changedimCB(CB)
    c.dimension_set("dimB", val)
    c.dimension_set("height_dimC", (val-CB))

# %%
def changedimEFA(valE, valF, valDIM_DIST):
    c.dimension_set("dimEA", valE)
    c.dimension_set("dimFA", valF)
    c.dimension_set("dim_distEFA", valDIM_DIST)

def changedimEFB(valE, valF, valDIM_DIST):
    c.dimension_set("dimEB", valE)
    c.dimension_set("dimFB", valF)
    c.dimension_set("dim_distEFB", valDIM_DIST)

# %%
def supress_all():
    c.feature_suppress(name="WYPUSTA1")
    c.feature_suppress(name="WYPUSTB1")
    c.feature_suppress(name="PATTERN_OTWORYA140")
    c.feature_suppress(name="PATTERN_OTWORYB140")
    wypust('A', 0)
    wypust('B', 0)

# %%
def wypust(bok, tryb):
    if bok == 'A':
        if tryb == 0:
            c.feature_suppress(name="WYPUSTA1")            
        else:
            c.feature_resume(name="WYPUSTA1")
            c.feature_resume(name="WYPUSTA2")
            c.feature_resume(name="WYPUSTA3")
    else:
        if tryb == 0:
            c.feature_suppress(name="WYPUSTB1")            
        else:
            c.feature_resume(name="WYPUSTB1")
            c.feature_resume(name="WYPUSTB2")
            c.feature_resume(name="WYPUSTB3")

# %%
def save_wymiary(nazwa, A, B, C, D, E, F):
    material_name = c.file_get_cur_material()
    mass = c.file_massprops()['mass']

    msg =str("Nazwa: " + nazwa +
    "\nA= " + str(A) +
    "\nB= " + str(B) +
    "\nC= " + str(C) +
    "\nD= " + str(D) +
    "\nE= " + str(E) +
    "\nF= " + str(F) +
    "\nNazwa materiału: " + material_name +
    "\nMasa modelu: " +  str(mass))

    f = open("wymiary.txt", 'w')
    f.write(msg)
    print(msg)

# %%
def default():
    
    supress_all()

    changedimA(140, 8)
    changedimB(140, 8)
    changedimEFA(36, 10, 22)
    changedimEFB(36, 10, 22)

    wypust('A', 1)
    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYB140")

    creopyson.file.regenerate(c)

    save_wymiary('model prototypowy', 140, 140, 8, 100, 36, 10)

    creopyson.file.regenerate(c)

# %%
def W1():
    supress_all()

    changedimA(100, 8)
    changedimB(100, 8)
    changedimEFA(36, 10, 22)
    changedimEFB(36, 10, 22)

    creopyson.file.regenerate(c)

    save_wymiary('W1', 100, 100, 8, 100, 36, 10)

    creopyson.file.regenerate(c)

    

# %%
def W2():
    supress_all()

    changedimA(100, 8)
    changedimB(140, 8)
    changedimEFA(36, 10, 22)
    changedimEFB(36, 10, 22)

    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYB140")

    creopyson.file.regenerate(c)

    save_wymiary('W2', 100, 140, 8, 100, 36, 10)

    creopyson.file.regenerate(c)

# %%
def W3():
    supress_all()

    changedimA(100, 8)
    changedimB(180, 8)
    changedimEFA(36, 10, 22)
    changedimEFB(36, 10, 22)

    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYB140")
    c.feature_resume(name="PATTERN_OTWORYB180")

    creopyson.file.regenerate(c)

    save_wymiary('W3', 100, 180, 8, 100, 36, 10)

    creopyson.file.regenerate(c)

# %%
def W4():
    supress_all()

    changedimA(140, 10)
    changedimB(100, 10)
    changedimEFA(38, 12, 19)
    changedimEFB(38, 12, 19)

    wypust('A', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")

    creopyson.file.regenerate(c)

    save_wymiary('W4', 140, 100, 10, 100, 38, 12)

    creopyson.file.regenerate(c)

# %%
def W5():
    supress_all()

    changedimA(140, 10)
    changedimB(140, 10)
    changedimEFA(38, 12, 19)
    changedimEFB(38, 12, 19)

    wypust('A', 1)
    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYB140")

    creopyson.file.regenerate(c)

    save_wymiary('W5', 140, 140, 10, 100, 38, 12)

    creopyson.file.regenerate(c)

# %%
def W6():
    supress_all()

    changedimA(140, 10)
    changedimB(180, 10)
    changedimEFA(38, 12, 19)
    changedimEFB(38, 12, 19)

    wypust('A', 1)
    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYB140")
    c.feature_resume(name="PATTERN_OTWORYB180")

    creopyson.file.regenerate(c)

    save_wymiary('W6', 140, 180, 10, 100, 38, 12)

    creopyson.file.regenerate(c)

# %%
def W7():
    supress_all()

    changedimA(180, 11)
    changedimB(100, 11)
    changedimEFA(40, 14, 16)
    changedimEFB(40, 14, 16)

    wypust('A', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYA180")

    creopyson.file.regenerate(c)

    save_wymiary('W7', 180, 100, 11, 100, 40, 14)

    creopyson.file.regenerate(c)

# %%
def W8():
    supress_all()

    changedimA(180, 11)
    changedimB(140, 11)
    changedimEFA(40, 14, 16)
    changedimEFB(40, 14, 16)

    wypust('A', 1)
    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYA180")
    c.feature_resume(name="PATTERN_OTWORYB140")

    creopyson.file.regenerate(c)

    save_wymiary('W8', 180, 140, 11, 100, 40, 14)

    creopyson.file.regenerate(c)

# %%
def W9():
    supress_all()

    changedimA(180, 11)
    changedimB(180, 11)
    changedimEFA(40, 14, 16)
    changedimEFB(40, 14, 16)

    wypust('A', 1)
    wypust('B', 1)
    c.feature_resume(name="PATTERN_OTWORYA140")
    c.feature_resume(name="PATTERN_OTWORYA180")
    c.feature_resume(name="PATTERN_OTWORYB140")
    c.feature_resume(name="PATTERN_OTWORYB180")

    creopyson.file.regenerate(c)

    save_wymiary('W9', 180, 180, 11, 100, 40, 14)

    creopyson.file.regenerate(c)

# %%
def loadMat(name, src):
    for i in range(len(name)):
        c.file_load_material_file(name[i], src)

# %%
loadMat(["Cast_iron_ductile", "Steel_cast", "Steel_medium_carbon"], r"C:\Program Files\PTC\Creo 7.0.1.0\Common Files\text\materials-library\Standard-Materials_Granta-Design\Ferrous_metals")

# %%
def changeMat():
    print("Aktualny materiał: " + c.file_get_cur_material())
    try:
        print("\nDostępne materiały: " + str(c.file_list_materials()))
        print("Podaj nazwę materiału:")
        name = input()
        name = str(name)
        c.file_set_cur_material(name)
        current = c.file_get_cur_material()
    except:
        print("Zła wartość!")
    else:
        print(current)

# %%
def changeDir():
    try:
        print(c.creo_pwd())
        print("Podaj ścieżkę:")
        newDir = input()
        newDir = str(newDir)
        new = c.creo_cd(newDir)
    except:
        print("Wrong directory path")
    else:
        print(new)

# %%
def changeModel(model):
    if model == "1":
        W1()
    elif model == "2":
        W2()
    elif model == "3":
        W3()
    elif model == "4":
        W4()
    elif model == "5":
        W5()
    elif model == "6":
        W6()
    elif model == "7":
        W7()
    elif model == "8":
        W8()
    elif model == "9":
        W9()
    elif model == "0":
        default() 
    else:
        print("Podano złą wartość!")

# %%
def model_export():
    c.interface_export_file(file_type="STEP")
    c.interface_export_3dpdf()

# %%
def assembly():
    c.file_assemble("projekt2.prt")

# %%
def start():
    run = True
    while(run):
        print("Wybierz dostępną opcję: \
        \n1. Zmień model \
        \n2. Zmień materiał \
        \n3. Zmień katalog roboczy \
        \n4. Eksportuj model \
        \n5. Wstaw model do złożenia \
        \nQ. Wyjdź")   

        act = input()
        if act == "1":
            print("Wybierz model: \
                \n1. W1 \
                \n2. W2  \
                \n3. W3  \
                \n4. W4  \
                \n5. W5  \
                \n6. W6  \
                \n7. W7  \
                \n8. W8  \
                \n9. W9 \
                \n0. Model prototypowy")
            model = input()
            changeModel(model)
        elif act == "2":
            changeMat()
        elif act == "3":
            changeDir()
        elif act == "4":
            model_export()
        elif act == "5":
            assembly()
        elif act == "Q":
            run = False
        else:
            print("Podano złą wartość!")

# %%
start()
