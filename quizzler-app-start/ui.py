from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0 ', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Sample',
            width=280,
            fill=THEME_COLOR,
            font=("Gill Sans MT", 16, 'italic')
        )

        self.canvas.grid(column=0, row=1, columnspan=2, pady = 50)

        cross_image = PhotoImage(file='images/false.png')
        tick_image = PhotoImage(file='images/true.png')
        self.tick_button = Button(image=tick_image, highlightthickness=0, command = self.true_pressed)
        self.tick_button.grid(column=0, row=2, padx=20, pady=20)
        self.cross_button = Button(image=cross_image,  highlightthickness=0,  command = self.false_pressed)
        self.cross_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end")
            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))



    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.window.after(250, self.get_next_question)