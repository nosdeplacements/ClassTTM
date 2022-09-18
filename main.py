#!/usr/bin/env python3

import app_text
import datetime
import numpy as np
import streamlit as st
import tree

# Initialize streamlit
if 'num' not in st.session_state:
    st.session_state.num   = 0
    st.session_state.ans   = np.full((app_text.question.size,), None)
    st.session_state.id    = st._get_script_run_ctx().session_id
    st.session_state.date  = datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')[:-4]
    st.session_state.phase = None

# Routine to send the email
def write_message():

    message  = u"Nom de l'utilisateur: %s\n" % (st.session_state.id)
    message += u"Timestamp de l'utilisateur: %s\n" % (st.session_state.date)
    message += u"Phase de l'utilisateur: phase %s\n" % (app_text.phase_nom[st.session_state.phase])
    message += u"Version de l'algorithme: %s\n" % (tree.version)
    message += u"%s: %s\n" % (app_text.question[0], st.session_state.ans[0][0])
    message += u"%s: %s\n" % (app_text.question[1], ",".join(st.session_state.ans[1]))
    message += u"%s: %s\n" % (app_text.question[2], st.session_state.ans[2][0])
    message += u"%s %s\n" % (app_text.question[3], ",".join(st.session_state.ans[3]))
    message += u"%s %s\n" % (app_text.question[4], ",".join(st.session_state.ans[4]))
    message += u"%s: %s\n" % (app_text.question[5], st.session_state.ans[5][0])
    message += u"%s: %s\n" % (app_text.question[6], st.session_state.ans[6].replace("\n", ". "))
    message += u"%s: %s\n" % (app_text.question[7], st.session_state.ans[7][0])
    message += u"%s: %s\n" % (app_text.question[8], st.session_state.ans[8].replace("\n", ". "))
    message += u"\n"
    
    f = open("ttm.database", "a+")
    f.write(message)
    f.close()
    
# Routine for the first page
def page_one():

    while (st.session_state.num == 0) or (st.session_state.num == 1):

        placeholder = st.empty()
        num         = st.session_state.num
        with placeholder.form(key=str(num)):

             st.write(""" # Bienvenue! """)

             for i in range(5):
                 st.session_state.ans[i] = st.multiselect(app_text.question[i]+'\n'+app_text.consigne[i], key=num*5+i, options=app_text.reponse[i], default=st.session_state.ans[i])

             if st.form_submit_button(u"Soumettre les réponses"):
                 st.session_state.num += 1

                 check = True
                 if st.session_state.ans[0] is None or          len(st.session_state.ans[0]) != 1: check = False ; st.session_state.ans[0] = None
                 if st.session_state.ans[1] is None                                              : check = False ; st.session_state.ans[1] = None
                 if st.session_state.ans[2] is None or          len(st.session_state.ans[2]) != 1: check = False ; st.session_state.ans[2] = None
                 if st.session_state.ans[3] is None or not 1 <= len(st.session_state.ans[3]) <= 3: check = False ; st.session_state.ans[3] = None
                 if st.session_state.ans[4] is None or not 1 <= len(st.session_state.ans[4]) <= 3: check = False ; st.session_state.ans[4] = None
                 if check:
                     st.session_state.num = 2
                     placeholder.empty()
                     return

                 if st.session_state.num >= 2: st.session_state.num = 0
                 placeholder.empty()
             else:
                 st.stop()

# Routine for the second page
def page_two():

    while (st.session_state.num == 2) or (st.session_state.num == 3):

        st.session_state.phase = tree.logic_tree(st.session_state.ans[:5], app_text.reponse[:5])

        placeholder = st.empty()
        num         = st.session_state.num
        with placeholder.form(key=str(num)):

            st.write("""
                     # Resultats

                     ##### Vous êtes dans la phase %s
                     %s
                     """ % (app_text.phase_nom[st.session_state.phase], app_text.phase_description[st.session_state.phase]))
            st.image("MTT.png")

            for i in range(4):
                if (i % 2) == 0: st.session_state.ans[5+i] = st.multiselect(app_text.question[5+i], key=num*5+i, options=app_text.reponse[5+i], default=st.session_state.ans[5+i])
                if (i % 2) == 1: st.session_state.ans[5+i] = st.text_area  (app_text.question[5+i], key=num*5+i, placeholder=st.session_state.ans[5+i])

            if st.form_submit_button(u"Soumettre les réponses"):
                st.session_state.num += 1

                check = True
                if st.session_state.ans[5] is None or len(st.session_state.ans[5]) != 1: check = False ; st.session_state.ans[5] = None
                if st.session_state.ans[6] is None or len(st.session_state.ans[6]) == 0: check = False ; st.session_state.ans[6] = None
                if st.session_state.ans[7] is None or len(st.session_state.ans[7]) != 1: check = False ; st.session_state.ans[7] = None
                if st.session_state.ans[8] is None or len(st.session_state.ans[8]) == 0: check = False ; st.session_state.ans[8] = None
                if check:
                    st.session_state.num = 4
                    placeholder.empty()
                    return

                if st.session_state.num >= 4: st.session_state.num = 2
                placeholder.empty()
            else:
                st.stop()

# Routine for the third page
def page_three():

    if st.session_state.num == 4:

        placeholder = st.empty()
        num         = st.session_state.num
        with placeholder.form(key=str(num)):

            oui = st.radio(app_text.question_fin, key=num*10, options=app_text.reponses_fin)

            if st.form_submit_button(u"Soumettre les réponses"):
                st.session_state.num += 1
                placeholder.empty()
                if oui == app_text.reponses_fin[0]: write_message()
                return
            else:
                st.stop()

page_one()
page_two()
page_three()
if st.session_state.num == 5: st.write(""" ## Merci pour votre contribution! """)
