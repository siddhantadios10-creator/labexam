
s = input("Enter the Expression:")
st = []

for c in s:

    # Push opening brackets onto stack
    if c in '({[':
        st.append(c)

    # Check closing brackets
    elif c in ')}]':
        if not st or (c == ')' and st[-1] != '(') or (c == '}' and st[-1] != '{') or (c == ']' and st[-1] != '['):
            print(False)
            break

        st.pop()

else:
    print(True if not st else False)
