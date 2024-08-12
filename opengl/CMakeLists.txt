cmake_minimum_required(VERSION 3.5.0)
project(learn_opengl VERSION 0.1.0 LANGUAGES C CXX)


# Compile external dependencies 
add_subdirectory (dependencies)


include_directories(
  include/
  dependencies/glad/include/
  dependencies/glfw/include/
)

set(ALL_LIBS
	${OPENGL_LIBRARY}
	glfw
)

# Tutorial 1
add_executable(01_open_window 
	src/tutorials/01_open_window/main.cpp
)
target_link_libraries(01_open_window
	${ALL_LIBS}
)


# Visual Studio
SOURCE_GROUP(common REGULAR_EXPRESSION "src/common/.*" )
SOURCE_GROUP(shaders REGULAR_EXPRESSION ".*/.*shader$" )
