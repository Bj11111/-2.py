import streamlit as st

# st.beta container():
st.columns(1)
# dict = {}
for i in range(1,10):
#         dict[i] = ' '
      d = {}

def check():
    if (dict[1] == dict[2]== dict[3] != ' ' 
    or dict[4] == dict[5]== dict[6] != ' '
    or dict[7] == dict[8]== dict[9] != ' '
    or dict[1] == dict[4]== dict[7] != ' '
    or dict[2] == dict[5]== dict[8] != ' '
    or dict[3] == dict[6]== dict[9] != ' '
    or dict[1] == dict[5]== dict[9] != ' '
    or dict[3] == dict[5]== dict[7] != ' ' ):
        return True

def print_board():
    st.write(dict[7], '|' , dict[8] , '|', dict[9])
    st.write('- + - + -') 
    st.write(dict[4], '|' , dict[5] , '|', dict[6])
    st.write('- + - + -')
    st.write(dict[1], '|' , dict[2] , '|', dict[3])
     
def main( ):
    move1 = int(text_input('你想怎麼走?'))
    if dict[move1] == ' ':
      dict[move1] = 'X'
    else:
        print('這是被禁止的')
    print_board()

    move2 = int(text_input('你想怎麼走?'))
    if dict[move2] == ' ':
        dict[move2] = 'O'
    else:
        print('這是被禁止的')
    print_board()
    
    if check():
        print('game over')
    else:
        main()

a = st.test_input('想玩井字遊戲嗎？（是/否): ')
if a =='是':

    main()
else:
    wt.write('可憐')
