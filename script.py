def report_status(**kwargs):

    print('\nBEGIN: REPORT\n')

    for key, value in kwargs.items():
        print(key + ": " + value)
    
    print("\nEND REPORT")

report_status(name='luke', affiliation='jedi', status='missing')
