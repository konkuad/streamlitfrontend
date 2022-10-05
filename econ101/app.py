import streamlit as st

functions = {
    "Price Elasticity of Demand":1,
    "Cross Elasticity of Demand":2,
    "Income Elasticity of Demand":3,
    "Price Elasticity of Supply":4,
}

posneg = {
    "Decrease":-1,
    "Increase":1,
}

def midpointED(PQ):
    q1, q2 = PQ["Q"]
    p1, p2 = PQ["P"]
    dq = (q2-q1)/((q1+q2)/2)
    dp = (p2-p1)/((p1+p2)/2)
    return dq/dp

def percentED(P,Q):
    return Q/P

def analyzeAbsoluteED(ED):
    if(abs(ED)>=1):
        return "Goods is elastic. Increase in price will decrease in revenue and vice versa."
    else:
        return "Goods is inelastic. Increase in price will increase in revenue and vice versa."

def analyzeIncomeED(ED):
    if(ED>=1):
        return "Goods is a normal goods. Increase in income will increase in quantity demanded."
    elif((ED<=1)and(ED>=0)):
        return "Goods is a necessity. Increase in income will increase in quantity demanded."
    else:
        return "Goods is an inferior goods. Increase in income will decrease in quantity demanded."

def analyzeCrossED(ED):
    if(ED>=0):
        return "The two goods are substitudes. Increasing a price of one will increase the quantity demanded for the other."
    else:
        return "The two goods are complements. Increasing a price of one will decrease the quantity demanded for the other."

st.title("ECON101 Calculator")

with st.sidebar:

    st.write('## Choose Function')
    f = functions[st.selectbox("Choose your function: ",list(functions.keys()))]

if(f==1):
    with st.sidebar:
        mode = st.selectbox("Choose your mode:" ,["percentage","raw values"])
    if(mode=="percentage"):
        st.write("### Quantity")
        multQ = posneg[st.selectbox("Q increase or decrease: ",list(posneg.keys()))]
        Q = st.number_input("Input % Change in Quantity",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multQ
        st.write("### Price")
        multP = posneg[st.selectbox("P increase or decrease: ",list(posneg.keys()),index=1)]
        P = st.number_input("Input % Change in Price",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multP
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            ED = abs(percentED(P,Q))
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeAbsoluteED(ED))
    elif(mode=="raw values"):
        st.write("### Quantity")
        Q1 = st.number_input("Input Initial Quantity (Q1)",min_value=0.0)
        Q2 = st.number_input("Input Final Quantity (Q2)",min_value=0.0)
        st.write("### Price")
        P1 = st.number_input("Input Initial Price (P1)",min_value=0.0)
        P2 = st.number_input("Input Final Price (P2)",min_value=0.0)
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            PQ = {
                "Q":(Q1,Q2),
                "P":(P1,P2),
            }
            ED = abs(midpointED(PQ))
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeAbsoluteED(ED))
    else:
        pass
    
if(f==2):
    with st.sidebar:
        mode = st.selectbox("Choose your mode:" ,["percentage","raw values"])
    if(mode=="percentage"):
        st.write("### Quantity of First Goods")
        multQ = posneg[st.selectbox("Q increase or decrease: ",list(posneg.keys()))]
        Q = st.number_input("Input % Change in Quantity",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multQ
        st.write("### Price of Second Goods")
        multP = posneg[st.selectbox("P increase or decrease: ",list(posneg.keys()),index=1)]
        P = st.number_input("Input % Change in Price",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multP
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            ED = percentED(P,Q)
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeCrossED(ED))
    elif(mode=="raw values"):
        st.write("### Quantity of First Goods")
        Q1 = st.number_input("Input Initial Quantity (Q1)",min_value=0.0)
        Q2 = st.number_input("Input Final Quantity (Q2)",min_value=0.0)
        st.write("### Price of Second Goods")
        P1 = st.number_input("Input Initial Price (P1)",min_value=0.0)
        P2 = st.number_input("Input Final Price (P2)",min_value=0.0)
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            PQ = {
                "Q":(Q1,Q2),
                "P":(P1,P2),
            }
            ED = midpointED(PQ)
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeCrossED(ED))
    else:
        pass

if(f==3):
    with st.sidebar:
        mode = st.selectbox("Choose your mode:" ,["percentage","raw values"])
    if(mode=="percentage"):
        st.write("### Quantity")
        multQ = posneg[st.selectbox("Q increase or decrease: ",list(posneg.keys()))]
        Q = st.number_input("Input % Change in Quantity",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multQ
        st.write("### Income")
        multP = posneg[st.selectbox("I increase or decrease: ",list(posneg.keys()),index=1)]
        P = st.number_input("Input % Change in Price",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multP
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            ED = percentED(P,Q)
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeIncomeED(ED))
    elif(mode=="raw values"):
        st.write("### Quantity")
        Q1 = st.number_input("Input Initial Quantity (Q1)",min_value=0.0)
        Q2 = st.number_input("Input Final Quantity (Q2)",min_value=0.0)
        st.write("### Income")
        P1 = st.number_input("Input Initial Income (I1)",min_value=0.0)
        P2 = st.number_input("Input Final Income (I2)",min_value=0.0)
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            PQ = {
                "Q":(Q1,Q2),
                "P":(P1,P2),
            }
            ED = midpointED(PQ)
            st.write(f"### Elasticity is {round(ED,2)}")
            st.write("### "+analyzeIncomeED(ED))
    else:
        pass

if(f==4):
    with st.sidebar:
        mode = st.selectbox("Choose your mode:" ,["percentage","raw values"])
    if(mode=="percentage"):
        st.write("### Quantity Supplied")
        multQ = posneg[st.selectbox("Q increase or decrease: ",list(posneg.keys()))]
        Q = st.number_input("Input % Change in Quantity",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multQ
        st.write("### Price")
        multP = posneg[st.selectbox("P increase or decrease: ",list(posneg.keys()))]
        P = st.number_input("Input % Change in Price",min_value=0.0,max_value=100.0,value=50.0,step=0.01)*multP
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            ED = percentED(P,Q)
            st.write(f"### Elasticity is {round(ED,2)}")
    elif(mode=="raw values"):
        st.write("### Quantity Supplied")
        Q1 = st.number_input("Input Initial Quantity (Q1)",min_value=0.0)
        Q2 = st.number_input("Input Final Quantity (Q2)",min_value=0.0)
        st.write("### Price")
        P1 = st.number_input("Input Initial Price (P1)",min_value=0.0)
        P2 = st.number_input("Input Final Price (P2)",min_value=0.0)
        calculate_form = st.form(key='calculate')
        calculate = calculate_form.form_submit_button('Calculate!')
        if calculate:
            PQ = {
                "Q":(Q1,Q2),
                "P":(P1,P2),
            }
            ED = abs(midpointED(PQ))
            st.write(f"### Elasticity is {round(ED,2)}")
    else:
        pass

else:
    pass