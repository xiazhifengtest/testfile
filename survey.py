class AnonymousSurvey():
    '''收集匿名问卷的答案'''
    def __init__(self,question):
        self.question=question
        self.responses=[]
    def show_question(self):
        '''显示调查问卷'''
        print(self.question)
    def store_response(self,new_response):
        '''存储单份问卷'''
        self.responses.append(new_response)
    def show_results(self):
        '''显示收集的所有答案'''
        print('Survey result: ')
        for response in self.responses:
            print('- '+response)