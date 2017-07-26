speed=input('what was your speed?')
birthday= input('is it your birthday?')

if birthday=='no':
    if int(speed)<31:
        print('no ticket!')
    elif int(speed)>30 and int(speed)<51:
        print('small ticket!')
    elif int(speed)>50:
        print('big ticket')

else:
    if int(speed)<36:
        print('no ticket!')
    elif int(speed)>35 and int(speed)<56:
        print('small ticket!')
    elif int(speed)>55:
        print('big ticket')


    
    print('it is your birthday! on your birthday tour speed can be 5 higher in all cases!')
