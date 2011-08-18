play: user_main.o botBrain.o info.o bfs.o map.o position.o map.o position.o
	g++ -o final user_main.o botBrain.o info.o bfs.o map.o position.o 
user_main.o: user_main.cpp botBrain.h info.h bfs.h map.h constants.h position.h
	g++ -c user_main.cpp
botBrain.o: info.h bfs.h map.h position.h constants.h botBrain.cpp
	g++ -c botBrain.cpp 
info.o: constants.h map.h position.h bfs.h info.cpp
	g++ -c info.cpp
bfs.o: map.h constants.h position.h bfs.cpp
	g++ -c bfs.cpp
map.o: position.h constants.h map.cpp
	g++ -c map.cpp
position.o: constants.h position.cpp
	g++ -c position.cpp
	
