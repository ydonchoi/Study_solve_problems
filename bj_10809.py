# 문제번호: 10809
# 알파벳 찾기
# url: https://www.acmicpc.net/problem/10809
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
#########################


# be about to revise soon if there is... Below is a prior solution.


'''(approach) [풀이과정 구상]
- s = 단어의 길이는 100 이내
- 단어 내 알파벳 등장 위치 표시
- 정리하면 주어진 단어를 알파벳 단위로 스캔하여 알파벳별로 처음 등장하는 위치를 표시하는 프로그램이라는 것
- 중복 등장하는 경우는 처음 등장하는 위치만, 등장하지 않는 경우는 -1 표시하는 조건'''

def location():
	s = input('영단어:')
	none = []
	print('입력 영단어 = ',s)
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(len(alphabet)):
		for j in range(len(s)):
			if s[j] == alphabet[i]:
				print(alphabet[i], '의 등장 위치: ',j,'번째 처음 등장')
				break
			else:
				none.append(alphabet[i])
	none2 = sorted(list(set(none)))
	for i in range(len(none2)):
		print(none2[i],'의 위치: -1')    # 너무 복잡하게 생각했다ㅠ 괜히 순서대로 맞춰야 한다는 점에 얽매여서 엄청 헤맸음
	print('mission complete')

location()

# fin.