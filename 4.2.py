import queue

# Creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')
        # Add new file to the end of the queue
        files_to_print.put(file_name)
        print(f'File "{file_name}" added to the print queue.')

    elif menu == '2':
        if not files_to_print.empty():  # Check if the print queue is not empty
            file_to_print = files_to_print.get()
            print(f'File "{file_to_print}" is currently being printed. Please wait!')
        else:
            print('The print queue is empty. No files to print.')

    elif menu == '0':
        break

    else:
        print('Invalid option. Please try again.')

    print()  # Add a blank line for better readability
