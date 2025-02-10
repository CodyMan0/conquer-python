import asyncio

# .0. 루틴 : 일련의 명령 (코드의 흐름)
# 1. 메인 루틴 : 프로그램의 메인 코드의 흐름
# 2. 서브 루틴 : 메인 루틴 내부 함수나 메소드를 말함.(인풋과 아웃풋이 있어야함)
# 3. 코루틴
## 서브루틴의 일반화된 형태
## 다양한 진입점, 탈출점이 있는 루틴? JS에서 generator? yield? next 이런 느낌과 비슷하다?


# 어웨이터블 객체?
## 코루틴, 테스트, 퓨처가 와야한다.
### 테스크 : 코루틴을 동시에 예약하는데 사용됨.

#### task = asyncio.create_task(delivery("A",2))

### 퓨쳐 : 비동기 연산의 최종 결과를 나타내는 저수준 어웨이터블 객체
#### 멀티 스레딩, 프로세싱과 연관있음.


async def hello_world():
    print("happy ")


if __name__ == "__main__":
    asyncio.run(hello_world())
