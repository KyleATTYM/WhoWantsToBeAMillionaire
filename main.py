from question_list import questions
from Question import Question
from QuestionMaster import QuestionMaster
question_bank = []
for qns in questions:
    question_bank.append(Question(qns["question"],qns["answer"]))

question_master = QuestionMaster(q_list=question_bank)
question_master.start_quiz()