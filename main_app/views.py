from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    finch_list = [
        {'id': 1, 'name': 'American Goldfinch', 'species': 'Spinus tristis', 'age': 2, 'sex': 'M'},
        {'id': 2, 'name': 'Common Chaffinch', 'species': 'Fringilla coelebs', 'age': 3, 'sex': 'F'},
        {'id': 3, 'name': 'Brambling', 'species': 'Fringilla montifringilla', 'age': 2, 'sex': 'F'},
        {'id': 4, 'name': 'Hawfinch', 'species': 'Coccothraustes coccothraustes', 'age': 1, 'sex': 'F'},
        {'id': 5, 'name': 'Pine Grosbeak', 'species': 'Pinicola enucleator', 'age': 2, 'sex': 'M'},
        {'id': 6, 'name': 'Eurasian Bullfinch', 'species': 'Pyrrhula pyrrhula', 'age': 2, 'sex': 'F'},
        {'id': 7, 'name': 'Azores Bullfinch', 'species': 'Pyrrhula murina', 'age': 3, 'sex': 'M'},
        {'id': 8, 'name': 'Evening Grosbeak', 'species': 'Hesperiphona vespertina', 'age': 5, 'sex': 'M'},
        {'id': 9, 'name': 'Gray-Crowned Rosy-Finch', 'species': 'Leucosticte tephrocotis', 'age': 2, 'sex': 'F'},
        {'id': 10, 'name': 'Black Rosy-Finch', 'species': 'Leucosticte atrata', 'age': 5, 'sex': 'F'},
    ]
    return render(request, 'index.html', {'finch_list': finch_list})