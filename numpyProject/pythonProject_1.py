"""
    자료형
    => 리스트 => []
    => 튜플 => ()
    => 딕트 => {키:값}
    => 데이터 프레임 : table
"""

score = [98,89,78,50,56]

print(score)

for jumsu in score:
    print(jumsu)

hap = sum(score)

print(hap)

member =["홍길동",90,"심청이",85,"박문수",77,"이순신",99,"강감찬",67]

print(member[2:])
print(member[::2])
# 한개 => 인덱스 (0번부터...) , 범위 ===> : 
# 요소 변경 / 추가 / 삭제

nums = list(range(10))

print(nums)
nums.append(50)

print(nums)

print(sorted(nums,reverse=True))