# GUI 모듈(tkinter) import
import tkinter

operation = ''      # 연산자 저장 변수
temp_number = 0     # 이전 값 저장 변수

# 버튼 눌렸을 때, 텍스트 창에 숫자 표시하는 함수
def button_pressed(value):
    if value == 'AC':
        number_entry.delete(0, "end")  # 텍스트 창에 있는 모든 내용을 지우는 것
        print("AC pressed")
    else:
        number_entry.insert("end", value)  # 텍스트 창으로 숫자 전송하는 것, 'end'는 오른쪽 끝에 추가하라는 의미
        print(value, "pressed")

# 사칙연산('+, -, /, *') 버튼 처리하는 함수
def math_button_pressed(value):
    global operation
    global temp_number

    # 기존에 입력한 숫자가 있을 경우에만 연산 버튼 인식
    if not number_entry.get() == '':
        operation = value
        temp_number = int(number_entry.get())   # 입력된 숫자를 임시변수에 저장
        number_entry.delete(0, 'end')           # 입력칸을 비우고, 다음숫자를 받을 준비
        print(temp_number, operation)

# '=' 버튼 처리하는 함수
def equal_button_pressed():
    global operation
    global temp_number

    # 연산자나 숫자가 입력되지 않으면, 실행하지 X
    if not (operation == '' and number_entry.get() == ''):
        number = int(number_entry.get())

        if operation == '/':
            solution = temp_number/number
        elif operation == '*':
            solution = temp_number*number
        elif operation == '+':
            solution = temp_number+number
        else:
            solution = temp_number-number

        # 계산 후, 숫자 표시칸을 비우고, 계산 결과를 표시
        number_entry.delete(0, 'end')
        number_entry.insert(0, solution)
        print(temp_number, operation, number, '=', solution)
        operation = ''
        temp_number = 0

# 가장 상위 레벨의 윈도우 창 생성
window = tkinter.Tk()

window.title("Calculator")      # 윈도우 창의 제목 설정
window.geometry("350x200")      # ("너비x높이+x좌표+y좌표") 윈도우 창의 너비와 높이, 초기 화면의 위치 설정

# 텍스트 창의 값 저장할 변수
entry_value = tkinter.StringVar(window, value='')

# 숫자 및 결과 표시창
number_entry = tkinter.Entry(window, textvariable=entry_value, width=20)
number_entry.grid(row=0, columnspan=3)

# 숫자 버튼
button_ac = tkinter.Button(window, text="AC", width=10, command=lambda:button_pressed('AC'))
button_ac.grid(row=4, column=0)

button0 = tkinter.Button(window, text="0", width=10, command=lambda:button_pressed('0'))
button0.grid(row=4, column=1)

button_equal = tkinter.Button(window, text="=", width=10, command=lambda:equal_button_pressed())
button_equal.grid(row=4, column=2)

button_sub = tkinter.Button(window, text="-", width=10, command=lambda:math_button_pressed('-'))
button_sub.grid(row=4, column=3)


button1 = tkinter.Button(window, text="1", width=10, command=lambda:button_pressed('1'))
button1.grid(row=3, column=0)

button2 = tkinter.Button(window, text="2", width=10, command=lambda:button_pressed('2'))
button2.grid(row=3, column=1)

button3 = tkinter.Button(window, text="3", width=10, command=lambda:button_pressed('3'))
button3.grid(row=3, column=2)

button_add = tkinter.Button(window, text="+", width=10, command=lambda:math_button_pressed('+'))
button_add.grid(row=3, column=3)


button4 = tkinter.Button(window, text="4", width=10, command=lambda:button_pressed('4'))
button4.grid(row=2, column=0)

button5 = tkinter.Button(window, text="5", width=10, command=lambda:button_pressed('5'))
button5.grid(row=2, column=1)

button6 = tkinter.Button(window, text="6", width=10, command=lambda:button_pressed('6'))
button6.grid(row=2, column=2)

button_mult = tkinter.Button(window, text="*", width=10, command=lambda:math_button_pressed('*'))
button_mult.grid(row=2, column=3)


button7 = tkinter.Button(window, text="7", width=10, command=lambda:button_pressed('7'))
button7.grid(row=1, column=0)

button8 = tkinter.Button(window, text="8", width=10, command=lambda:button_pressed('8'))
button8.grid(row=1, column=1)

button9 = tkinter.Button(window, text="9", width=10, command=lambda:button_pressed('9'))
button9.grid(row=1, column=2)

button_div = tkinter.Button(window, text="/", width=10, command=lambda:math_button_pressed('/'))
button_div.grid(row=1, column=3)

# 윈도우 이름의 윈도우 창을 윈도우가 종료될 때까지 실행
window.mainloop()