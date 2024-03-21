import speeches

def greeting():
    print(speeches.greeting)
    for i in speeches.menu:
        print('\t'+i)
    answer=input().lower()
    return answer