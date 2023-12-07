from django.shortcuts import render

# Create your views here.

def home(request):
    d={'author': 'Xenocide', 'age':40, 'guilds':['The ghost', 'Saints', 'Star Ocean'],
       'members':[
           {
               'IGN': 'Yakushi',
               'Joined': 'March',
               'Class': 'Gun'
           },
           {
               'IGN': 'Zepiro',
               'Joined': 'March',
               'Class': 'Two handed sword'
           },
           {
               'IGN': 'Fermion',
               'Joined': 'April',
               'Class': 'Halberd'
           },
       ]
       
       }
    return render(request,'home.html', d)