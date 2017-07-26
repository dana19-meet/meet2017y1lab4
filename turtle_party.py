is_weekend=input('is it a weekend?')

if is_weekend=='no':
    strawberries=input('how much strwberries do you have?')
    if int(strawberries)>39 and int(strawberries)<61:
        print('fun')
    else:
        print('not fun')
if is_weekend=='yes':
    strawberries=input('how much strwberries do you have?')
    if int(strawberries)>39 :
        print('fun')
    else:
        print('not fun')
