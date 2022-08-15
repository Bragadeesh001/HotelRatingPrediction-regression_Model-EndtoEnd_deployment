

import pickle
import streamlit as st

 
#loading the model
pickle_in = open('regression_Model.pkl', 'rb')
classifier = pickle.load(pickle_in)
 
@st.cache()
def Home():
    return render_template('index.html')
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(online_order,book_table,votes,approx_cost,Overall_review,listed_in):   
 
    if online_order == "yes":
        online_order = 1
    else:
        online_order = 0
 
    if book_table == "yes":
        book_table = 0
    else:
        book_table = 1

    if Overall_review == "0.0":
       Overall_review = 0
    elif Overall_review == '1.0':
        Overall_review = 1
    elif Overall_review == '2.0':
        Overall_review = 2
    elif Overall_review == '3.0':
        Overall_review = 3
    elif Overall_review == '4.0':
        Overall_review = 4
    else:
      Overall_review = 5
      
    if listed_in == "Buffet":
        listed_in = 0
    elif listed_in == "Cafes":
        listed_in = 1
    elif listed_in == "Delivery":
        listed_in = 2
    elif listed_in == "Desserts":
        listed_in = 3
    elif listed_in == "Dine-out":
        listed_in = 4
    elif listed_in == "Drinks & nightlife":
        listed_in = 5
    else:
        listed_in = 6  
 
 
    # Making predictions 
    prediction = classifier.predict( 
        [[online_order,book_table,votes,approx_cost,Overall_review,listed_in]])
    
    return prediction
     
    
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Automated Loan Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    online_order = st.selectbox('online_order',("yes","no"))
    book_table = st.selectbox('book_table',("yes","no")) 
    Overall_review  = st.selectbox('Overall_review',("0.0","1.0","2.0","3.0","4.0","5.0"))
    votes = st.number_input("votes") 
    approx_cost = st.number_input("approx_cost")
    listed_in = st.selectbox('listed_in',('Buffet', 'Cafes', 'Delivery', 'Desserts', 'Dine-out','Drinks & nightlife', 'Pubs and bars'))
    
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(online_order,book_table,votes,approx_cost,Overall_review,listed_in) 
        st.success('Your loan is {}',result)
        
     
if __name__=='__main__': 
    main()