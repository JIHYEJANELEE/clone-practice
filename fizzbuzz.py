def print_(obj):
    print(obj, end='\t')

for i in range(1,300+1):
    if i%3==0:
    if i%15==0:
        print_('fizzbuzz')
    elif i%3==0:
        print_('fizz')
    elif i%5==0:
        print_('buzz')
