from django.shortcuts import render

def news_info(request):
    return render(request, 'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Info'
    sub_msg1 = 'Good Movie'
    sub_msg2 = 'Worst'
    sub_msg3 = 'Better'
    type = 'movies'
    my_dict ={'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
    return render(request, 'testapp/news.html', my_dict)

def sports_view(request):
    head_msg = 'Sports Info'
    sub_msg1 = 'dhoni'
    sub_msg2 = 'Ronaldo'
    sub_msg3 = 'Mccullum'
    type = 'sports'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
    return render(request, 'testapp/news.html', my_dict)

def politics_view(request):
    head_msg = 'Politics Info'
    sub_msg1 = 'Modi'
    sub_msg2 = 'KCR'
    sub_msg3= 'Trump'
    type = 'politics'
    my_dict = {'head_msg': head_msg, 'sub_msg1': sub_msg1, 'sub_msg2': sub_msg2, 'sub_msg3': sub_msg3,'type':type}
    return render(request, 'testapp/news.html', my_dict)