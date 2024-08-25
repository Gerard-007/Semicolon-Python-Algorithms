'''
'''


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

                            match phonebook_option_menu:
                
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
            back_to_main = False
            while not back_to_main:
                call_register_menu = """
                Call Register
                1 -> Missed calls
                2 -> Received calls
                3 -> Dialled numbers
                4 -> Erase recent call lists
                5 -> Show call duration
                6 -> Show call costs
                7 -> Call cost settings
                8 -> Prepaid credit
                0 -> Back
                >> """
                call_register_menu_option = int(input(call_register_menu))

                match call_register_menu_option:
                    case 0:
                        back_to_main = True
                        break

                    case 1:
                        print("Missed calls")

                    case 2:
                        print("Received calls")

                    case 3:
                        print("Dialled numbers")

                    case 4:
                        print("Erase recent call lists")

                    case 5:
                        print("Show call duration")

                    case 6:
                        print("Show call costs")

                    case 7:
                        print("Call cost settings")

                    case 8:
                        print("Prepaid credit")
            
        case 5:
            back_to_main = False
            while not back_to_main:
                tone_menu = """
                Tone
                1 -> Ringing tone
                2 -> Ringing volume
                3 -> Incoming call alert
                4 -> Composer
                5 -> Message alert tone
                6 -> Keypad tones
                7 -> Warning and game tones
                8 -> Vibrating alert
                9 -> Screen saver
                0 -> Back
                >> """
                tone_menu_option = int(input(tone_menu))

                match tone_menu_option:
                    case 0:
                        back_to_main = True
                        break

                    case 1:
                        print("Ringing tone")

                    case 2:
                        print("Ringing volume")

                    case 3:
                        print("Incoming call alert")

                    case 4:
                        print("Composer")

                    case 5:
                        print("Message alert tone")

                    case 6:
                        print("Keypad tones")

                    case 7:
                        print("Warning and game tones")

                    case 8:
                        print("Vibrating alert")

                    case 9:
                        print("Screen saver")
            
        case 6:
            back_to_main = False
            while not back_to_main:
                settings_menu = """
                Settings
                1 -> Call settings
                2 -> Phone settings
                3 -> Security settings
                4 -> Restore factory settings
                0 -> Back
                >> """
                settings_menu_option = int(input(settings_menu))

                match settings_menu_option:
                    case 0:
                        back_to_main = True
                        break

                    case 1:
                        print("Call settings")

                    case 2:
                        print("Phone settings")

                    case 3:
                        print("Security settings")

                    case 4:
                        print("Restore factory settings")
            
        case 7:
            print("Call divert")
            
        case 8:
            print("Games")
            
        case 9:
            print("Calculator")
            
        case 10:
            print("Reminder")
            
        case 11:
            back_to_main = False
            while not back_to_main:
                clock_menu = """
                Clock
                1 -> Alarm clock
                2 -> Clock settings
                3 -> Date setting
                4 -> Stopwatch
                5 -> Countdown timer
                6 -> Auto update of date and time
                0 -> Back
                >> """
                clock_menu_option = int(input(clock_menu))

                match clock_menu_option:
                    case 0:
                        back_to_main = True
                        break

                    case 1:
                        print("Alarm clock")

                    case 2:
                        print("Clock settings")

                    case 3:
                        print("Date setting")

                    case 4:
                        print("Stopwatch")

                    case 5:
                        print("Countdown timer")

                    case 6:
                        print("Auto update of date and time")
            
        case 12:
            print("Profiles")
            
        case 13:
            print("SIM services")
