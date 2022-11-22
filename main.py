import CGE


def main():
    CGE.output(CGE.title)
    status = False
    while status is False:
        answer = CGE.menu_yon("Start a new game?")
        if answer == 1:
            status = CGE.new_save()
        if answer == 2:
            status = CGE.load_save()
    CGE.save()


if __name__ == '__main__':
    main()






