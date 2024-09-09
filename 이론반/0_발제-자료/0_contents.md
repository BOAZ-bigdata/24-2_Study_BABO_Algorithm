<!-- 
아래 적힌 내용들은 팀장(원종빈)이 코테를 준비하면서 주제별로 도움이 될만한 내용들을 메모해둔 것들입니다.

발제자분들께서는 아래 내용에 크게 구애받지 않고 편하신대로 발제 구성하신 뒤, 아래 목차만 업데이트해주시면 감사하겠습니다!

-->

### 1. OT, 시간복잡도 (원종빈)
1. OT
    - 소개 및 코테 공부 경험, 자구알 수업 수강여부 조사
    - 이론 발제가 가능한 사람 조사
2. 공부법 소개
    - 백준/솔브닥 회원가입 및 솔드닥 연결
        - 그 외 플랫폼들 소개 (프로그래머스, 릿코드)
        - 난이도 비교
    - 교재 소개
    - 솔브닥 클래스 소개
    - 백준에서 좋은 코드를 찾는 법
    - 다 하고나서 마지막으로 깃헙 pull/pr 테스트
3. 시간복잡도
    - 시간복잡도 이론 간단 설명 (clrs 참고)
    - 완전 탐색 문제
    - `import sys; input = lambda~` (단, 프로그래머스는 X)
    - 시간복잡도 표 공유 및 같이보기
- 과제
    - [백준 1018 - 체스판 다시 칠하기 (S4)](https://www.acmicpc.net/problem/1018)
    - [백준 18870 - 좌표압축 (S2)](https://www.acmicpc.net/problem/18870)
    - [프로그래머스 - 연속된 부분수열의 합 (lv2)](https://school.programmers.co.kr/learn/courses/30/lessons/178870)



<br>



### 2. 재귀 (김윤주)
- `import sys; sys.setrecursionlimit(10 ** 6)` <- 재귀로 문제를 풀 때는 해당 코드는 필수다! ([출처](https://fuzzysound.github.io/sys-setrecursionlimit))
1. 1주차 과제 코드 리뷰
2. 재귀 이론 설명
    - 꼬리 재귀
- 과제
    - [백준 4779 - 칸토어 집합 (S3)](https://www.acmicpc.net/problem/4779)
    - [백준 1182 - 부분 수열의 합 (S2)](https://www.acmicpc.net/problem/1182)
    - [백준 1759 - 암호 만들기 (G5)](https://www.acmicpc.net/problem/1759)



<br>



### 3. DFS/BFS (원종빈)
1. post-OT
    - 과제로 나가는 문제들 난이도/개수 괜찮은지 조사
    - git commit message 작성법
2. 기초 자료구조
    - 스택과 덱(deque)
    - 그래프
        - 그래프의 두 가지 표현법 
3. DFS/BFS
    - DFS/BFS 기초
    - DFS/BFS 변형
    - DFS/BFS 확장
- 과제
    - [백준 1260 - DFS와 BFS (S2)](https://www.acmicpc.net/problem/1260)
    - [백준 11724 - 연결 요소의 개수 (S2)](https://www.acmicpc.net/problem/11724)
    - [백준 1743 - 음식물 피하기(S1)](https://www.acmicpc.net/problem/1743)
- 번외 (난이도가 조금 있어서, 과제로 나가지는 않지만 재밌는 문제들)
    - [백준 7576 - 토마토 (G5)](https://www.acmicpc.net/problem/7576)
    - [백준 1697 - 숨바꼭질 (S1)](https://www.acmicpc.net/problem/1697) 
<!-- 조금 난이도 있는 문제인 것 같다. DP로도 풀 수 있다! -->



<br>



### 4. 그리디 (박지원)
1. 3주차 과제 코드리뷰
2. Greedy
    1. Greedy 정당성 증명
    2. 거스름돈 문제
3. DP
    1. 구현 방식: top-down vs bottom-up
- 과제
    - [백준 1931 - 회의실 배정 (S1)](https://www.acmicpc.net/problem/1931)
    - [백준 11501 - 주식 (S2)](https://www.acmicpc.net/problem/11501)
    - [백준 1912 - 연속합 (S2)](https://www.acmicpc.net/problem/1912)
- 번외
    - [백준 11000 - 강의실 배정 (G5)](https://www.acmicpc.net/problem/11000)
    - [프로그래머스 42884 - 단속카메라 (lv3)](https://school.programmers.co.kr/learn/courses/30/lessons/42884)



<br>



### 5. 다이나믹 프로그래밍 (유종문)

1. 4주차 과제 코드리뷰

2. 다이나믹 프로그래밍 (동적계획법) [[PDF]](./5_다이나믹-프로그래밍/5_동적계획법.pdf)
    - DP의 필요성 및 메모이제이션 기법 소개
    - DP 예제1 : 피보나치 수열
    - DP 예제2 : 진우의 달 여행 (Large)
    - DP 풀이 팁
    - Greedy 와의 비교

3. DP 유형 소개
    - LIS: Longest Increasing Subsequence
    - LCS: Longest Common Substring
    - Knsapsack
    - TSP: Traveling Salesman Problem

4. 기타 문제 풀이 팁


- 과제
    - [백준 11726 - $2 \times N$ 타일링 (S3)](https://www.acmicpc.net/problem/11726)
    - [백준 9095 - 1, 2, 3 더하기 (S3)](https://www.acmicpc.net/problem/9095)
    - [백준 1932 - 정수 삼각형 (S1)](https://www.acmicpc.net/problem/1932)
- 번외
    - [백준 2579 - 계단 오르기 (S3)](https://www.acmicpc.net/problem/2579)
    - [백준 11727 - $2 \times N$ 타일링 2 (S3)](https://www.acmicpc.net/problem/11727)
    - 꼭 더 많은 문제들 풀어보세요 🔥

<br>



### 6. 최단경로 알고리즘 (이상윤)
1. 사전 지식
    - 최단거리의 개념
    - BFS/DFS와의 비교
2. 알고리즘 소개
    - 다익스트라 알고리즘
    - 플로이드-와샬 알고리즘
    - 벨만포드 알고리즘
3. 문제풀이시 마인드셋
- 과제
    - [백준 14284 - 간선 이어가기2 (G5)](https://www.acmicpc.net/problem/14284)
    - [백준 14938 - 서강그라운드 (G4)](https://www.acmicpc.net/problem/14938)
- 번외
    - [백준 13549 - 숨바꼭질 3 (G5)](https://www.acmicpc.net/problem/13549)
    - [백준 11404 - 플로이드 (G5)](https://www.acmicpc.net/problem/11404)

<br>



### 7. 이진탐색 (심재혁)
1. Up-down Game
2. 이진탐색
3. 이진탐색 대표유형
    - 특정 숫자 빠르게 찾기
    - 특정 숫자 개수 세기
    - 정수 분배
- 과제
    - [백준 1920 - 수 찾기 (S4)](https://www.acmicpc.net/problem/1920)
    - [백준 16401 - 과자 나눠주기 (S2)](https://www.acmicpc.net/problem/16401)
    - [백준 2110 - 공유기 설치 (G4)](https://www.acmicpc.net/problem/2110)