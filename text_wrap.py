import textwrap

def wrap(string, max_width):
    list=textwrap.wrap(string,width=max_width)
    text=''
    for i in list:
        text=text+i+'\n'
    return text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
