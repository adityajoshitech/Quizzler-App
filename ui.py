from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz

        self.window=Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        wrong_image=PhotoImage(file="images/false.png")
        right_image=PhotoImage(file="images/true.png")

        self.canvas=Canvas(height=250,width=300,highlightthickness=0)
        self.question_text=self.canvas.create_text(150,125,text="Text",fill="black",font=("Arial",20,"italic"),width=280)

        self.score_label=Label(text="Score: 0",bg=THEME_COLOR,highlightthickness=0,fg="White",font=("Arial",15))
        self.score_label.grid(row=0,column=1)

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.tick_button=Button(image=right_image,highlightthickness=0,bg=THEME_COLOR,command=self.right_answer)
        self.tick_button.grid(row=2,column=0)
        self.cross_button=Button(image=wrong_image,highlightthickness=0,bg=THEME_COLOR,command=self.wrong_answer)
        self.cross_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the Quiz :)")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
    def wrong_answer(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def right_answer(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)