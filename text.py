from captionstransformer.sbv import Reader


test_content = open("t.txt", "r")
print(test_content.read())

reader = Reader(test_content)
#print (reader.read())

captions = reader.read()