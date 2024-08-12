get_filename_component(CURRENT_DIR_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)

add_executable(${CURRENT_DIR_NAME}
	main.cpp
	${VENDORS_SOURCES}
)

target_link_libraries(${CURRENT_DIR_NAME}
	${ALL_LIBS}
)

set_target_properties(${CURRENT_DIR_NAME}
	PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
)
