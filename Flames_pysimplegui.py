import re
import PySimpleGUI as pg
pg.theme("NeutralBlue")
layout = [    [pg.Text("Enter Name 1 :", size = (15,1), key= "name1"), pg.InputText()],
    [pg.Text("Enter Name 2 :", size = (15,1), key= "name2"), pg.InputText()],
    [pg.Text("Result : ")],
    [pg.Text((""), key = "OP")],
    [pg.Button("Ok"), pg.Button("Reset"), pg.Button("Cancel")]]
window = pg.Window("FLAMES", layout)
while True:
    event, values = window.read()
    if event == "Cancel" or event ==pg.WIN_CLOSED:
        break
    if event == "Reset":
        for key in values:
            window[0].update('')
            window[1].update('')
    if event == "Ok":
        p1 = str(values[0])
        p2 = str(values[1])
        #print (p1, p2)
        def remove_same_chars(list1, list2):
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        c = list1[i]
                        list1.remove(c)
                        list2.remove(c)
                        list3 = list1 + ["*"] + list2
                        return [list3, True]
            list3 = list1 + ["*"] + list2
            return [list3, False]
        if __name__ == "__main__":
            c, d = 0, 0
            p1 = p1.lower()
            p1 = p1.replace(" ", "")
            if(p1.isalpha()) == True:
                c += 1
            p1_list = list(p1)
            p2 = p2.lower()
            p2 = p2.replace(" ", "")
            if(p2.isalpha()) == True:
                d += 1
            p2_list = list(p2)
            proceed = True
            while proceed:
                ret_list = remove_same_chars(p1_list, p2_list)
                con_list = ret_list[0]
                proceed = ret_list[1]
                star_index = con_list.index("*")
                p1_list = con_list[: star_index]
                p2_list = con_list[star_index + 1:]
            count = len(p1_list) + len(p2_list)
            if count == 0 or (c == 0 or d == 0):
                window["OP"].update("Enter valid inputs")
            else:
                result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
                while len(result) > 1:
                    split_index = (count % len(result) - 1)
                    if split_index >= 0:
                        right = result[split_index + 1:]
                        left = result[: split_index]
                        result = right + left
                    else: 
                        result = result[: len(result) - 1]
                a = (result[0])
                window["OP"].update(a)
window.close()