k = int(input())
st = []
for i in range(k):
    num = int(input())
    if num == 0:
        st.pop()
    else:
        st.append(num)
print(sum(st))