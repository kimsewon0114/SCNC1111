print('Let me help you to find the residential hall you want!')
print('What is your ratio for the importance of factor [distance to school]?')
a=float(input())
print('What is your ratio for the importance of factor [time spent to school]?')
b=float(input())
print('What is your ratio for the importance of factor [transportation fee?]')
c=float(input())
print('What is your ratio for the importance of factor [lodging fee?]')
d=float(input())


SKYL=a*-0.985+b*-1.831+c*-1.215+d*-0.162
SwH=a*-0.933+b*-1.051+c*-1.215+d*-0.162
StH=a*-0.724+b*0.12+c*-1.215+d*-0.162
LHTH=a*-0.881+b*-0.661+c*0.101+d*-0.162
RH=a*-0.724+b*0.12+c*0.101+d*-1.356
SCSH=a*-0.253+b*-0.27+c*0.101+d*-0.162
LSKH=a*-0.253+b*-0.27+c*0.101+d*-0.162
MH=a*-0.253+b*-0.661+c*0.101+d*-0.162
SJC=a*-0.463+b*1.291+c*1.418+d*3.142
RCLH=a*1.211+b*0.51+c*1.418+d*-0.162
LHH=a*1.211+b*0.51+c*1.418+d*-0.162
WLH=a*1.106+b*0.12+c*0.101+d*-0.162
UH=a*1.943+b*2.072+c*-1.215+d*-0.162

a=0
for i in (SKYL,SwH,StH,LHTH,RH,SCSH,LSKH,MH,SJC,RCLH,LHH,WLH,UH):
      if i<a:
          a=i
      else:
          continue

         
if a==SKYL:
    print('most suitable hall for you is Simon K.Y.Lee Hall!')
elif a==SwH:
    print('most suitable hall for you is Swire Hall!')
elif a==StH:
    print('most suitable hall for you is Starr Hall!')
elif a==LHTH:
    print('most suitable hall for you is Lady Ho Tung Hall!')
elif a==RH:
    print('most suitable hall for you is Ricci Hall!')
elif a==SCSH:
    print('most suitable hall for you is Suen Chi Sun Hall!')
elif a==LSKH:
    print('most suitable hall for you is Lee Shau Kee Hall!')
elif a==MH:
    print('most suitable hall for you is Morrison Hall!')
elif a==SJC:
    print('most suitable hall for you is St.Johns College!')
elif a==RCLH:
    print('most suitable hall for you is R.C.Lee Hall!')
elif a==LHH:
    print('most suitable hall for you is Lee Hysan Hall!')
elif a==WLH:
    print('most suitable hall for you is Wei Lun Hall!')
elif a==UH:
    print('most suitable hall for you is University Hall!')


