cmake_minimum_required(VERSION 3.5.0)
project(learn_opengl VERSION 0.1.0 LANGUAGES C CXX)


# Compile external dependencies 
add_subdirectory(dependencies)


include_directories(
  include/
  dependencies/glad/include/
  dependencies/glfw/include/
)

file(GLOB VENDORS_SOURCES dependencies/glad/src/glad.c)
set(ALL_LIBS
	${OPENGL_LIBRARY}
	glfw
)

add_subdirectory(src)

# Visual Studio
SOURCE_GROUP(common REGULAR_EXPRESSION "src/common/.*" )
SOURCE_GROUP(shaders REGULAR_EXPRESSION ".*/.*shader$" )
