from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from disease_prediction import *

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
#    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# GUI setup
if __name__ == '__main__':
    root = Tk()
    root.title("Disease Predictor")
    root.geometry("900x600")  # Adjust size as needed

    # Load and set background image
    bg_image = Image.open("bg3.jpg")  # Replace with your image path
    bg_image = bg_image.resize((900, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Heading
    w2 = Label(root, justify=CENTER, text="Disease Predictor using Machine Learning", fg="black", bg='SystemButtonFace')
    w2.config(font=("Helvetica", 24, "bold"))
    w2.pack(pady=20)

    # Create a frame for input fields
    input_frame = Frame(root, bg='SystemButtonFace')
    input_frame.pack(pady=20)

    # labels and entries
    entries = [
        ("Symptom 1", Symptom1 := StringVar()),
        ("Symptom 2", Symptom2 := StringVar()),
        ("Symptom 3", Symptom3 := StringVar()),
        ("Symptom 4", Symptom4 := StringVar()),
        ("Symptom 5", Symptom5 := StringVar()),
    ]

    for i, (text, var) in enumerate(entries):
        label = Label(input_frame, text=text, fg="black", bg='SystemButtonFace', font=("Helvetica", 12))
        label.grid(row=i, column=0, pady=5, sticky=W)
        entry = ttk.Combobox(input_frame, textvariable=var, values=sorted(l1), font=("Helvetica", 12))
        entry.grid(row=i, column=1, pady=5, padx=10)

    # Button frame
    button_frame = Frame(root, bg='SystemButtonFace')
    button_frame.pack(pady=20)

    # Buttons
    buttons = [
        ("DecisionTree", DecisionTree),
        ("RandomForest", randomforest),
        ("NaiveBayes", NaiveBayes)
    ]

    for text, command in buttons:
        btn = Button(button_frame, text=text, command=command, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        btn.pack(side=LEFT, padx=10)

    # Result frame
    result_frame = Frame(root, bg='SystemButtonFace')
    result_frame.pack(pady=20)

    # Results
    results = [
        ("DecisionTree Result:", t1 := Entry(result_frame, width=40, font=("Helvetica", 12), readonlybackground='SystemButtonFace', state='readonly')),
        ("RandomForest Result:", t2 := Entry(result_frame, width=40, font=("Helvetica", 12), readonlybackground='SystemButtonFace', state='readonly')),
        ("NaiveBayes Result:", t3 := Entry(result_frame, width=40, font=("Helvetica", 12), readonlybackground='SystemButtonFace', state='readonly'))
    ]

    for i, (text, t) in enumerate(results):
        Label(result_frame, text=text, fg="black", bg='SystemButtonFace', font=("Helvetica", 12)).grid(row=i, column=0, pady=5, sticky=W)
        t.grid(row=i, column=1, pady=5, padx=10)

    root.mainloop()