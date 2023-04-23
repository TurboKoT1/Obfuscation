import base64, zlib, time, os

while True:
    print("|| Please enter path to the file")
    path = input("/> ")
    if path == "" or len(path)<4:
        print("You're entered incorrect path!")
    elif not path.endswith(".py"):
        print("File should ends with .py!")
    elif not os.path.exists(path):
        print("File not found!")
    else:
        start_time = time.time()
        print("[INFO] * Getting the file name..")
        filename = path.split("/")[-1].split(".")[0]

        print("[INFO] * Getting the file code..")
        code = open(path, 'r', encoding='utf-8').read()
        print("[INFO] * Encoding the file code..")
        encoded_code = base64.b85encode(code.encode("utf-8"))
        print("[INFO] * Compressing encoded file code..")
        compress = zlib.compress(encoded_code)

        unde = f'''exec(base64.b85decode(zlib.decompress({compress})).decode())'''
        unde_encoded = base64.b85encode(unde.encode("utf-8"))
        unde_compress = zlib.compress(unde_encoded)

        try:
            with open(filename + "-obf.py", "x") as obf:
                obf.write(f'''TurboObfuscate=132;import zlib,base64;exec(base64.b85decode(zlib.decompress({unde_compress})).decode())''')
                obf.close()
        except:
            with open(filename + "-obf.py", "w+") as obf:
                obf.write(f'''TurboObfuscate=132;import zlib,base64;exec(base64.b85decode(zlib.decompress({unde_compress})).decode())''')
                obf.close()
        print(f"[INFO] * Successfully obfuscated in {time.time() - start_time} ms!")
