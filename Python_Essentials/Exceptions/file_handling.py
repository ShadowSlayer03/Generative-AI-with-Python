try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
        file.close()

    with open("hoho.txt", "w", encoding="utf-8") as file:
        try:
            file.write("Masala chai is great!\n")
        except Exception as e:
            print("Error while writing to file:", e)
        finally:
            file.close()
except FileNotFoundError:
    print("File not found!")
