def print_(obj):
    print(obj, end='\t')
#fb_list = ['fizzbuzz' if i%15==0 else 'fizz' if i%3==0  else 'buzz' if i%5==0 else  i for i in range(1,300+1)]

#<<<<<<< HEAD
for i in range(1,300+1):
    if i%3==0:
    if i%15==0:
        print_('fizzbuzz')
    elif i%3==0:
        print_('fizz')
    elif i%5==0:
        print_('buzz')
#=======
#print(fb_list)
#>>>>>>> fb-listcomp
