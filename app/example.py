def sum_strings(a, b):
    try:
        return int(a) + int(b)
    except Exception:
        from pudb.remote import set_trace
        set_trace(term_size=(160, 40), host='0.0.0.0', port=6900)
        print(a)
        print(b)
        return float(a) + float(b)


print("----- starting example -----")
res = sum_strings("1", "2.0")
print("res={}".format(res))
print("----- ending example -----")
