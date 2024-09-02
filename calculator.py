try:    
    import streamlit as st
    number = st.radio("What maths do you want to calculate ?",('addition(+)','subtraction(-)','division(/)','mutiplication(*)'))
    if (number == "addition(+)"):
        a1 = st.number_input ("What is the first number  you want to add")
        a1 = int(a1)
        a2 = st.number_input("what is the second number you want to add")
        a2 = int(a2)
        st.write(f"{a1} + {a2} = {a1 + a2}")
    elif (number == "subtraction(-)") :
        s1 = st.number_input("What is the first number  you want to subtract")
        s1 = int(s1)
        s2 = st.number_input("what is the second number you want to subtract")
        s2 = int(s2)
        st.write(f"{s1} - {s2} = {s1 - s2}")
    elif (number == "division(/)") :
        d1 = st.number_input("What is the first number  you want to divide")
        d1 = int(d1)
        d2 = st.number_input("what is the second number you want to divide")
        d2 = int(d2)
        st.write(f"{d1} / {d2} = {d1 / d2}")
    elif (number == "mutiplication(*)") :
        m1 = st.number_input("What is the first number  you want to multiply")
        m1 = int(m1)
        m2 = st.number_input("what is the second number you want to multiply")
        m2 = int(m2)
        st.write(f"{m1} * {m2} = {m1 * m2}")
    else:
        st.write('We only calculate addition(+),subtraction(-),division(/),mutiplication(*)')
except ZeroDivisionError:
    st.write("0 / 0 = 0")
finally:
    st.write()