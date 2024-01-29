import base64

if __name__ == '__main__':
    hex = "57656c636f6d6520746f207468652063727970746f20636f7572736521"
    byte_ = bytes.fromhex(hex)
    ascii_ = byte_.decode()
    base64_ = base64.b64encode(byte_)

    print("hex = ", hex)
    print("byte_arr = ", byte_)
    print("ascii = ", ascii_)
    print("base64 = ", base64_.decode())