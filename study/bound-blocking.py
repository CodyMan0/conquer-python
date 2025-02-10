import requests


# CPU Bound
## CPU에 의해 막히는 것
### 프로그램이 실행될때 실행 속도가 느려짐
def cpu_bound_func(num: int):
    total = 1
    arrange = range(1, num + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
    return total


# I/O Bound
## 프로그램 실행 속도가 IO에 의해 제한될 때
### 유저가 주체
def io_bound_func():
    result = requests.get("https://google.com")
    return result

    # print("값을 입력해주세요.")
    input_value = input()
    # return int(input_value) + 100


### 다른 서버가 주체
### Network I/O 바운드

if __name__ == "__main__":
    # result = cpu_bound_func(30)
    for i in range(10):
        result1 = io_bound_func()
    print(result1)


# 블로킹 : 바운드에 의해 코드가 멈추게 되는 현상이 일어나는 것
