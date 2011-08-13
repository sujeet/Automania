main: user_main.cpp botBrain.h info.h bfs.h map.h constants.h position.h botBrain info bfs
	g++ -o main user_main.cpp botBrain info bfs
botBrain: info.h bfs.h map.h position.h constants.h botBrain.cpp
	g++ -o botBrain botBrain.cpp 
info: constants.h map.h position.h bfs.h info.cpp
	g++ -o info info.cpp
bfs: map.h constants.h position.h bfs.cpp
	g++ -o bfs bfs.cpp
	
