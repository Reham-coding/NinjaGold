
from django.shortcuts import render, HttpResponse, redirect
from random import randint
from datetime import datetime
def index(request):
    
    request.session.setdefault('total_gold',0)
    request.session.setdefault('activities',[])
    return render(request,'index.html')
         
def goldCal(request, which_form):
    which_form = {
            'farm': randint(10, 20),
            'cave': randint(5, 10),
            'house': randint(2, 5),
            'casino': randint(-50, 50)
        }

    gold = which_form[request.POST['which_form']]
    print('gold is: ' + str(gold))
    request.session['total_gold'] += gold

    time = '{:%Y/%m/%d %I:%M %p}'.format(datetime.now())
    if gold > 0:
        # gained money
        print(time)
        result = f"Earned {gold} from the {request.POST['which_form']}! ({time})"
        earned = 'text-success'
        print(result)
    else:
        # loss money
        result = f"Enter a casino and lost {abs(gold)} gold....ouch... ({time})"
        earned = 'text-danger'
    request.session['activities'].append({'earned':earned, 'activity': result})

    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect('/')