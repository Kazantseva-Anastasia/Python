st = []
st1 = []
for i in range(int(input())):
    st.append(input())
for i in range(len(st)):
    if int(st[i][-1]) > 3:
        st1.append(st[i])
print()
for students in st1:
    print(students)

