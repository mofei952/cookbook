

def parse_int(s):
    try:
        int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)


parse_int('42')
parse_int('n/a')
