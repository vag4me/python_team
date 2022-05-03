#Import module
import tkinter
from tkinter import *
from tkinter.ttk import *



#παρουσιαση φαγητου ψαροκροκετες
def monday_food1():
    clear_window_5()

    global photo_psarokroketes
    global back16
    global canv12
    global label20
    global label21

    canv12 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv12.place(relx=0.5, rely=0.5, anchor=CENTER)

    label20 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :230kcal.\n3) Υδατάνθρακες: 16g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label20.place(x=20, y=320)

    photo_psarokroketes = PhotoImage(file="ψαρακροκετες.png")
    label21 = Label(root, image=photo_psarokroketes)
    label21.place(x=650, y=250)

    back16 = Button(text="Πίσω", command=back_at_start16)
    back16.place(x=550, y=700)


#παρουσιαση φαγητου περκα
def monday_food2():
    clear_window_5()

    global photo_perka
    global back17
    global canv13
    global label22
    global label23

    canv13 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv13.place(relx=0.5, rely=0.5, anchor=CENTER)

    label22 = Label(
        text="1) Αλλεργιογόνες ουσίες: Αλλεργία των ψαριών.\n2) Θερμίδες Aνα 100γρα. :142kcal.\n3) Υδατάνθρακες: 1,6g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label22.place(x=20, y=320)

    photo_perka = PhotoImage(file="περκα_λεμονατη.png")
    label23 = Label(root, image=photo_perka)
    label23.place(x=650, y=250)

    back17 = Button(text="Πίσω", command=back_at_start17)
    back17.place(x=550, y=700)


#παρουσιαση φαγητου ριζοτο
def monday_food3():
    clear_window_5()

    global photo_rizoto
    global back18
    global canv14
    global label24
    global label25

    canv14 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv14.place(relx=0.5, rely=0.5, anchor=CENTER)

    label24 = Label(
        text="1) Αλλεργιογόνες ουσίες: Αλλεργία των ψαριών.\n2) Θερμίδες Aνα 100γρα. :519kcal.\n3) Υδατάνθρακες: 16.4g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label24.place(x=20, y=320)

    photo_rizoto = PhotoImage(file="rizoto.png")
    label25 = Label(root, image=photo_rizoto)
    label25.place(x=650, y=250)

    back18 = Button(text="Πίσω", command=back_at_start18)
    back18.place(x=550, y=700)


#παρουσιαση φαγητου μπακαλιαρος
def monday_food4():
    clear_window_5()

    global photo_mpakaliarow
    global back19
    global canv15
    global label26
    global label27

    canv15 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv15.place(relx=0.5, rely=0.5, anchor=CENTER)

    label26 = Label(
        text="1) Αλλεργιογόνες ουσίες: Αλλεργία των ψαριών.\n2) Θερμίδες Aνα 100γρα. :380kcal.\n3) Υδατάνθρακες: 25.4g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label26.place(x=20, y=320)

    photo_mpakaliarow = PhotoImage(file="μπακαλιαρος.png")
    label27 = Label(root, image=photo_mpakaliarow)
    label27.place(x=650, y=250)

    back19 = Button(text="Πίσω", command=back_at_start19)
    back19.place(x=550, y=700)


#παρουσιαση του φαγητου μπριζολα
def tuesday_food1():
    clear_window_3()

    global photo_mprizola
    global back8
    global canv4
    global label6
    global label5

    canv4 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv4.place(relx=0.5, rely=0.5, anchor=CENTER)

    label6 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σινάπι.\n2) Θερμίδες Aνα 100γρα. :380kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label6.place(x=20, y=320)


    photo_mprizola = PhotoImage(file="μπριζολα.png")
    label5 = Label(root, image=photo_mprizola)
    label5.place(x=650, y=250)

    back8 = Button(text="Πίσω",command=back_at_start8)
    back8.place(x=550,y=700)

#παρουσιαση του φαγητου τηγανια
def tuesday_food2():
    clear_window_3()

    global photo_tigania
    global back9
    global canv5
    global label7
    global label8

    canv5 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv5.place(relx=0.5, rely=0.5, anchor=CENTER)

    label7 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :230kcal.\n3) Υδατάνθρακες: 1.5g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label7.place(x=20, y=320)

    photo_tigania = PhotoImage(file="τηγανια.png")
    label8 = Label(root, image=photo_tigania)
    label8.place(x=650, y=250)

    back9 = Button(text="Πίσω", command=back_at_start9)
    back9.place(x=550, y=700)

#παρουσιαση του φαγητου αλα κρεμ
def tuesday_food3():
    clear_window_3()

    global photo_alakrem
    global back10
    global canv6
    global label9
    global label10

    canv6 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv6.place(relx=0.5, rely=0.5, anchor=CENTER)

    label9 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :260kcal.\n3) Υδατάνθρακες: 11g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label9.place(x=20, y=320)

    photo_alakrem = PhotoImage(file="αλα κρεμ.png")
    label10 = Label(root, image=photo_alakrem)
    label10.place(x=650, y=250)

    back10 = Button(text="Πίσω", command=back_at_start10)
    back10.place(x=550, y=700)

#παρουσιαση του φαγητου φαλαφελ
def tuesday_food4():
    clear_window_3()

    global photo_falafel
    global back11
    global canv7
    global label11
    global label12

    canv7 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv7.place(relx=0.5, rely=0.5, anchor=CENTER)

    label11 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :333kcal.\n3) Υδατάνθρακες: 26g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label11.place(x=20, y=320)

    photo_falafel = PhotoImage(file="φαλαφελ.png")
    label12 = Label(root, image=photo_falafel)
    label12.place(x=650, y=250)

    back11 = Button(text="Πίσω", command=back_at_start11)
    back11.place(x=550, y=700)


#παρουσιαση φαγητου fakes
def wensday_food1():
    clear_window_6()

    global photo_fakes
    global back20
    global canv16
    global label28
    global label29

    canv16 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv16.place(relx=0.5, rely=0.5, anchor=CENTER)

    label28 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :116kcal.\n3) Υδατάνθρακες: 20g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label28.place(x=20, y=320)

    photo_fakes = PhotoImage(file="φακες.png")
    label29 = Label(root, image=photo_fakes)
    label29.place(x=650, y=250)

    back20 = Button(text="Πίσω", command=back_at_start20)
    back20.place(x=550, y=700)

#παρουσιαση φαγητου ρεβυθια
def wensday_food2():
    clear_window_6()

    global photo_refithia
    global back21
    global canv17
    global label30
    global label31

    canv17 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv17.place(relx=0.5, rely=0.5, anchor=CENTER)

    label30 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :364kcal.\n3) Υδατάνθρακες: 61g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label30.place(x=20, y=320)

    photo_refithia = PhotoImage(file="ρεβυθια.png")
    label31 = Label(root, image=photo_refithia)
    label31.place(x=650, y=250)

    back21 = Button(text="Πίσω", command=back_at_start21)
    back21.place(x=550, y=700)


#παρουσιαση φαγητου φασολαδα
def wensday_food3():
    clear_window_6()

    global photo_fasolada
    global back22
    global canv18
    global label32
    global label33

    canv18 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv18.place(relx=0.5, rely=0.5, anchor=CENTER)

    label32 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σέλινο.\n2) Θερμίδες Aνα 100γρα. :142kcal.\n3) Υδατάνθρακες: 26g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label32.place(x=20, y=320)

    photo_fasolada = PhotoImage(file="φασολαδα.png")
    label33 = Label(root, image=photo_fasolada)
    label33.place(x=650, y=250)

    back22 = Button(text="Πίσω", command=back_at_start22)
    back22.place(x=550, y=700)

#παρουσιαση φαγητου γιγαντες
def wensday_food4():
    clear_window_6()

    global photo_gigantes
    global back23
    global canv19
    global label34
    global label35

    canv19 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv19.place(relx=0.5, rely=0.5, anchor=CENTER)

    label34 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σέλινο.\n2) Θερμίδες Aνα 100γρα. :149kcal.\n3) Υδατάνθρακες: 34g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label34.place(x=20, y=320)

    photo_gigantes = PhotoImage(file="Γιγαντες.png")
    label35 = Label(root, image=photo_gigantes)
    label35.place(x=650, y=250)

    back23 = Button(text="Πίσω", command=back_at_start23)
    back23.place(x=550, y=700)


#πααρουσιαση του φαγητου μπιφτεκι
def thurday_food1():
    clear_window_4()

    global photo_mpifteki
    global back12
    global canv8
    global label13
    global label14

    canv8 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv8.place(relx=0.5, rely=0.5, anchor=CENTER)

    label13 = Label(
        text="1) Αλλεργιογόνες ουσίες: Γλουτένη.\n2) Θερμίδες Aνα 100γρα. :208kcal.\n3) Υδατάνθρακες: 6.5g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label13.place(x=20, y=320)

    photo_mpifteki = PhotoImage(file="Mpifteki.png")
    label14 = Label(root, image=photo_mpifteki)
    label14.place(x=650, y=250)

    back12 = Button(text="Πίσω", command=back_at_start12)
    back12.place(x=550, y=700)

#παρουσιαση του φαγητου κοτοπουλο μπουτι
def thursday_food2():
    clear_window_4()

    global photo_mpouti
    global back13
    global canv9
    global label14
    global label15

    canv9 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv9.place(relx=0.5, rely=0.5, anchor=CENTER)

    label14 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σινάπι.\n2) Θερμίδες Aνα 100γρα. :209kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label14.place(x=20, y=320)

    photo_mpouti = PhotoImage(file="Κοτοπουλο_μπουτι.png")
    label15 = Label(root, image=photo_mpouti)
    label15.place(x=650, y=250)

    back13 = Button(text="Πίσω", command=back_at_start13)
    back13.place(x=550, y=700)

#παρουσιαση του φαγητου κοτομπουκιες
def thursday_food3():
    clear_window_4()

    global photo_kotompoykies
    global back14
    global canv10
    global label16
    global label17

    canv10 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv10.place(relx=0.5, rely=0.5, anchor=CENTER)

    label16 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σόγια,γλουτένη,αυγό.\n2) Θερμίδες Aνα 100γρα. :295kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label16.place(x=20, y=320)

    photo_kotompoykies = PhotoImage(file="κοτμπουκια.png")
    label17 = Label(root, image=photo_kotompoykies)
    label17.place(x=650, y=250)

    back14 = Button(text="Πίσω", command=back_at_start14)
    back14.place(x=550, y=700)

#παρουσιαση φαγητου κοπανακι κοτοπουλο
def thursday_food4():
    clear_window_4()

    global photo_kopanaki
    global back15
    global canv11
    global label18
    global label19

    canv11 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv11.place(relx=0.5, rely=0.5, anchor=CENTER)

    label18 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σινάπι.\n2) Θερμίδες Aνα 100γρα. :239kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label18.place(x=20, y=320)

    photo_kopanaki = PhotoImage(file="kopanaki.png")
    label19 = Label(root, image=photo_kopanaki)
    label19.place(x=650, y=250)

    back15 = Button(text="Πίσω", command=back_at_start15)
    back15.place(x=550, y=700)


#παρουσιαση φαγητου tortelinia
def saturday_food1():
    clear_window_7()

    global photo_tortelinia
    global back24
    global canv20
    global label36
    global label37

    canv20 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv20.place(relx=0.5, rely=0.5, anchor=CENTER)

    label36 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :306kcal.\n3) Υδατάνθρακες: 47g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label36.place(x=20, y=320)

    photo_tortelinia = PhotoImage(file="τορτελινια.png")
    label37 = Label(root, image=photo_tortelinia)
    label37.place(x=750, y=250)

    back24 = Button(text="Πίσω", command=back_at_start24)
    back24.place(x=550, y=700)

#παρουσιαση φαγητου κοκκινιστο
def saturday_food2():
    clear_window_7()

    global photo_kokkino
    global back25
    global canv21
    global label38
    global label39

    canv21 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv21.place(relx=0.5, rely=0.5, anchor=CENTER)

    label38 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :610kcal.\n3) Υδατάνθρακες: 6g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label38.place(x=20, y=320)

    photo_kokkino = PhotoImage(file="κρεας_κοκκινιστο.png")
    label39 = Label(root, image=photo_kokkino)
    label39.place(x=750, y=300)

    back25 = Button(text="Πίσω", command=back_at_start25)
    back25.place(x=550, y=700)


#παρουσιαση φαγητου λεμονατο
def saturday_food3():
    clear_window_7()

    global photo_lemonato
    global back26
    global canv22
    global label40
    global label41

    canv22 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv22.place(relx=0.5, rely=0.5, anchor=CENTER)

    label40 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :486kcal.\n3) Υδατάνθρακες: 7g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label40.place(x=20, y=320)

    photo_lemonato = PhotoImage(file="κρεας_λεμονατο.png")
    label41 = Label(root, image=photo_lemonato)
    label41.place(x=750, y=240)

    back26 = Button(text="Πίσω", command=back_at_start26)
    back26.place(x=550, y=700)


#παρουσιαση φαγητου σνιτζελ
def saturday_food4():
    clear_window_7()

    global photo_snitsel
    global back27
    global canv23
    global label42
    global label43

    canv23 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv23.place(relx=0.5, rely=0.5, anchor=CENTER)

    label42 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :250kcal.\n3) Υδατάνθρακες: 12.4g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label42.place(x=20, y=320)

    photo_snitsel = PhotoImage(file="Σνιτσελ.png")
    label43 = Label(root, image=photo_snitsel)
    label43.place(x=750, y=290)

    back27 = Button(text="Πίσω", command=back_at_start27)
    back27.place(x=550, y=700)

#παρουσιαση φαγητου σουτζουκακια
def friday_food1():
    clear_window_8()

    global photo_soutzoukakia
    global back28
    global canv24
    global label44
    global label45

    canv24 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv24.place(relx=0.5, rely=0.5, anchor=CENTER)

    label44 = Label(
        text="1) Αλλεργιογόνες ουσίες: Δεν βρέθηκε.\n2) Θερμίδες Aνα 100γρα. :150kcal.\n3) Υδατάνθρακες: 1.4g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label44.place(x=20, y=320)

    photo_soutzoukakia = PhotoImage(file="soutzoukaki.png")
    label45 = Label(root, image=photo_soutzoukakia)
    label45.place(x=700, y=250)

    back28 = Button(text="Πίσω", command=back_at_start28)
    back28.place(x=550, y=700)

#παρουσιαση φαγητου κεφτεδακια
def friday_food2():
    clear_window_8()

    global photo_keftedakia
    global back29
    global canv25
    global label46
    global label47

    canv25 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv25.place(relx=0.5, rely=0.5, anchor=CENTER)

    label46 = Label(
        text="1) Αλλεργιογόνες ουσίες: γλουτένη,σουσάμι,αυγο.\n2) Θερμίδες Aνα 100γρα. :196kcal.\n3) Υδατάνθρακες: 8g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label46.place(x=20, y=320)

    photo_keftedakia = PhotoImage(file="keftedaki.png")
    label47 = Label(root, image=photo_keftedakia)
    label47.place(x=730, y=310)

    back29 = Button(text="Πίσω", command=back_at_start29)
    back29.place(x=550, y=700)


#παρουσιαση φαγητου gigantes
def friday_food3():
    clear_window_8()

    global photo_giga
    global back30
    global canv26
    global label48
    global label49

    canv26 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv26.place(relx=0.5, rely=0.5, anchor=CENTER)

    label48 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σέλινο.\n2) Θερμίδες Aνα 100γρα. :149kcal.\n3) Υδατάνθρακες: 34g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label48.place(x=20, y=320)

    photo_giga = PhotoImage(file="Γιγαντες.png")
    label49 = Label(root, image=photo_giga)
    label49.place(x=700, y=250)

    back30 = Button(text="Πίσω", command=back_at_start30)
    back30.place(x=550, y=700)

#παρουσιαση φαγητου παστιτζιο
def friday_food4():
    clear_window_8()

    global photo_past
    global back31
    global canv27
    global label50
    global label51

    canv27 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv27.place(relx=0.5, rely=0.5, anchor=CENTER)

    label50 = Label(
        text="1) Αλλεργιογόνες ουσίες: Γλουτένη,λακτόζη,αυγό.\n2) Θερμίδες Aνα 100γρα. :220kcal.\n3) Υδατάνθρακες: 15g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label50.place(x=20, y=320)

    photo_past = PhotoImage(file="pastitsio.png")
    label51 = Label(root, image=photo_past)
    label51.place(x=700, y=250)

    back31 = Button(text="Πίσω", command=back_at_start31)
    back31.place(x=550, y=700)

#παρουσιαση φαγητου κοτομποθκιες
def sunday_food1():
    clear_window_9()

    global photo_kotom
    global back32
    global canv28
    global label52
    global label53

    canv28 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv28.place(relx=0.5, rely=0.5, anchor=CENTER)

    label52 = Label(
        text="1) Αλλεργιογόνες ουσίες: Γλουτένη,σόγια,αυγό.\n2) Θερμίδες Aνα 100γρα. :295kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label52.place(x=20, y=320)

    photo_kotom = PhotoImage(file="κοτμπουκια.png")
    label53 = Label(root, image=photo_kotom)
    label53.place(x=700, y=250)

    back32 = Button(text="Πίσω", command=back_at_start32)
    back32.place(x=550, y=700)

#παρουσιαση φαγητου κοτοπουλο
def sunday_food2():
    clear_window_9()

    global photo_koto
    global back33
    global canv29
    global label54
    global label55

    canv29 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv29.place(relx=0.5, rely=0.5, anchor=CENTER)

    label54 = Label(
        text="1) Αλλεργιογόνες ουσίες: Σινάπι.\n2) Θερμίδες Aνα 100γρα. :209kcal.\n3) Υδατάνθρακες: 0g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label54.place(x=20, y=320)

    photo_koto = PhotoImage(file="Κοτοπουλο_μπουτι.png")
    label55 = Label(root, image=photo_koto)
    label55.place(x=700, y=250)

    back33 = Button(text="Πίσω", command=back_at_start33)
    back33.place(x=550, y=700)


#παρουσιαση φαγητου keftedakia
def sunday_food3():
    clear_window_9()

    global photo_kef
    global back34
    global canv30
    global label56
    global label57

    canv30 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv30.place(relx=0.5, rely=0.5, anchor=CENTER)

    label56 = Label(
        text="1) Αλλεργιογόνες ουσίες: Γλουτένη.\n2) Θερμίδες Aνα 100γρα. :208kcal.\n3) Υδατάνθρακες: 6,5g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label56.place(x=20, y=320)

    photo_kef = PhotoImage(file="Mpifteki.png")
    label57 = Label(root, image=photo_kef)
    label57.place(x=700, y=250)

    back34 = Button(text="Πίσω", command=back_at_start34)
    back34.place(x=550, y=700)

#παρουσιαση φαγητου spageti
def sunday_food4():
    clear_window_9()

    global photo_spa
    global back35
    global canv31
    global label58
    global label59

    canv31 = Canvas(height=400, width=1200, bg="LightCyan3")
    canv31.place(relx=0.5, rely=0.5, anchor=CENTER)

    label58 = Label(
        text="1) Αλλεργιογόνες ουσίες: Γλουτένη.\n2) Θερμίδες Aνα 100γρα. :208kcal.\n3) Υδατάνθρακες: 6,5g.\n4) Συνοδεύεται απο ψωμί και σαλάτα. ",
        font="Bold 18", background='LightCyan3')
    label58.place(x=20, y=320)

    photo_spa = PhotoImage(file="spaggeti.png")
    label59 = Label(root, image=photo_spa)
    label59.place(x=700, y=280)

    back35 = Button(text="Πίσω", command=back_at_start35)
    back35.place(x=550, y=700)


#καθαριζει την οθονη απο το κουμπι γισ της ημερες
def clear_window_1():
    label2.destroy()
    canv.destroy()
    button2.destroy()
    button1.destroy()
    page2()

#καθαριζει την οθονη απο το κουμπι για τα αγαπημενα
def clear_window_2():
    label2.destroy()
    canv.destroy()
    button2.destroy()
    button1.destroy()

    global canv32
    global label60
    global back36

    canv32 = Canvas(height=300, width=520, bg = "LightCyan3")
    canv32.place(relx=0.5,rely=0.5,anchor=CENTER)

    label60 = Label(text= "Αυτη η εφαρμογή έχει σκοπό να παρουσιάσει οπτικά ολα τα\nμεσημεριανά φαγητά που προσφέρονται "
                          "απο την λέσχη.\nΟι πληροφορίες που δίνονται (υδατάνθρακες,θερμίδες)\nμπορει να διαφερουν απο"
                          " την πραγματικότητα.Στην εφαρμογή \nπαρουσιάζονται τα φαγητά οπου εγκρίθηκαν απο την \nφοιτητική"
                          " μέριμνα.Αν το πρόγραμμα φαγητου αλλάξει \nτοτε η εταιρία ΧΟΥΤΟΣ και η φοιτητική μέριμνα ηρθαν"
                          " σε νέα συμφωνία. \nΑυτη η εφαρμογή δεν θα ενημερωθεί αν αυτο συμβει.    "
                            ,font="Bold 10",background='LightCyan3')
    label60.place(x=360,y=300)

    back36 = Button(text="Δες τα φαγητά",command=clear_window_10)
    back36.place(x=530,y=500)

#καθαριζει την οθονη απο το μενου της τριτης
def clear_window_3():
    canv3.destroy()
    label4.destroy()
    button10.destroy()
    button11.destroy()
    button12.destroy()
    button13.destroy()
    back2.destroy()

#καθαριζει την οθονη απο το μενου της Πεμπτης
def clear_window_4():
    canv3.destroy()
    label4.destroy()
    button22.destroy()
    button23.destroy()
    button24.destroy()
    button25.destroy()
    back4.destroy()

# καθαριζει την οθονη σπο το μενου της Δευτερας
def clear_window_5():
    canv3.destroy()
    label4.destroy()
    button18.destroy()
    button19.destroy()
    button20.destroy()
    button21.destroy()
    back1.destroy()

# καθαριζει την οθονη σπο το μενου της Δευτερας
def clear_window_6():
    canv3.destroy()
    label4.destroy()
    button14.destroy()
    button15.destroy()
    button16.destroy()
    button17.destroy()
    back3.destroy()

# καθαριζει την οθονη σπο το μενου του Σαββατου
def clear_window_7():
    canv3.destroy()
    label4.destroy()
    button30.destroy()
    button31.destroy()
    button32.destroy()
    button33.destroy()
    back6.destroy()

# καθαριζει την οθονη απο το μενου της Παρασκευης
def clear_window_8():
    canv3.destroy()
    label4.destroy()
    button26.destroy()
    button27.destroy()
    button28.destroy()
    button29.destroy()
    back5.destroy()

# καθαριζει την οθονη απο το μενου της Κυριακης
def clear_window_9():
    canv3.destroy()
    label4.destroy()
    button34.destroy()
    button35.destroy()
    button36.destroy()
    button37.destroy()
    back7.destroy()

def clear_window_10():
    canv32.destroy()
    label60.destroy()
    back36.destroy()
    start()


#συναρτηση για αρχικη σελιδα
def start():
    global canv
    global label2
    global button1
    global button2
    canv = Canvas(height=270, width=380, bg="LightCyan3")
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    label2 = Label(text="Καλώς Ηρθατε!", font="Bold 20", background='LightCyan3')
    label2.place(x=490, y=300)
    button1 = Button(text="Δες όλα τα φαγητά της εβδομάδας" ,command=clear_window_1)
    button1.place(x=470, y=350)
    button2 = Button(text="       Διαβάστε πριν την χρήση        ", command=clear_window_2)
    button2.place(x=470, y=390)

#αν ο χρηστης πατησει το κουμπι πισω απο την Δευτερα
def back_at_start1():
    canv3.destroy()
    label4.destroy()
    button18.destroy()
    button19.destroy()
    button20.destroy()
    button21.destroy()
    back1.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο την Τριτη
def back_at_start2():
    canv3.destroy()
    label4.destroy()
    button10.destroy()
    button11.destroy()
    button12.destroy()
    button13.destroy()
    back2.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο την Τεταρτη
def back_at_start3():
    canv3.destroy()
    label4.destroy()
    button14.destroy()
    button15.destroy()
    button16.destroy()
    button17.destroy()
    back3.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο την Πεμπτη
def back_at_start4():
    canv3.destroy()
    label4.destroy()
    button22.destroy()
    button23.destroy()
    button24.destroy()
    button25.destroy()
    back4.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο την Παρασκευη
def back_at_start5():
    canv3.destroy()
    label4.destroy()
    button26.destroy()
    button27.destroy()
    button28.destroy()
    button29.destroy()
    back5.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο το Σαββατο
def back_at_start6():
    canv3.destroy()
    label4.destroy()
    button30.destroy()
    button31.destroy()
    button32.destroy()
    button33.destroy()
    back6.destroy()
    start()

#αν ο χρηστης πατησει το κουμπι πισω απο την Κυριακη
def back_at_start7():
    canv3.destroy()
    label4.destroy()
    button34.destroy()
    button35.destroy()
    button36.destroy()
    button37.destroy()
    back7.destroy()
    start()

#αν ο χρηστης πατησει το πισω απο το φαγητο μπριζολα
def back_at_start8():
    label6.destroy()
    canv4.destroy()
    back8.destroy()
    label5.destroy()
    start()

#an ο χρηστης πατησει το πισω απο το φαγητο τηγανια
def back_at_start9():
    label7.destroy()
    canv5.destroy()
    back9.destroy()
    label8.destroy()
    start()

# αν ο χρηστης πατησει το πισω απο το φαγητο αλα κρεμ
def back_at_start10():
    label9.destroy()
    label10.destroy()
    canv6.destroy()
    back10.destroy()
    start()

#αν ο χρηστης πατησει το πισω απο το φαγητο φαλαφελ
def back_at_start11():
    label11.destroy()
    label12.destroy()
    canv7.destroy()
    back11.destroy()
    start()

#αν ο χρηστης pατησει το πισω απο το φαγητο μπιφτεκι
def back_at_start12():
    label13.destroy()
    label14.destroy()
    canv8.destroy()
    back12.destroy()
    start()

#Αν ο χρηστης πατησει το πισω απο το φαγητο κοτοπουλο_μπουτι
def back_at_start13():
    label14.destroy()
    label15.destroy()
    canv9.destroy()
    back13.destroy()
    start()

# αν ο χρηστης πατησει το πισω απο το φαγητο κοτομπουκιες
def back_at_start14():
    label16.destroy()
    label17.destroy()
    canv10.destroy()
    back14.destroy()
    start()

# αν ο χρηστης πατησει το πισω απο το φαγητο κοπανακι
def back_at_start15():
    label18.destroy()
    label19.destroy()
    canv11.destroy()
    back15.destroy()
    start()

# an o xristis pathsei piso apo tiw psarokroketes
def back_at_start16():
    label20.destroy()
    label21.destroy()
    canv12.destroy()
    back16.destroy()
    start()

# an o xristis pathsei piso apo tin perka
def back_at_start17():
    label22.destroy()
    label23.destroy()
    canv13.destroy()
    back17.destroy()
    start()

# an o xristis pathsei piso apo tin ριζοτο
def back_at_start18():
    label24.destroy()
    label25.destroy()
    canv14.destroy()
    back18.destroy()
    start()

# an o xristis pathsei piso apo ton mpakaliaro
def back_at_start19():
    label26.destroy()
    label27.destroy()
    canv15.destroy()
    back19.destroy()
    start()

# an o xristis pathsei piso apo fakes
def back_at_start20():
    label28.destroy()
    label29.destroy()
    canv16.destroy()
    back20.destroy()
    start()

# an o xristis pathsei piso apo refithia
def back_at_start21():
    label30.destroy()
    label31.destroy()
    canv17.destroy()
    back21.destroy()
    start()

# an o xristis pathsei piso apo fasolada
def back_at_start22():
    label32.destroy()
    label33.destroy()
    canv18.destroy()
    back22.destroy()
    start()

# an o xristis pathsei piso apo gigantes
def back_at_start23():
    label34.destroy()
    label35.destroy()
    canv19.destroy()
    back23.destroy()
    start()

# an o xristis pathsei piso apo tortelinia
def back_at_start24():
    label36.destroy()
    label37.destroy()
    canv20.destroy()
    back24.destroy()
    start()

# an o xristis pathsei piso apo kokkinisto
def back_at_start25():
    label38.destroy()
    label39.destroy()
    canv21.destroy()
    back25.destroy()
    start()

# an o xristis pathsei piso apo lemonato
def back_at_start26():
    label40.destroy()
    label41.destroy()
    canv22.destroy()
    back26.destroy()
    start()

# an o xristis pathsei piso apo snitsel
def back_at_start27():
    label42.destroy()
    label43.destroy()
    canv23.destroy()
    back27.destroy()
    start()

# an o xristis pathsei piso apo soutzoykakia
def back_at_start28():
    label44.destroy()
    label45.destroy()
    canv24.destroy()
    back28.destroy()
    start()

# an o xristis pathsei piso apo keftedaakia
def back_at_start29():
    label46.destroy()
    label47.destroy()
    canv25.destroy()
    back29.destroy()
    start()

# an o xristis pathsei piso apo gigantes paraskeyis
def back_at_start30():
    label48.destroy()
    label49.destroy()
    canv26.destroy()
    back30.destroy()
    start()

# an o xristis pathsei piso apo pastitsio
def back_at_start31():
    label50.destroy()
    label51.destroy()
    canv27.destroy()
    back31.destroy()
    start()

# an o xristis pathsei piso apo kotompoykies
def back_at_start32():
    label52.destroy()
    label53.destroy()
    canv28.destroy()
    back32.destroy()
    start()

# an o xristis pathsei piso apo kotopoulo
def back_at_start33():
    label54.destroy()
    label55.destroy()
    canv29.destroy()
    back33.destroy()
    start()

# an o xristis pathsei piso apo kefteadakia
def back_at_start34():
    label56.destroy()
    label57.destroy()
    canv30.destroy()
    back34.destroy()
    start()

# an o xristis pathsei piso apo s[aggeti
def back_at_start35():
    label58.destroy()
    label59.destroy()
    canv31.destroy()
    back35.destroy()
    start()

# Η συναρτηση για την Δευτερα
def b3():
    destruction()
    global canv3
    global label4
    global button18
    global button19
    global button20
    global button21
    global back1

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button18 = Button(text="Ψαροκροκέτες",command=monday_food1)
    button18.place(x=470, y=370)

    button19 = Button(text="Μπακαλίαρος",command=monday_food4)
    button19.place(x=610, y=370)

    button20 = Button(text="  Πέρκα   ",command=monday_food2)
    button20.place(x=470, y=415)

    button21 = Button(text="Ριζότο",command=monday_food3)
    button21.place(x=610, y=415)

    back1 = Button(text="Πίσω", command=back_at_start1)
    back1.place(x=540, y=470)


# // για την Τριτη
def b4():
    destruction()
    global canv3
    global label4
    global button10
    global button11
    global button12
    global button13
    global back2

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button10 = Button(root,text="Μπριζόλες",command= tuesday_food1)
    button10.place(x=470, y=370)

    button11 = Button(text="Τηγανία",command=tuesday_food2)
    button11.place(x=610, y=370)

    button12 = Button(text="Aλα Κρεμ",command=tuesday_food3)
    button12.place(x=470, y=415)

    button13 = Button(text="Φαλάφελ",command=tuesday_food4)
    button13.place(x=610, y=415)

    back2 = Button(text="Πίσω", command=back_at_start2)
    back2.place(x=540, y=470)

# //  για την Τεταρτη
def b5():
    destruction()
    global canv3
    global label4
    global button14
    global button15
    global button16
    global button17
    global back3

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button14 = Button(text="Φακές :(",command=wensday_food1)
    button14.place(x=470, y=370)

    button15 = Button(text="Ρεβύθια ",command=wensday_food2)
    button15.place(x=610, y=370)

    button16 = Button(text="Φασολάδα ",command=wensday_food3)
    button16.place(x=470, y=415)

    button17 = Button(text="Γίγαντες",command=wensday_food4)
    button17.place(x=610, y=415)

    back3 = Button(text="Πίσω", command=back_at_start3)
    back3.place(x=540, y=470)

# // για την Πεμπτη
def b6():
    destruction()
    global canv3
    global label4
    global button22
    global button23
    global button24
    global button25
    global back4

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button22 = Button(text="Κοτομπουκίες",command=thursday_food3)
    button22.place(x=450, y=370)

    button23 = Button(text="Κοτόπουλο Μπούτι",command=thursday_food2)
    button23.place(x=590, y=370)

    button24 = Button(text="Μπιφτέκι ",command=thurday_food1)
    button24.place(x=450, y=415)

    button25 = Button(text="Κοπανάκι Κοτόπουλου",command=thursday_food4)
    button25.place(x=590, y=415)

    back4 = Button(text="Πίσω", command=back_at_start4)
    back4.place(x=540, y=470)

# // για την Παρασκευη
def b7():
    destruction()
    global canv3
    global label4
    global button26
    global button27
    global button28
    global button29
    global back5

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button26 = Button(text="Σουτζουκάκια",command=friday_food1)
    button26.place(x=470, y=370)

    button27 = Button(text="Παστίτσιο :)",command=friday_food4)
    button27.place(x=610, y=370)

    button28 = Button(text="Κεφτεδάκια ",command=friday_food2)
    button28.place(x=470, y=415)

    button29 = Button(text="Γίγαντες  ",command=friday_food3)
    button29.place(x=610, y=415)

    back5 = Button(text="Πίσω", command=back_at_start5)
    back5.place(x=540, y=470)


# // για το Σαββατο
def b8():
    destruction()
    global canv3
    global label4
    global button30
    global button31
    global button32
    global button33
    global back6

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button30 = Button(text="Κρέας λεμονάτο",command=saturday_food3)
    button30.place(x=450, y=370)

    button31 = Button(text="Κρέας Κοκκινιστό",command=saturday_food2)
    button31.place(x=610, y=370)

    button32 = Button(text="   Τορτελίνια   ",command=saturday_food1)
    button32.place(x=450, y=415)

    button33 = Button(text="   Σνίτζελ        ",command=saturday_food4)
    button33.place(x=610, y=415)

    back6 = Button(text="Πίσω", command=back_at_start6)
    back6.place(x=540, y=470)

# // για την Κυριακη
def b9():
    destruction()
    global canv3
    global label4
    global button34
    global button35
    global button36
    global button37
    global back7

    canv3 = Canvas(height=225, width=380, bg="LightCyan3")
    canv3.place(relx=0.5, rely=0.5, anchor=CENTER)

    label4 = Label(text="Επίλεξε φαγητό", font="Bold 20", background='LightCyan3')
    label4.place(x=500, y=320)

    button34 = Button(text="Σπαγγέτι",command= sunday_food4)
    button34.place(x=470, y=370)

    button35 = Button(text="Κοτόπουλο",command = sunday_food2)
    button35.place(x=470, y=415)

    button36 = Button(text="Μπηφτέκακια", command= sunday_food3)
    button36.place(x=610, y=370)

    button37 = Button(text="Κοτομπουκίες", command = sunday_food1)
    button37.place(x=610, y=415)

    back7 = Button(text="Πίσω", command=back_at_start7)
    back7.place(x=540, y=470)

# καθαριζει την οθονη για την επομενη σελιδα
def destruction():
    canv2.destroy()
    label3.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()

#εμφανιζει της μερες της εβδομαδας
def page2():
    global canv2
    global label3
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9

    canv2=Canvas(height=270, width=380, bg="LightCyan3")
    canv2.place(relx=0.5, rely=0.5, anchor=CENTER)

    label3 = Label(text="Διάλεξε μέρα", font="Bold 20", background='LightCyan3')
    label3.place(x=515, y=300)

    button3 = Button(text="Δευτέρα", command=b3)
    button3.place(x=470, y=350)

    button4 = Button(text="Τρίτη", command=b4)
    button4.place(x=610, y=350)

    button5 = Button(text="Τετάρτη", command=b5)
    button5.place(x=470, y=395)

    button6 = Button(text="Πέμπτη", command=b6)
    button6.place(x=610, y=395)

    button7 = Button(text="Παρασκευή", command=b7)
    button7.place(x=470, y=440)

    button8 = Button(text="Σάββατο", command=b8)
    button8.place(x=610, y=440)

    button9 = Button(text="Κυριακή", command=b9)
    button9.place(x=540, y=485)


# ανοιγμα του παραθυρου
root = Tk()

#βαζει τιτλο
root.title("Πρόγραμμα Λέσχης")

root.geometry("1200x856")

#lock the deminsions of the window
root.resizable(width=False, height=False)

#put logo icon
photo = PhotoImage(file = "C:/Users/user/Downloads/9f596769-790d-4b5f-bb80-668016a9c920.png")
root.iconphoto(False, photo)

# put image file
bg = PhotoImage(file="C:/Users/user/Downloads/background-images-for-login-page3bc68c53b0db224b.png")
# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

#αρχιζει το προγραμμα
start()

#στυλ για τα κουμπια
style = Style()
style.configure('TButton', font=
('calibri'),  borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'blue')],
          background=[('active', 'black')])

# Execute tkinter
root.mainloop()
