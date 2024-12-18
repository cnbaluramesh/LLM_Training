import io 

with io.open("data.txt","a",encoding="utf-8") as f1:
    f1.write("\n")
    f1.write("i know python")
    f1.close()
