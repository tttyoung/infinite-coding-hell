def ins_sort(arr):
    n = len(arr)
    for i in range(1, n): #첫번째 요소는 이미 정렬되어있다고 간주, 2번째 요소부터 시작
        for j in range(i, 0, -1): #i부터 왼쪽으로 한칸씩 이동
            if arr[j] < arr[j-1]: #arr[j]와 그 전 항몽(arr[j-1]) 비교하여 오른쪽 항목이 더 작을 경우 두 항몽의 위치를 바꾼다
                arr[j], arr[j-1] = arr[j-1], arr[j]
        print(arr)
            
d = [4, 2, 3, 1, 6, 8, 0]     
ins_sort(d)    
print(d)

""" 선택정렬과 삽입정렬 차이
선택정렬 - index[0]을 최솟값의 위치로 임의설정, 뒤로 하나씩 비교하며 더 작은 값이 있는지 찾고 있으면 그 값을 최솟값의 위치로 설정, 원래의 최솟값 위치랑 swap, 5개, 4개, 3개 ... 이런식으로 반복
삽입정렬 - index[1]부터 시작하여 왼쪽에 자기보다 큰 값이 있는지 찾기, 있으면 위치 바꾸기... 반복 """