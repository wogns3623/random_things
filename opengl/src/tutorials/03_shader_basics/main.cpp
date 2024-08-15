#include <glad/glad.h>

#include <GLFW/glfw3.h>

#include <iostream>
#include <math.h>

void framebuffer_size_callback(GLFWwindow *window, int width, int height);
void processInput(GLFWwindow *window);
void GLAPIENTRY MessageCallback(GLenum source, GLenum type, GLuint id,
                                GLenum severity, GLsizei length,
                                const GLchar *message, const void *userParam);

const char *vertex_shader_source = "\
#version 330 core\n\
layout (location = 0) in vec3 aPos;\n\
\n\
// out vec4 vertex_color;\n\
\n\
void main() {\n\
  gl_Position = vec4(aPos.xyz, 1.0);\n\
  // vertex_color = vec4(0.5, 0.0, 0.0, 1.0);\n\
}\0\
";
const GLsizei vertex_shader_string_count = 1;

const char *fragment_shader_source = "\
#version 330 core\n\
\n\
// // input from vertex shader\n\
// in vec4 vertex_color;\n\
\n\
// input from application\n\
uniform vec4 our_color;\n\
\n\
out vec4 frag_color;\n\
\n\
void main() {\n\
  frag_color = our_color;\n\
}\0\
";
const GLsizei fragment_shader_string_count = 1;

int success;
char infoLog[512];

int main() {
  // ==== initialize glfw & opengl ====
  glfwInit();

  // During init, enable debug output

  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

  auto window = glfwCreateWindow(800, 600, "First Triangle", NULL, NULL);

  if (window == NULL) {
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
  }

  glfwMakeContextCurrent(window);
  glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

  if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
    std::cout << "Failed to initialize GLAD" << std::endl;
    return -1;
  }

  glEnable(GL_DEBUG_OUTPUT);
  glDebugMessageCallback(MessageCallback, 0);
  glViewport(0, 0, 800, 600);
  // ==== end initializing ====

  // ==== compile shader program ====
  // vertex shader
  GLuint vertex_shader = glCreateShader(GL_VERTEX_SHADER);
  glShaderSource(vertex_shader, vertex_shader_string_count,
                 &vertex_shader_source, NULL);
  glCompileShader(vertex_shader);

  glGetShaderiv(vertex_shader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(vertex_shader, sizeof(infoLog), NULL, infoLog);
    std::cout << "Error: Cannot compile vertex shader\n"
              << infoLog << std::endl;
  }

  // fragment shader
  GLuint fragment_shader = glCreateShader(GL_FRAGMENT_SHADER);
  glShaderSource(fragment_shader, fragment_shader_string_count,
                 &fragment_shader_source, NULL);
  glCompileShader(fragment_shader);

  glGetShaderiv(fragment_shader, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(fragment_shader, sizeof(infoLog), NULL, infoLog);
    std::cout << "Error: Cannot compile fragment shader\n"
              << infoLog << std::endl;
  }

  // create shader program
  GLuint shader_program = glCreateProgram();
  glAttachShader(shader_program, vertex_shader);
  glAttachShader(shader_program, fragment_shader);
  glLinkProgram(shader_program);

  glGetProgramiv(shader_program, GL_COMPILE_STATUS, &success);
  if (!success) {
    glGetShaderInfoLog(shader_program, sizeof(infoLog), NULL, infoLog);
    std::cout << "Error: Cannot link shader program\n" << infoLog << std::endl;
  }

  // cleanup shaders
  glDeleteShader(vertex_shader);
  glDeleteShader(fragment_shader);
  // ==== end shader compile ====

  // clang-format off
  float vertices[] = {
      -0.5f, -0.5f, 0.0f,
      0.5f, -0.5f, 0.0f,
      0.0f,  0.5f, 0.0f
  };

  unsigned int indices[] = {
    0, 1, 2,
  };
  // clang-format on

  GLuint VBO, EBO, VAO;
  glGenBuffers(1, &VBO);
  glGenBuffers(1, &EBO);
  glGenVertexArrays(1, &VAO);

  glBindVertexArray(VAO);

  glBindBuffer(GL_ARRAY_BUFFER, VBO);
  glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

  glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
  glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices,
               GL_STATIC_DRAW);

  GLuint location = 0;
  GLint vector_len = 3;
  glVertexAttribPointer(location, vector_len, GL_FLOAT, GL_FALSE,
                        vector_len * sizeof(float), (void *)0);
  glEnableVertexAttribArray(location);

  // main loop
  while (!glfwWindowShouldClose(window)) {
    processInput(window);

    // ==== render section ====
    glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    float time = glfwGetTime() * 8;
    float red = (sin(time) / 2.0f) + 0.5f;
    float green = (sin(time * 2) / 2.0f) + 0.5f;
    float blue = (sin(time * 4) / 2.0f) + 0.5f;

    // can find location before use the program
    int our_color_location = glGetUniformLocation(shader_program, "our_color");

    // use complied shader program
    glUseProgram(shader_program);

    // pass vec4 value to our_color
    // But updating the uniform should be done after using the shader program
    // glUniform4f(our_color_location, 0.0f, green, 0.0f, 1.0f);

    float our_color[4] = {red, green, blue, 1.0f};
    glUniform4fv(our_color_location, 1, our_color);

    glBindVertexArray(VAO);
    glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, 0);
    // ==== end render section ====

    glfwSwapBuffers(window);
    glfwPollEvents();
  }

  glDeleteVertexArrays(1, &VAO);
  glDeleteBuffers(1, &VBO);
  glDeleteBuffers(1, &EBO);
  glDeleteProgram(shader_program);

  glfwTerminate();
  return 0;
}

void framebuffer_size_callback(GLFWwindow *window, int width, int height) {
  glViewport(0, 0, width, height);
}

void processInput(GLFWwindow *window) {
  if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
    glfwSetWindowShouldClose(window, true);
  }
}

void GLAPIENTRY MessageCallback(GLenum source, GLenum type, GLuint id,
                                GLenum severity, GLsizei length,
                                const GLchar *message, const void *userParam) {
  fprintf(stderr,
          "GL CALLBACK: %s type = 0x%x, severity = 0x%x, message = %s\n",
          (type == GL_DEBUG_TYPE_ERROR ? "** GL ERROR **" : ""), type, severity,
          message);
}
