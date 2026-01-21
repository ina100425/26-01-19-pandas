import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------------

""" 그래프 생성 """

plt.plot([2, 3, 4, 5]) # y축
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # x축, y축
plt.xlabel("x-axis") # x축 제목
plt.ylabel("y-axis") # y축 제목
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 5, 13], label = "Square") # label : 법례 이름
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend() # 그래프 구석에 법례(이름표 상자) 생성
plt.show()

""" 축 범위 설정 """
# xlim(xmin, xmax)
# ylim(ymin, ymax)

plt.plot([1, 2, 3, 4], [12, 6, 12, 6])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim([0, 5])
plt.ylim([0, 15])
plt.show()

#---------------------------------------------------------------------------------------

""" 선 종류 """
# solid line : 실선 ("-")
# dashed line : ---------------- ("--")
# dashdot line : -.-.-.-.-.-.-. ("-.")
# dotted line : 점선 (":")

    # 기호는 linestyle = 을 생략해도 됨
plt.plot([1, 2, 3], [4, 4, 4], "-", label = "solid")            # color = 으로 선 색상 설정 가능
plt.plot([1, 2, 3], [3, 3, 3], "--", label = "dashed")
    # 풀네임은 linestyle = 을 반드시 붙여줘야 함
plt.plot([1, 2, 3], [2, 2, 2], linestyle = "dashdot", label = "dash-dot")
plt.plot([1, 2, 3], [1, 1, 1], linestyle = "dotted", label = "dotted")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
    # loc = 으로 법례의 위치를 설정 가능
    # ncol = 으로 법례를 어떻게 나열할 지 설정 가능
plt.legend(loc = "upper right", ncol = 4)
plt.show()


# plt.clf() : 현재 열려 있는 그래프 창을 깨끗하게 지우는 명령

#---------------------------------------------------------------------------------------

""" 마커 """
# 그래프의 데이터 포인트 표시

plt.plot([4, 5, 6], "b") # b는 blue
plt.plot([3, 4, 5], "ro") # r은 red, o는 원
plt.plot([2, 3, 4], marker = "s") # s는 square
plt.plot([1, 2, 3], marker = "D") # D는 Diamond
plt.plot([0, 1, 2], marker = "$A$") # $A$는 A라는 문자를 마커로 하겠다는 뜻

""" 베이스 컬러 """
# 약자로 지정할 수 있는 8가지 기본 색상
# b(blue), g(green), r(red), c(cyan), m(magenta), y(yellow), k(black), w(white)

plt.title("titanic", pad = 10) # pad : 제목과 그래프 사이에 간격 설정
plt.show()

#---------------------------------------------------------------------------------------

""" 산점도 차트 """
np.random.seed(0) # 초기값
                  # 랜덤 숫자 생성기의 시작점을 고정
n = 50 # 점의 개수
x = np.random.rand(n) # x 좌표에 n개
y = np.random.rand(n) # y 좌표에 n개
size = (np.random.rand(n)*20)**2 # 그래프 크기
color = np.random.rand(n) # 색상
    # scatter 옵션
plt.scatter(x, y, s = size, c = color, alpha = 0.5) # alpha : 투명도
plt.colorbar()
plt.show()