from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Set it to Empty Array which is Empty List
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Instantiating an object new_question for each of the for loop:
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


# After Appending all into the question_bank List []
# Instantiating the quiz object using the QuizBrain class
quiz = QuizBrain(question_bank)


# Invoking the QuizBrain Method, using the Object being created:
# The while loop will evaluate the expression to be True or False
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed your quiz")
print(f"Your final Score was: {quiz.score}/{quiz.question_number}")

