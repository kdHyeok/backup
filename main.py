from tkinter import * #GUI 실행을 위해 tkinter 불러오기
import tkinter.font as font
#import pyautogui

class Sc: #스케쥴러 정보
    Process = [] #프로세스 ID
    Arr_Time = [] #도착 시간
    Play_Time = [] #작업 시간
    Prio = [] #우선순위
    Time_Cut=3

def Rank_out(list): #리스트 정렬 후 index 출력
    rank=[]+ list #입력받은 리스트를 따로 저장, rank=list를 할 경우 rank의 원소를 변경했을때 list의 원소도 변견되서 다음같이 지정
    Rlist=[] #리스트의 순서를 변경했을 때 인덱스 순서도 변경하기 위해 인덱스를 저장할 변수
    for a in range(len(list)):
        Rlist.append(a) #리스트의 길이만큼 인덱스 저장
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            if rank[x]>rank[y]:
                rank.insert(x,rank[y]) #앞에있는 원소와 뒤에 있는 원소를 비교, 뒷 원소가 작으면 뒷 원소를 앞원소 위치에 추가
                del rank[y+1] # 뒷원소가 앞에 하나 더 추가됐으므로 기존 원소 제거
                Rlist.insert(x, Rlist[y])
                del Rlist[y + 1] #인덱스 값 또한 같은 방식으로 추가,제거
    return Rlist #리스트의 오름차순으로 인덱스값 반환

#-------------------------------------------------------------------------------------------------------------------(FCFS

def FCFS(pr,at,pt): #FCFS 알고리즘(ID,도착시간,작업시간)
    Start=Rank_out(at) # 도착시간 순으로 인덱스 정렬
    a = 0 # '->' 문자 출력을 위한 카운트 변수
    Dsum = 0 # 총 소요시간
    Dtime = []+at #대기시간, 원소를 바꾸기 전에 인덱스 개수을 프로세스 개수만큼 초기화
    print('=============(FCFS)============')
    print('실행 순서 : ',end='') #파이썬은 출력 끝에 \n이 기본값으로 붙어서 end=''를 통해 \n을 제거
    ttext1.insert('end','[실행 순서] : ') #print 내용과 똑같게 텍스트 상자에 입력

    for i in Start: #정렬된 인덱스값들을 순서대로 i에 저장,반복
        if Dsum < at[i]:
            Dsum = at[i] #총 대기시간이 도착시간보다 작으면 대기시간에 도착 시간을 추가
        print(f'{pr[i]}',end='') #도착시간 순으로 실행된 프로세스ID출력
        ttext1.insert('end', f'{pr[i]}')  #print 내용과 똑같게 텍스트 상자에 입력
        Dtime[i]=Dsum-at[i] #해당 프로세스의 대기시간=총대기시간-도착시간
        Dsum += pt[i] #총 대기시간에 작업시간 추가
        if a < len(Start)-1:
            a += 1 #맨 뒤에는 화살표가 입력되지 않도록 하는 카운트 변수
            print(' -> ',end='') #맨끝에는 '->'문자열이 추가되지 않도록 (전체길이-1)만큼 카운트 후 출력
            ttext1.insert('end', ' => ')  #print 내용과 똑같게 텍스트 상자에 입력
    print('\n')#줄바꿈
    ttext1.insert('end','\n\n') #print 내용과 똑같게 텍스트 상자에 입력

    for i in range(len(pr)):
        print(f'{pr[i]} 대기시간: {Dtime[i]} 초') #순서대로 프로세스의 대기시간 출력
        ttext1.insert('end', f'[{pr[i]} 대기시간] : {Dtime[i]} 초\n')  #print 내용과 똑같게 텍스트 상자에 입력

    print(f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n') #모든 프로세스의 대기시간의 합 / 프로세스 수
    ttext1.insert('end', f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n\n')  #print 내용과 똑같게 텍스트 상자에 입력

#-----------------------------------------------------------------------------------------------------------------------(SJF

def SJF(pr,at,pt): #SJF 알고리즘(ID,도착시간,작업시간)
    srt = Rank_out(at)# 도착시간 순으로 인덱스 정렬
    a = 0 # '->' 문자 출력을 위한 카운트 변수
    Dsum = 0 # 총 소요시간
    Dtime = []+at #대기시간, 원소를 바꾸기 전에 인덱스 개수을 프로세스 개수만큼 초기화
    print('=============(SJF)============')
    print('실행 순서 : ',end='')
    ttext2.insert('end', '[실행 순서] : ')
    print(f'{pr[srt[0]]} -> ', end='') #맨처음 도착한 프로세스는 바로 실행
    ttext2.insert('end', f'{pr[srt[0]]} => ')  #print 내용과 똑같게 텍스트 상자에 입력
    Dtime[srt[0]] = 0 #처음이므로 대기시간 0
    Dsum += at[srt[0]]+pt[srt[0]] #총 대기시간에 처음 도착한 프로세스의 도착,작업시간 추가
    Start = Rank_out(pt) # 작업시간이 짧은 순으로 인덱스 정렬
    Start.remove(srt[0]) #처음 도착한 프로세스의 인덱스값 제거
    for i in Start:

        if Dsum < at[i]:
            Dsum = at[i] #앞과 동일
        print(f'{pr[i]}',end='')
        ttext2.insert('end',f'{pr[i]}')
        Dtime[i]=Dsum-at[i] #앞과 동일
        Dsum += pt[i] #앞과 동일
        if a < len(Start)-1:
            a += 1
            print(' -> ',end='') #앞과 동일
            ttext2.insert('end', ' => ')  #print 내용과 똑같게 텍스트 상자에 입력
    print('\n')
    ttext2.insert('end', '\n\n')  #print 내용과 똑같게 텍스트 상자에 입력
    for i in range(len(pr)):
        print(f'{pr[i]} 대기시간: {Dtime[i]} 초') #앞과 동일
        ttext2.insert('end', f'[{pr[i]} 대기시간] : {Dtime[i]} 초\n')  #print 내용과 똑같게 텍스트 상자에 입력

    print(f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n') #앞과 동일
    ttext2.insert('end', f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n\n')  #print 내용과 똑같게 텍스트 상자에 입력

#--------------------------------------------------------------------------------------------------------------------(RR

def RR(pr,at,pt,cut): #RR 알고리즘(ID,도착시간,작업시간,타임슬라이스)
    Start=Rank_out(at) # 도착시간 순으로 인덱스 정렬
    Rpr = [] # 타임슬라이스대로 나뉜 프로세스의 목록을 저장할 리스트
    Rat = [] # 타임 슬라이스대로 나뉜 프로세스의 도착시간을 재 저장시킬 리스트 변수
    Rpt = [] # 실행 시간을 타임 슬라이스대로 나눠서 저장하기 위한 리스트 변수
    a = 0  # '->' 문자 출력을 위한 카운트 변수
    Dsum = 0  # 총 소요시간
    Dtime = []  # 대기시간

    print('=============(RR)============')
    print('실행 순서 : ',end='') #파이썬은 출력 끝에 \n이 기본값으로 붙어서 end=''를 통해 \n을 제거
    ttext3.insert('end', '[실행 순서] : ')  #print 내용과 똑같게 텍스트 상자에 입력
    for n in range(len(Start)):
        Rpr.append(pr[Start[n]])
        Rat.append(at[Start[n]])
        Rpt.append(pt[Start[n]])
    ii=0
    while ii < len(Rpr): #프로세스 순만큼 반복, for문으로는 중간에 프로세스가 늘어난만큼 반복이 진행되지 않기 때문에 while문 사용
        if Dsum < Rat[ii]:
            Dsum = Rat[ii] #총 대기시간이 도착시간보다 작으면 대기시간에 도착 시간
        print(f'{Rpr[ii]}',end='') #순서대로 실행될 프로세스ID출력
        ttext3.insert('end', f'{Rpr[ii]}')  #print 내용과 똑같게 텍스트 상자에 입력

        if Rpt[ii] > cut: #만약 작업시간이 cut(타임 슬라이스)보다 크다면
            Rpr.append(Rpr[ii]) #지금의 프로세스를 맨 뒤로 다시 보내고
            Rpt.append(Rpt[ii]-cut) #작업 시간에서 cut만큼 빼고 맨뒤에 저장
            Rpt[ii] = cut #지금 작업시간은 cut만큼으로 저장
            Dtime.append(Dsum - Rat[ii])  # 해당 프로세스의 대기시간=총대기시간-도착시간
            Dsum += Rpt[ii]  # 총 대기시간에 작업시간 추가
            Rat.append(Dsum) #도착시간은 지금까지 총 작업시간으로 저장
        else:
            Dtime.append(Dsum - Rat[ii])  # 해당 프로세스의 대기시간=총대기시간-도착시간
            Dsum += Rpt[ii]  # 총 대기시간에 작업시간 추가

        if a < len(Rpr)-1:
            a += 1 #
            print(' -> ',end='') #맨끝에는 '->'문자열이 추가되지 않도록 (전체길이-1)만큼 카운트 후 출력
            ttext3.insert('end', ' => ')
        ii += 1 #while문 반복 카운트
    print('\n')#줄바꿈
    ttext3.insert('end', '\n\n')

    for i in range(len(Rpr)):
        print(f'{Rpr[i]} 대기시간: {Dtime[i]} 초') #순서대로 프로세스의 대기시간 출력
        ttext3.insert('end', f'[{Rpr[i]} 대기시간] : {Dtime[i]} 초\n')

    print(f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n') #모든 프로세스의 대기시간의 합 / 프로세스 수
    ttext3.insert('end', f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n\n') #print 내용과 똑같게 텍스트 상자에 입력

#--------------------------------------------------------------------------------------------------------------------(우선순위

def PRIO(pr,at,pt,pri): #우선순위 알고리즘(ID,도착시간,작업시간,우선순위)
    srt = Rank_out(at)# 도착시간 순으로 인덱스 정렬
    a = 0 # '->' 문자 출력을 위한 카운트 변수
    Dsum = 0 # 총 소요시간
    Dtime = []+at #대기시간, 원소를 바꾸기 전에 인덱스 개수을 프로세스 개수만큼 초기화
    print('=============(우선순위)============')
    print('실행 순서 : ',end='')
    ttext4.insert('end', '[실행 순서] : ') #print 내용과 똑같게 텍스트 상자에 입력
    print(f'{pr[srt[0]]} -> ', end='') #맨처음 도착한 프로세스는 바로 실행
    ttext4.insert('end', f'{pr[srt[0]]} => ') #print 내용과 똑같게 텍스트 상자에 입력
    Dtime[srt[0]] = 0 #처음이므로 대기시간 0
    Dsum += at[srt[0]]+pt[srt[0]] #총 대기시간에 처음 도착한 프로세스의 도착,작업시간 추가
    Start = Rank_out(pri) # 우선순위 순으로 인덱스 정렬
    Start.remove(srt[0]) #처음 도착한 프로세스의 인덱스값 제거
    for i in Start:

        if Dsum < at[i]:
            Dsum = at[i] #앞과 동일
        print(f'{pr[i]}',end='')
        ttext4.insert('end', f'{pr[i]}') #print 내용과 똑같게 텍스트 상자에 입력
        Dtime[i]=Dsum-at[i] #앞과 동일
        Dsum += pt[i] #앞과 동일
        if a < len(Start)-1:
            a += 1 #앞과 동일
            print(' -> ',end='') #앞과 동일
            ttext4.insert('end', ' => ') #print 내용과 똑같게 텍스트 상자에 입력
    print('\n')
    ttext4.insert('end', '\n\n') #print 내용과 똑같게 텍스트 상자에 입력

    for i in range(len(pr)):
        print(f'{pr[i]} 대기시간: {Dtime[i]} 초') #앞과 동일
        ttext4.insert('end', f'[{pr[i]} 대기시간] : {Dtime[i]} 초\n') #print 내용과 똑같게 텍스트 상자에 입력

    print(f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n') #앞과 동일
    ttext4.insert('end', f'\n[평균 대기 시간 : {sum(Dtime)/len(pr)} 초]\n\n') #print 내용과 똑같게 텍스트 상자에 입력

#########################################################################################################################################################
#여기서부터 GUI

def Text_in(msg,xx,yy): #  화면에서 리스트 박스 위 목록 이름을 나타나게 해줄 함수(텍스트상자 내용, x좌표, y좌표)
    Tfont = font.Font(family="Arial", size=12, weight="bold") # 글꼴을 Arial, 글자크기를 12, 두꺼운 글씨로 폰트 형식 저장
    text = Text(root, bg="#EAEAEA", height=1, width=11) #배경색이 밝은 회색인 높이가 1, 폭이 11인 텍스트상자 선언
    text.place(x=xx, y=yy) #텍스트 상자를 x좌표 xx, y좌표 yy인 위치에 붙임
    text.insert(1.0, msg) #텍스트상자에 내용 입력
    text.configure(font=Tfont, state='disabled') #텍스트 상자의 글의 폰트를 Tfont로 지정하고, 텍스트상자의 내용을 변경할 수 없게 지정

def Text_in2(textB,xx,yy): #화면에 결과창을 넣어줄 함수(변수, x좌표, y좌표)
    Tfont = font.Font(family="Arial", size=10) #폰트 지정
    textB.place(x=xx, y=yy) #좌표 지정
    textB.configure(font=Tfont) #폰트 적용
def Label_in(msg,xx,yy): #화면에 이름표를 붙여줄 함수(이름표 내용, x좌표, y좌표)
    Tfont = font.Font(family="Arial", size=9, weight="bold") #폰트 지정
    lab = Label(root,text=msg, font=Tfont) #내용은msg고 폰트는 Tfont인 라벨 선언
    lab.place(x=xx,y=yy) #좌표 지정

def bt_in(msg,cmd,xx,yy): #버튼 추가 함수(버튼 내용,버튼을 눌렀을때 호출할 함수, x좌표, y좌표)
    btt = Button(root, bg="#BDBDBD", text=str(msg), height=2, width=10, command=cmd)  # 배경이 어두운 회색이고, 내용은 msg, 호출함수는 cmd인 버튼 선언
    btt.place(x=xx, y=yy) #버튼 좌표 지정


#------------------------------------------------------------------------------------------------------------------------------
#버튼 함수들

def Pinsert(): #"추가" 버튼을 눌렀을때 프로세스 리스트에 프로세스를 추가해줄 함수
    if text1.get(1.0,'end-1c')=='': #입력 받을 텍스트박스가 공백일때
        Sc.Process.append(str('None')) #프로세스 리스트에 None 추가
        prLB.insert('end', "None") #프로세스id 화면에도 None 추가
    else:
        Sc.Process.append(str(text1.get(1.0, 'end-1c'))) #텍스트박스에 내용이 있다면 리스트에 추가
        prLB.insert('end', (text1.get(1.0, 'end-1c'))) #텍스트 박스 내용을 화면에 추가

    if text2.get(1.0,'end-1c')=='': #입력 받을 텍스트박스가 공백일때
        Sc.Arr_Time.append(int(0)) #도착시간 리스트에 0추가
        atLB.insert('end', '0') #도착시간 화면에 0추가
    else:
        Sc.Arr_Time.append(int(text2.get(1.0, 'end-1c')))#텍스트박스에 내용이 있다면 리스트에 추가
        atLB.insert('end', (text2.get(1.0, 'end-1c')))#도착시간 화면에 내용 추가

    if text3.get(1.0,'end-1c')=='':#입력 받을 텍스트박스가 공백일때
        Sc.Play_Time.append(int(0)) #작업시간 리스트에 0추가
        ptLB.insert('end', '0')#작업시간 화면에 0추가
    else:
        Sc.Play_Time.append(int(text3.get(1.0, 'end-1c')))#텍스트박스에 내용이 있다면 리스트에 추가
        ptLB.insert('end', (text3.get(1.0, 'end-1c')))#작업시간 화면에 내용 추가

    if text4.get(1.0,'end-1c')=='':#입력 받을 텍스트박스가 공백일때
        Sc.Prio.append(int(0))#우선순위 리스트에 0추가
        priLB.insert('end', '0')#우선순위 화면에 0추가
    else:
        Sc.Prio.append(int(text4.get(1.0, 'end-1c')))#텍스트박스에 내용이 있다면 리스트에 추가
        priLB.insert('end', (text4.get(1.0, 'end-1c')))#우선순위 화면에 내용 추가

def DEL(aa): #리스트박스마다 마우스로 선택된 항목의 줄을 지워줄 함수
    Psel = aa.curselection() #선택된 원소 목록을 저장
    prLB.delete(Psel[0]) #선택된 원소의 줄에 있는 프로세스id 값을 화면에서 제거
    Sc.Process.remove(Sc.Process[Psel[0]]) #선택된 원소의 줄에 있는 프로세스id 값을 리스트에서 제거
    atLB.delete(Psel[0])#선택된 원소의 줄에 있는 도착시간 값을 화면에서 제거
    Sc.Arr_Time.remove(Sc.Arr_Time[Psel[0]])#선택된 원소의 줄에 있는 도착시간 값을 리스트에서 제거
    ptLB.delete(Psel[0])#선택된 원소의 줄에 있는 작업시간 값을 화면에서 제거
    Sc.Play_Time.remove(Sc.Play_Time[Psel[0]])#선택된 원소의 줄에 있는 작업시간 값을 리스트에서 제거
    priLB.delete(Psel[0])#선택된 원소의 줄에 있는 우선순위 값을 화면에서 제거
    Sc.Prio.remove(Sc.Prio[Psel[0]])#선택된 원소의 줄에 있는 우선순위 값을 리스트에서 제거

def Pdel(): #"삭제"버튼이 눌렸을때 호출될 함수
    if(prLB.curselection()!=()): #프로세스ID 리스트에서 만약 마우스 커서에 선택된 항목이 있다면
        DEL(prLB) # 항목에 해당된 줄의 값들을 모두 지움
    elif atLB.curselection()!=():#도착시간 리스트에서 만약 마우스 커서에 선택된 항목이 있다면
        DEL(atLB) # 항목에 해당된 줄의 값들을 모두 지움
    elif ptLB.curselection()!=():#작업시간 리스트에서 만약 마우스 커서에 선택된 항목이 있다면
        DEL(ptLB) # 항목에 해당된 줄의 값들을 모두 지움
    elif priLB.curselection()!=():#우선순위 리스트에서 만약 마우스 커서에 선택된 항목이 있다면
        DEL(priLB) # 항목에 해당된 줄의 값들을 모두 지움


def Pstart(): #"실행"버튼이 눌렸을 때 호출될 함수
    ttext1.delete(1.0, 'end') #결과 창의 모든 내용을 초기화
    ttext2.delete(1.0, 'end') #위와 동일
    ttext3.delete(1.0, 'end') #//
    ttext4.delete(1.0, 'end') #//
    if cbVal1.get()==1:#FCFS 체크박스가 선택되 있으면
        FCFS(Sc.Process, Sc.Arr_Time, Sc.Play_Time)#FCFS(프로세스ID목록,도착시간목록,작업시간목록)함수를 실행
    if cbVal2.get()==1:#SFJ 체크박스가 선택되 있으면
        SJF(Sc.Process, Sc.Arr_Time, Sc.Play_Time)#SFJ(프로세스ID목록,도착시간목록,작업시간목록)함수를 실행
    if cbVal3.get()==1:#RR 체크박스가 선택되 있으면
        RR(Sc.Process, Sc.Arr_Time, Sc.Play_Time, Sc.Time_Cut)#RR(프로세스ID목록,도착시간목록,작업시간목록,타임슬라이스)함수를 실행
    if cbVal4.get()==1:#우선순위 체크박스가 선택되 있으면
        PRIO(Sc.Process, Sc.Arr_Time, Sc.Play_Time, Sc.Prio)#PRIO(프로세스ID목록,도착시간목록,작업시간목록,우선순위목록)함수를 실행

def Ex(): #과제의 예제로 나왔던 내용을 화면에 보여줄 함수
    PPP = ['P1', 'P2', 'P3', 'P4']  # 프로세스 ID ex 리스트
    ART = [0, 4, 7, 10]  # 도착 시간 ex
    PLT = [15, 7, 2, 5]  # 작업 시간 ex
    PRI = [3, 4, 1, 2]  # 우선순위 ex
    ttext1.delete(1.0, 'end')# 결과창 내용 모두 지움
    ttext2.delete(1.0, 'end')#//
    ttext3.delete(1.0, 'end')#//
    ttext4.delete(1.0, 'end')#//
    if cbVal1.get() == 1:  # FCFS 체크박스가 선택되 있으면
        FCFS(PPP, ART, PLT)#예제 리스트의 내용으로 FCFS()실행
    if cbVal2.get() == 1:
        SJF(PPP, ART, PLT)#예제 리스트의 내용으로 SFJ()실행
    if cbVal3.get() == 1:
        RR(PPP, ART, PLT, 3)  # 예제 리스트의 내용으로 RR()실행
    if cbVal4.get() == 1:
        PRIO(PPP, ART, PLT, PRI)#예제 리스트의 내용으로 PRIO()실행

#========================================================================================================================
#메인 실행

root = Tk() #tkinter 화면 함수 지정
root.title("[OS] 프로세스 스케쥴링") #화면 타이틀 지정
root.resizable(False,False)#화면의 크기를 바꿀 수 없게 지정

root.geometry('1080x720+220+20') #화면의 사이즈는 폭1080,높이720이고 화면의끝에서 x좌표 220,y좌표 20인 곳에서 화면이 나타나게 지정
frame = Frame(root,height=100, width=400) #100X400 사이즈인 프레임 선언

prLB = Listbox(frame,height=30, width=15) #프로세스ID 리스트창을 프레임에 속하게 선언
atLB = Listbox(frame,height=30, width=15) #도착시간 리스트창을 프레임에 속하게 선언
ptLB = Listbox(frame,height=30, width=15) #작업시간 리스트창을 프레임에 속하게 선언
priLB = Listbox(frame,height=30, width=15) #우선순위 리스트창을 프레임에 속하게 선언
prLB.pack(side='left',fill='y')#프레임의 왼쪽에 붙임
atLB.pack(side='left',fill='y')#프레임의 다음 왼쪽에 붙임
ptLB.pack(side='left',fill='y')#프레임의 다음 왼쪽에 붙임
priLB.pack(side='left',fill='y')#프레임의 다음 왼쪽에 붙임
frame.place(x=10,y=30) #프레임의 위치를 지정
Text_in(" 프로세스 ID",13,5) #텍스트박스 생성 함수를 이용해서 텍스트박스 추가
Text_in("   도착 시간",122,5)#//
Text_in("   작업 시간",232,5)#//
Text_in("   우선 순위",340,5)#//

Tfont1 = font.Font(family="Arial", size=11)#폰트 지정
text1 = Text(root, height=1, width=12)#프로세스ID 입력창 선언
text1.place(x=15, y=520)#위치 적용
text1.configure(font=Tfont1)#폰트 적용
text2 = Text(root, height=1, width=12)#도착시간 입력창 선언
text2.place(x=123, y=520)
text2.configure(font=Tfont1)
text3 = Text(root, height=1, width=12)#작업시간 입력창 선언
text3.place(x=232, y=520)
text3.configure(font=Tfont1)
text4 = Text(root, height=1, width=12)#우선순위 입력창 선언
text4.place(x=341, y=520)
text4.configure(font=Tfont1)

bt_in("추가",Pinsert,40,600)#프로세스 "추가" 버튼을 화면에 추가
bt_in("삭제",Pdel,140,600)#프로세스 "삭제" 버튼을 화면에 추가
bt_in("실행",Pstart,240,600)#스케쥴링 "실행" 버튼을 화면에 추가
bt_in("예제",Ex,340,600)# "예제" 실행 버튼을 화면에 추가

Label_in("===< FCFS >===",480,1)#FCFS 이름표 추가
ttext1 = Text(root, height=9, width=84)#FCFS 텍스트박스의 변수를 선언
Text_in2(ttext1,480,20)#FCFS 텍스트박스 추가
Label_in("===< SJF >===",480,178)#SFJ 이름표 추가
ttext2 = Text(root, height=9, width=84)#SFJ 텍스트박스의 변수를 선언
Text_in2(ttext2,480,200)#SFJ 텍스트박스 추가
Label_in("===< RR >===",480,359)#RR 이름표 추가
ttext3 = Text(root, height=9, width=84)#RR 텍스트박스의 변수를 선언
Text_in2(ttext3,480,380)#RR 텍스트박스 추가
ttext4 = Text(root, height=9, width=84)#우선순위 텍스트박스의 변수를 선언
Label_in("===< 우선순위 >===",480,538)#우선순위 이름표 추가
Text_in2(ttext4,480,560)#우선순위 텍스트박스 추가

cbVal1 = IntVar() #체크박스의 상태값을 정수형으로 저장
cbVal2 = IntVar()#//
cbVal3 = IntVar()#//
cbVal4 = IntVar()#//
cbox1 = Checkbutton(root, text='', variable=cbVal1)#이름이 지정되지 않은 체크박스 지정,FCFS()를 실행할지 선택할 체크박스
cbox1.place(x=452, y=90) #위치 지정
cbox1.toggle() #처음부터 체크박스가 선택되있는 상태로 지정
cbox2 = Checkbutton(root, text='', variable=cbVal2)#이름이 지정되지 않은 체크박스 지정,SFJ()를 실행할지 선택할 체크박스
cbox2.place(x=452, y=270)#위치 지정
cbox2.toggle()
cbox3 = Checkbutton(root, text='', variable=cbVal3)#이름이 지정되지 않은 체크박스 지정,RR()을 실행할지 선택할 체크박스
cbox3.place(x=452, y=450)#위치 지정
cbox3.toggle()
cbox4 = Checkbutton(root, text='', variable=cbVal4)#이름이 지정되지 않은 체크박스 지정,PRIO()를 실행할지 선택할 체크박스
cbox4.place(x=452, y=630)#위치 지정
cbox4.toggle()

root.mainloop()#프로그램창 실행
