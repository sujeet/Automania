CC = g++
strict_options = -Wall -pedantic

final: user_main.o botBrain.o info.o bfs.o map.o position.o map.o position.o
	$(CC) -o $@ $^

user_main.o: user_main.cpp botBrain.h info.h bfs.h map.h constants.h position.h
	$(CC) -o $@ -c $< $(strict_options)

botBrain.o: botBrain.cpp info.h bfs.h map.h position.h constants.h
	$(CC) -o $@ -c $< $(strict_options)

info.o: info.cpp constants.h map.h position.h bfs.h
	$(CC) -o $@ -c $< $(strict_options)

bfs.o: bfs.cpp map.h constants.h position.h
	$(CC) -o $@ -c $< $(strict_options)

map.o: map.cpp position.h constants.h 
	$(CC) -o $@ -c $< $(strict_options)

position.o: position.cpp constants.h
	$(CC) -o $@ -c $< $(strict_options)

clean :
	rm -rf *.o *.~ final
