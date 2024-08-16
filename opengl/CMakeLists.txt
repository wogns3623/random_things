cmake_minimum_required(VERSION 3.5.0)
project(learn_opengl VERSION 0.1.0 LANGUAGES C CXX)


# Compile external dependencies 
add_subdirectory(dependencies)


include_directories(
  src/
  dependencies/glad/include/
  dependencies/glfw/include/
)

add_library(glad dependencies/glad/src/glad.c)
set(LIBS
	${OPENGL_LIBRARY}
	glfw
  glad
)

add_subdirectory("src")

# file(GLOB COMMON
#   "src/common/*.h"
#   "src/common/*.cpp"
# )

# function(create_project_from_sources chapter)
#   file(GLOB SOURCE
#     "src/tutorials/${chapter}/*.h"
#     "src/tutorials/${chapter}/*.cpp"
#   )
#   file(GLOB SHADERS
#     "src/tutorials/${chapter}/*.vs"
#     "src/tutorials/${chapter}/*.fs"
#     "src/tutorials/${chapter}/*.tcs"
#     "src/tutorials/${chapter}/*.tes"
#     "src/tutorials/${chapter}/*.gs"
#     "src/tutorials/${chapter}/*.cs"
#   )
#   set(NAME ${chapter})

#   add_executable(${NAME} ${SOURCE} ${SHADERS} ${COMMON})
#   target_link_libraries(${NAME} ${LIBS})

#   set_target_properties(${NAME} PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

#   foreach(SHADER ${SHADERS})
#     add_custom_command(TARGET ${NAME} PRE_BUILD COMMAND ${CMAKE_COMMAND} -E copy ${SHADER} $<TARGET_FILE_DIR:${NAME}>)
#     add_custom_command(TARGET ${NAME} PRE_BUILD COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DLLS} $<TARGET_FILE_DIR:${NAME}>)
#   endforeach(SHADER)
# endfunction()


# file(GLOB TUTORIAL_DIRS LIST_DIRECTORIES true "src/tutorials/*")

# foreach(TUTORIAL_DIR ${TUTORIAL_DIRS})
#   IF(IS_DIRECTORY ${TUTORIAL_DIR})
#     # message(${TUTORIAL_DIR})
#     get_filename_component(TUTORIAL_NAME ${TUTORIAL_DIR} NAME)
#     create_project_from_sources(${TUTORIAL_NAME})
#   ENDIF()
# endforeach(TUTORIAL_DIR)
