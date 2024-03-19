'''
    문자열 / 리스트(배열) / for ...
    문자열
        1) Upper / lower (대문자, 소문자)
        2) rstrip() / lstrip() / strip()
           오른쪽 공백 / 왼쪽 공백/ 양쪽 공백 제거
        3) swapCase() => 대문자 => 소문자 변경, 소문자 => 대문자 변경
        4) len() => 문자의 길이
        5) startwith() => 시작 문자열
        6) find() => 첫번째 나오는 문자 또는 문자열 위치 찾기
        7) count() => 선택한 문자의 갯수
        8) split() => 문자 분리
    함수 / 데이터베이스 연결
'''
'''
data = " Hello Python "
print(data)
print(data.upper())
print(data.lower())
print(len(data))

print(data.find("l"))
print(data.count("o"))

print(data.split(" "))
print(data.index("e"))
'''

'''
    배열 = [] => list형
    예) 숫자
        nums=[12,3,4,5...]

'''
names = ["홍길동","심청이","이순신","춘향이","박문수"]
print(names)

for name in names:
    print(name)


#배열에 저장된 갯수 확인
print("인원:{}".format(len(names)))
#추가
'''
    마지막 첨부
    append(값)
    지정된 위치 첨부
    insert(번호,값)
'''
names.append("강감찬")
print(names)

names.insert(0,"김두한")
print(names)

print("======== 여러 개 동시에 추가 ========")
names.extend(["김유신","을지문덕"])
print(names)
print("======== 데이터 삭제 ===========")
names.remove("을지문덕")
print(names)
print("======== 데이터 정렬 ==========")
names.sort()
print(names)
print("======== 데이터 정렬 (DESC) ==========")
names.sort(reverse=True)
print(names)
