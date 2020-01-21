from django.shortcuts import render, get_object_or_404, redirect
from .models import Letter, Myhit, Mywrite
from .forms import LetterForm, CommentForm
import datetime
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html', {'dialog':False, 'dialogwrite':False})


def showlist(request):
    letters = Letter.objects.filter(writer=request.user)
    return render(request, 'myapp/showlist.html', {'letters' : letters})

    
def detail(request, letter_id):
    letter_detail = get_object_or_404(Letter, pk = letter_id) 
    mine = False
    if letter_detail.writer == request.user:
        mine = True
    return render(request, 'myapp/detail.html', {'letter':letter_detail, 'mine':mine})

def write(request):
    return render(request, 'myapp/write.html')

def reply(request):
    return render(request, 'myapp/reply.html')

def intro(request):
    return render(request, 'myapp/intro.html')

def lettercreate(request):
    if request.method =='POST': # POST 방식으로 요청이 들어왔을 때
        form = LetterForm(request.POST) # 입력된 내용들을 form이라는 변수에 저장
        if form.is_valid(): # form이 유효하다면(models.py에서 정의한 필드에 적합하다면)
            letter = form.save(commit=False) # form 데이터를 가져온다.
            letter.writer = request.user
            letter.save() # form 데이터를 DB에 저장한다.
            return render(request, 'myapp/home.html', {'dialog':False, 'dialogwrite':True})
    else: # GET 방식으로 요청이 들어왔을 때
        d = datetime.date.today()
        dialogwrite = False
        try:
            mywrite = Mywrite.objects.get(user=request.user)
        except: 
            mywrite = Mywrite(user=request.user, writecount=0, date="0000-00-00 00:00:00")
        date = str(mywrite.date)
        today = d.isoformat() + " 00:00:00"
        if date==today:
            if mywrite.writecount == 1:
                dialogwrite = True
                return render(request, 'myapp/home.html', {'dialog': False , 'dialogwrite':dialogwrite})
            else:
                mywrite.writecount = mywrite.writecount + 1
        else:
            mywrite.date = today
            mywrite.writecount = 1
        mywrite.save()
        form = LetterForm()
        return render(request,'myapp/write.html', {'form': form})


def letterupdate(request, letter_id):
    letter = get_object_or_404(Letter, pk = letter_id)
    if request.method == 'POST':
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.save()
            return redirect('detail', letter_id=letter.pk) # 수정한 글의 상세 페이지로 돌아간다
    else:
        form = LetterForm(instance=letter) # post 객체에 이미 저장돼있는 것들을 form에 띄워둠
        return render(request, 'myapp/edit.html', {'form': form})


def letterdelete(request, letter_id):
    letter = get_object_or_404(Letter, pk = letter_id)
    letter.delete() # Post DB에서 post 객체 삭제
    return redirect('showlist')

def commentcreate(request, letter_id):
    letter = get_object_or_404(Letter, pk=letter_id)
    mine = False
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.letter = letter
            comment.save()
            return render(request, 'myapp/home.html', {'dialog':False, 'dialogwrite':False})
        else:
            redirect('showlist')
    else:
        form = CommentForm()
        return render(request, 'myapp/detail.html', {'form': form, 'letter': letter, 'mine':mine})

def getrandom(request):
    d = datetime.date.today()
    try: #지금 로그인한 유저가 다른사람의 글을 조회한적이 있다면
        #해당 유저의 조회회수 객체 호출
        myhit = Myhit.objects.get(hitter=request.user)
    except: #지금 로그인한 유저가 다른사람의 글을 조회한적이 없으면
        #조회횟수 데이터 객체 생성
        myhit = Myhit(hitter=request.user, hit=0, date="0000-00-00 00:00:00")
    #오늘날짜랑 같으면
    date = str(myhit.date)
    today = d.isoformat() + " 00:00:00"
    if date==today:
        #hit 3이면
        if myhit.hit == 3:
            #접근불가
            #다이얼로그 띄우기
            dialog = True
            return render(request, 'myapp/home.html', {'dialog':dialog, 'dialogwrite':False})
        #3미만이면
        else:
            #hit 1 증가
            myhit.hit = myhit.hit + 1
    #오늘날짜랑 다르면
    else:
        #오늘날짜 저장
        myhit.date = today
        #hit 1으로 초기화
        myhit.hit = 1
    myhit.save()
    letter = Letter.objects.order_by("?").first()
    letter.update_counter
    mine = False
    while letter.writer == request.user:
        letter = Letter.objects.order_by("?").first()
    return render(request, 'myapp/detail.html', {'letter': letter, 'mine':mine, 'date':date, 'today':today})