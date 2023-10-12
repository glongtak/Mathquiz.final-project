import random
import time
class Mathquiz:
    def __init__(self, difficult):
        self.difficult = difficult
        self.corect = 0
        self.miss = 0
        self.time_Add = 0
        self.time_sub = 0
        self.time_multiply = 0
        self.time_divide = 0
        self.listforcalpoint = []
        self.sumtime = 0
    def random_mat(self):
        if self.difficult == 1:
            dif = 5
        elif self.difficult == 2:
            dif = 10
        elif self.difficult == 3:
            dif = 20
        else:
            print("Invalid difficulty level.")
            return 

        t1 = time.time()
        for i in range(5):
            x = random.randint(1, dif)
            y = random.randint(1, dif)
            r = x + y
            print(x, '+', y, '= ?')
            ans_user = int(input('Ans: '))
            if r == ans_user:
                self.corect += 1
                print('Correct')
            else:
                self.miss += 1
                print('Ans is:', r)
        t2 = time.time()
        self.time_Add = '{:.2f}'.format(t2 - t1)

        t1 = time.time()
        for i in range (5):
            x = random.randint(1,dif)
            y = random.randint(1,dif)
            r = x-y
            print(x,'-',y,'= ?')
            ans_user = int(input('Ans :'))
            if r == ans_user:
                self.corect+=1
                print ('correct')
            else :
                self.miss +=1
                print('Ans is :',r)
        t2 = time.time()
        self.time_sub = '{:.2f}'.format(t2-t1)

        t1 = time.time()
        for i in range (5):
            x = random.randint(1,dif)
            y = random.randint(1,dif)
            r = x*y
            print(x,'*',y,'= ?')
            ans_user = int(input('Ans :'))
            if r == ans_user:
                self.corect+=1
                print ('correct')
            else :
                self.miss +=1
                print('Ans is :',r)
        t2 = time.time()
        self.time_multiply = '{:.2f}'.format(t2-t1)

        t1 = time.time()
        for i in range (5):
            x = random.randint(1,dif)
            y = random.randint(1,dif)
            r = x/y
            print(x,'/',y,'= ?')
            ans_user = float(input('Ans :'))
            if r == ans_user:
                self.corect+=1
                print ('correct')
            else :
                self.miss +=1
                print('Ans is :',r)
        t2 = time.time()
        self.time_divide = '{:.2f}'.format(t2-t1)
        print('corect :',self.corect)
        print('miss :',self.miss)

        self.time_Add = float(self.time_Add)
        self.time_divide = float(self.time_divide)
        self.time_multiply = float(self.time_multiply)
        self.time_sub = float(self.time_sub)

        self.listforcalpoint.append(self.time_Add)
        self.listforcalpoint.append(self.time_sub)
        self.listforcalpoint.append(self.time_multiply)
        self.listforcalpoint.append(self.time_divide)
        self.sumtime = sum(self.listforcalpoint)

        print('Time part + :',self.time_Add)
        print('Time part - :',self.time_sub)
        print('Time part * :',self.time_multiply)
        print('Time part / :',self.time_divide)
    
    def cal_score(self):
        self.score = 0
        point_time = 0
        self.all_point_time = []
        for i in range(len(self.listforcalpoint)):
            if self.listforcalpoint[i] <= 10 :
                point_time = 5
            elif self.listforcalpoint[i] > 10 and self.listforcalpoint[i] <= 12 :
                point_time = 4 
            elif self.listforcalpoint[i] > 12 and self.listforcalpoint[i] <= 15 :
                point_time = 3
            elif self.listforcalpoint[i] > 15 and self.listforcalpoint[i] <= 18 :
                point_time = 2
            elif self.listforcalpoint[i] > 18 and self.listforcalpoint[i] <= 20 :
                point_time = 1
            self.all_point_time.append(point_time)

        self.score = self.corect + sum(self.all_point_time)

        return self.score
    def keeptime(self):
        return self.sumtime
    def reset(self):
        self.corect = 0
        self.miss = 0
        self.all_point_time = []
        self.score = 0
        self.listforcalpoint = []
        self.sumtime = 0 

class OnePlayers(Mathquiz):
    def __init__(self, difficult):
        super().__init__(difficult)
        self.player_name = None

    def get_player_name(self):
        if self.player_name is None:
            self.player_name = input("Player name: ")
        return self.player_name
    def show_score_one(self,p,nfsc,t):
        self.nameforshowscore = nfsc
        self.point = p
        self.time = t
        print('Name Player :',self.nameforshowscore)
        print('Score :',self.point,'เวลาที่ใช้ :','{:.2f}'.format(self.time))

class TwoPlayers(Mathquiz):
    def __init__(self, difficult):
        super().__init__(difficult)
        self.player1_name = None
        self.player2_name = None

    def get_player1_name(self):
        if self.player1_name is None:
            self.player1_name = input("Player 1 name: ")
        return self.player1_name

    def get_player2_name(self):
        if self.player2_name is None:
            self.player2_name = input("Player 2 name: ")
        return self.player2_name
    
    def show_score_p1(self,p,nfsc,t):
        self.nameforshowscore = nfsc
        self.point = p
        self.time = t
        print('Name Player :',self.nameforshowscore)
        print('Score :',self.point,'เวลาที่ใช้ :','{:.2f}'.format(self.time))
    def show_score_p2(self,p,nfsc,t):
        self.nameforshowscore = nfsc
        self.point = p
        self.time = t
        print('Name Player :',self.nameforshowscore)
        print('Score :',self.point,'เวลาที่ใช้ :','{:.2f}'.format(self.time))

class Multiple(Mathquiz):
    def __init__(self, difficult):
        super().__init__(difficult)
        self.players = []

    def get_player_names(self):
        self.num_players = int(input("Enter The Number Of Players: "))
        for i in range(self.num_players):
            player_name = input(f"Player Name {i + 1}: ")
            self.players.append(player_name)
    def numnplay(self):
        return self.num_players
    def listmul(self):
        return self.players
    def display_players(self):
        print("Players:")
        for player_number, player_name in self.players.items():
            print(f"Players {player_number}: {player_name}")

    def showscore(self,p,nfsc,t):
        self.player = nfsc
        self.point = p
        self.time = t
        
        print('Name Player :',self.player)
        print('Score :',self.point,'เวลาที่ใช้ :','{:.2f}'.format(self.time))
def show_rule():
    print('วิธีการเล่น และการได้รับคะแนน')
    print('จะมีคำถามคณิตศาสตร์ถามมาเลื่อย ๆ')
    print('ทุกคำตอบที่ ตอบถูกได้ 1 คะแนน')
    print('จะเริ่มจาก การ + - * / ตามลำดับ มีตอนละ 5 ข้อ ทั้งหมด 20 ข้อ')
    print('และจะได้รับโบนัสคะแนนในแต่ละตอน หากคุณตอบได้รวดเร็ว ')
    print('ภายใน 10 วินาที ได้ 5 คะแนน')
    print('ภายใน 10 - 12 วินาที ได้ 4 คะแนน')
    print('ภายใน 12 - 15 วินาที ได้ 3 คะแนน')
    print('ภายใน 15 - 18 วินาที ได้ 2 คะแนน')
    print('ภายใน 18 - 20 วินาที ได้ 1 คะแนน')
    print('หากช้ากว่านี้ไม่ได้โบนัสคะแนน')

def main_program():
    print()
    print('Game_mode')
    print('1.One player mode')
    print('2.Two players mode')
    print('3.Multiple players mode')
    print()

    choice = input('Choose a game mode (1/2/3): ')

    if choice == '1':
        difficulty = int(input('Choose difficulty (1-3): '))
        onepy = OnePlayers(difficulty)
        name_one_player = onepy.get_player_name()
        print('Are You Ready!!!, Start in 5 sec') 
        time.sleep(5)
        onepy.random_mat()
        pointoneplayer = onepy.cal_score()
        oneplaytime = onepy.keeptime()
        print('-----------YOU DONE-----------')
        onepy.reset()
        print()
        print('---------Show Score---------')
        onepy.show_score_one(pointoneplayer,name_one_player,oneplaytime)
        
    elif choice == '2':
        difficulty = int(input('Choose difficulty (1-3): '))
        two_players = TwoPlayers(difficulty)
        Namep1 = two_players.get_player1_name()
        Namep2 = two_players.get_player2_name()
    
        print('Player 1 turn, Start in 5 sec') 
        time.sleep(5)
        two_players.random_mat()
        pointp1 = two_players.cal_score()
        timep1 = two_players.keeptime()
        two_players.reset()
        print('-----------P1 DONE-----------')
        time.sleep(2)
        print('Player 2 turn, Start in 5 sec')
        time.sleep(5)
        two_players.random_mat()
        pointp2 = two_players.cal_score()
        timep2 = two_players.keeptime()
        two_players.reset()
        print('-----------P2 DONE-----------')
        print()
        print('---------Show Score---------')
        two_players.show_score_p1(pointp1,Namep1,timep1)
        two_players.show_score_p2(pointp2,Namep2,timep2)
        if pointp1 > pointp2 :
            print('The winner is ',Namep1)
        elif pointp2 > pointp1 :
            print('The winner is ',Namep2)
        elif pointp1 == pointp2:
            if timep1 > timep2 :
                print('The winner is ',Namep1)
            elif timep2 > timep1 :
                print('The winner is ',Namep1)
        else:
            print('EQUAL SCORE')
        
    elif choice == '3':
        difficulty = int(input('Choose difficulty (1-3): '))
        player_info = Multiple(difficulty)
        player_info.get_player_names()
        l = player_info.listmul()
        ps = []
        pt = []
        #player_info.display_players()
        for i in range(player_info.numnplay()):
            print('Player',i+1,'turn start in 5 sec')
            time.sleep(5)
            player_info.random_mat()
            p = player_info.cal_score()
            ps.append(p)
            t = player_info.keeptime()
            pt.append(t)
            print('-----------Player',i+1,' DONE-----------')
            time.sleep(2)
            player_info.reset()
            player_info.showscore(ps[i],l[i],pt[i])

    else: 
        print('Invalid choice. Please choose 1, 2, or 3.')

def menu():
    print('This is Program Quizmath')
    print('1.Rule')
    print('2.play game')
    print('Or put anything to exit this program')
    choose = input('choose :')
    if choose == '1':
        show_rule()
        print('you want to play?')
        print('1.yes')
        print('Or put anything to exit this program')
        choosetoplay = input('choose :')
        if choosetoplay == '1':
            main_program()
        else :
            exit()
    elif choose == '2':
        main_program()
    else:
        exit()
menu()

print('You want to play again ?')
print('1.yes')
print('Or put anything to exit program')

again = input('choose :')
if again == '1' :
    menu()
else :
    exit()
