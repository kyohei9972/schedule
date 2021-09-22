NAME_SPACE = 7

#ビット管理しているコマを取り出す
def check_lessons(lessons,i):
    if(lessons & (1 << i)):
        return 1
    else:
        return 0

#空白を出力する
def insert_blank(num):
    
    res =''
    for i in range(num):
        res += '　'

    return res
    
#メールをtxt形式で出力する
def Create_Mail(d):
    email_file = open('./email.txt','w')
    email_file.write('出勤コーチに連絡をしています\n\n')

    
    
    #出勤者ごとに、出勤するコマを出力する
    for name,lessons in d.items():
        
        
        email_file.write(name)
        #インデントを調整する
        num_of_blank = NAME_SPACE - len(name)
        email_file.write(insert_blank(num_of_blank))
        email_file.write(':')
        
        #コマチェック
        for i in range(6):
            flag = check_lessons(lessons,i)
            #授業があるなら数字を出力
            if(flag):
                email_file.write(('{}講'.format(i+1)) )
            else:
            #ないなら×講と出力
                email_file.write('×講')

            email_file.write(' ')
                

        email_file.write('\n')
            

    email_file.write('\n\n＊このメールは現時点でのマイクラスの情報から自動的に作成、送信しています。')
    email_file.write('\n\n1講目  12:20～13:40\n2講目  13:55～15:15\n3講目  15:30～16:50\n4講目  17:20～18:40\n5講目  18:55～20:15\n6講目  20:30～21:50\n\n')
    email_file.write('授業準備を万全にするため、余裕をもって出勤してください。')
    email_file.close()

    
