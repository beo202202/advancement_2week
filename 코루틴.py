# 실행 중인 함수를 잠시 중단(대기 상태)하고
# 나중에 실행을 재생하는 기능

def my_coroutine():
    while True:
        value = yield
        print('Received value:', value)


# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send('Hello, world!')
