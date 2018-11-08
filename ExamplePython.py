# GUI 모듈(tkinter) import
import tkinter

# 가장 상위 레벨의 윈도우 창 생성
window = tkinter.Tk()

window.title("LEE A REUM")              # 윈도우 창의 제목 설정
window.geometry("640x400+100+100")      # ("너비x높이+x좌표+y좌표") 윈도우 창의 너비와 높이, 초기 화면의 위치 설정
window.resizable(False, False)          # (상하, 좌우) 윈도우 창의 창 크기 조절 가능 여부 설정

label = tkinter.Label(window, text="안녕하세요.")    # 윈도우 창에 Label 위젯 설정
# 위젯 배치
label.pack()

# 윈도우 이름의 윈도우 창을 윈도우가 종료될 때까지 실행
window.mainloop()       