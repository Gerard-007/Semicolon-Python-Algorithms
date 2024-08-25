while True:
    main_menu = """
        Welcome to Nokia 3310
        Please select the below menu to start...
        1 -> Phone Book
        2 -> Messages
        3 -> Chat
        4 -> Call register
        5 -> Tone
        6 -> Settings
        7 -> Call divert
        8 -> Games
        9 -> Calculator
        10 -> Reminder
        11 -> Clock
        12 -> Profiles
        13 -> SIM services
        0 -> Exit
        >> """
    main_menu_option = int(input(main_menu))
        
    if main_menu_option == 0:
        print("Exiting... Goodbye!")
        break
    
    match main_menu_option:
        
        case 1:
            back_to_main = False
            while not back_to_main:
                phonebook_menu = """
                    Phone Book
                    1 -> Search
                    2 -> Service Nos.
                    3 -> Add name
                    4 -> Erase
                    5 -> Edit
                    6 -> Assign tone
                    7 -> Send b'card
                    8 -> Options
                    9 -> Speed dials
                    10 -> Voice tags
                    0 -> Back
                    >> """
                phonebook_menu_option = int(input(phonebook_menu))

                match phonebook_menu_option:
                
                    case 0:
                        back_to_main = True
                        break
                    
                    case 1:
                        print("Search")
                
                    case 2:
                        print("Service Nos.")
                
                    case 3:
                        print("Add name")
                
                    case 4:
                        print("Erase")
                
                    case 5:
                        print("Edit")
                
                    case 6:
                        print("Assign tone")
                
                    case 7:
                        print("Send b'card")
                
                    case 8:
                        back_to_phonebook_menu = False

                        while not back_to_phonebook_menu:
                            phonebook_option = """
                                Phone Book > Options
                                1 -> Type of view
                                2 -> Memory status
                                0 -> Back
                                >> """
                            phonebook_option_menu = int(input(phonebook_option))

                        match phonebook_menu_option:
                
                            case 0:
                                back_to_phonebook_menu = True
                                break

                            case 1:
                                print("Type of view")

                            case 2:
                                print("Memory status")
                
                    case 9:
                        print("Speed dials")
                
                    case 10:
                        print("Voice tags")
            
        case 2:
            back_to_main = False
            while not back_to_main:
                message_menu = """
                    Messages
                    1 -> Write Message
                    2 -> Inbox
                    3 -> Outbox
                    4 -> Picture Messages
                    5 -> Templates
                    6 -> Smileys
                    7 -> Message settings
                    8 -> Info service
                    9 -> Voice mailbox number
                    10 -> Service command editor
                    0 -> Back
                    >> """
                message_menu_option = int(input(message_menu))

                match message_menu_option:
                    case 0:
                        back_to_main = True
                        break

                    case 1:
                        print("Write Message")

                    case 2:
                        print("Inbox")

                    case 3:
                        print("Outbox")

                    case 4:
                        print("Picture Messages")

                    case 5:
                        print("Templates")

                    case 6:
                        print("Smileys")

                    case 7:
                        print("Message settings")

                    case 8:
                        print("Info service")

                    case 9:
                        print("Voice mailbox number")

                    case 10:
                        print("Service command editor")
            
        case 3:
            print("Chat")
            
        case 4:
            print("Call register")
            
        case 5:
            print("Tone")
            
        case 6:
            print("Settings")
            
        case 7:
            print("Call divert")
            
        case 8:
            print("Games")
            
        case 9:
            print("Calculator")
            
        case 10:
            print("Reminder")
            
        case 11:
            print("Clock")
            
        case 12:
            print("Profiles")
            
        case 13:
            print("SIM services")
