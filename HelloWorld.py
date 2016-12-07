#Created by: Moises Medina 

class Question:
    def __init__(self, question, answers, match_response, no_match_response):
        self.question = question
        self.answers = answers
        self.match_response = match_response
        self.no_match_response = no_match_response

    def print_question(self):
        return input(self.question + " ")

    def print_response(self, user_answer):
        user_answer = self.__clean_string(user_answer)         
        match = False  
        for  answer in self.answers:
            answer = self.__clean_string(answer) 
            if answer == user_answer:
                match = True

        if match:
            print (self.match_response + "\n")
        else:
            print (self.no_match_response+ "\n")

    def __clean_string(self, string_to_clean):
        string_to_clean = string_to_clean.strip()
        string_to_clean = string_to_clean.lower()
        return string_to_clean
            
print ("Hello World! Get to know me by responding to three questions.\n")
question_one = Question("What is your favorite college football team?"
                        ,["Florida Gators","Gators" ]
                        ,"Mine too! Go Gators!"
                        ,"Boo! Just kidding but mine are the Florida Gators.")
question_one.print_response(question_one.print_question())

question_two = Question("Do you own a pet?"
                        ,["Yes","Y"]
                        ,"Aren't pets fun! I own a dog named Lulu."
                        ,"Okay. I own a dog named Lulu.")
question_two.print_response(question_two.print_question()) 

question_three = Question("What's one of your hobbies?"
                          ,["Coding","Reading","Running"]
                          , "Cool! That's one of mine too!"
                          , "Bet that's fun! Mine are coding, reading and running.")
question_three.print_response(question_three.print_question())

input("Thank you and have a good day! Press any key to exit...")




