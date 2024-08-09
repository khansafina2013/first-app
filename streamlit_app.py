import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "Safina Khan.")   


first_number = st.text_input("Type a number 10-20:point_down:")
second_number = st.text_input("Type a number 50-70:point_down:")

number_sum = int(first_number) + int(second_number)

st.write(str(number_sum))

#display the sum of number 1 and 2
st.write(str(first_number)  + "+" + str(second_number)  
         + "=" + str(number_sum))


# write an if elif else statment for the first number 

if int(first_number) < 10:
    st.warning("first number is too low")

elif int(first_number) > 20:
    st.warning("first number is too high")

else:
    st.success("number " + str(first_number) + " is okay")    

# write an if elif else statment for the second number


if int(second_number) < 50:
    st.warning("second number is too low")

elif int(second_number) > 70:
    st.warning("second number is too high")  

else:
    st.success("number " + str(second_number) + " is okay")

  


