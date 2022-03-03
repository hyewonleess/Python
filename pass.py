# 1. 클래스, 함수에서의 pass 사용

# 내부 구현은 필요하지 않지만, 의미적으로 껍데기만 필요한 경우
# 아무것도 정의하지 않아도 에러 없이 RUN

class Hello:
    pass


def func():
    pass


# 2. 반복문, if문에서의 pass 사용

# pass
for i in range(10):
    if i % 2 == 0:
        pass
        print(i)
    else:
        print(i)
print("Done")

# continue: i가 짝수이면 continue을 통해 바로 loop로 가기 때문에 print(i)를 실행하지 않음
for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
    else:
        print(i)
print("Done")

# break
for i in range(10):
    if i % 2 == 0:
        break
        print(i)
    else:
        print(i)
print("Done")


