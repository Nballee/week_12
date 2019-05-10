def main():
    course_num = input('Enter the course number(Ex. CS101): ')
    rooms = room_num()
    instruct = instructor()
    meeting = meeting_time()
    print(course_num, ' will be held in room ', rooms[course_num], ' and taught by ', instruct[course_num], ' at ', meeting[course_num], sep='')


def room_num():
    rooms = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    return rooms


def instructor():
    instruct = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    return instruct

def meeting_time():
    meeting = {'CS101':'8:00 am', 'CS102':'9:00 am', 'CS103':'10:00 am', 'NT110':'11:00 am', 'CM241':'1:00 pm'}
    return meeting


main()

