PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as mail:
    txt = mail.read()
    # print(txt)
    new_txt = txt.replace(PLACEHOLDER, "{}")
    # print(new_txt)
    with open("./Input/Names/invited_names.txt") as names:
        name = names.readlines()
        for name in name:
            # print(f"{name.strip()}")
            # print(new_txt.format(f"{name.strip()}"))
            with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", 'w') as letter:
                letter.write(new_txt.format(f"{name.strip()}"))







        # print(names.readlines())

        # new_names = []
        # for i in names:

            # new_names.append(i.split('\n')[0])
            # new_names.append(names.pop(i))

        # print(new_names)
        # names.readlines(i)


    # new_mail = txt.replace("[name]", "Angela" )


    # contents = mail.read()
    # print(contents)
    # print(type(contents))

    # contents.replce("[name]", f"{name}")


    # print(mail.readlines())

    # /Input/Letters/starting_letter.txt
    # main.py

    # txt = mail.readlines()




        # contents = names.read()
        # print(contents)
        # print(type(contents))
        # for

        # print(names.readlines())
        # print(type(names.readlines()))

        # len(names.readlines())
        # name_list = names.readlines()
        # print(name_list)

        # len(name_list)
        # name = [i.split(',') for i in name_list]
        # print(name)
        # print(name_list[1])

        # for i in name_list:
        #     print(i)
            # txt.replace("[name]", name)



