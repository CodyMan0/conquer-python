import asyncio
import time

# 동기 : 코드가 반드시 작성된 순서 대로 실행됨

# def delivery(name, mealtime):
#     print(f"{name}에게 배달 완료!")
#     time.sleep(mealtime)
#     print(f"{name} 식사 완료, {mealtime}시간 소요...")
#     print(f"{name}그릇 수거 완료")
#
#
# def main():
#     delivery("A", 3)
#     delivery("B", 4)
#     delivery("C", 5)


# 비동기 : 코드가 반드시 작성된 순서 대로 실행 되는 것은 아님


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name}그릇 수거 완료")


async def main():
    await delivery("A", 3)
    await delivery("B", 4)
    await delivery("C", 5)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
