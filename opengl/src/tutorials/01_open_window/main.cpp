#include <glad/glad.h>

#include <GLFW/glfw3.h>

#include <iostream>

int main() {
  glfwInit();

  // configure glfw using glfwWindowHint
  // see https://www.glfw.org/docs/latest/window.html#window_hints
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

  auto window = glfwCreateWindow(800, 600, "First Window", NULL, NULL);

  if (window == NULL) {
    std::cout << "Failed to create GLFW window" << std::endl;
    glfwTerminate();
    return -1;
  }

  glfwMakeContextCurrent(window);

  // Initialize glad to use opengl
  if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
    std::cout << "Failed to initialize GLAD" << std::endl;
    return -1;
  }

  /**
   * void glViewport(x, y, width, height)
   * lower left position x, y, window width, height
   *
   * opengl 내부에서의 좌표 표현은 -1 ~ 1 사이
   * 이 값을 0~800, 0~600으로 매핑해 화면에 그려줌
   * framebuffer_size_callback 함수를 통해 window resize시 viewport를 다시
   * 설정해줄 수 있음
   * ```c
   * void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
   *   glViewport(0, 0, width, height);
   * }
   * glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
   * ```
   */
  glViewport(0, 0, 800, 600);

  // update loop
  while (!glfwWindowShouldClose(window)) {
    // swap front buffer(current displayed frame) to back buffer (next frame)
    glfwSwapBuffers(window);
    // poll key event, mouse event, etc...
    glfwPollEvents();
  }

  // cleanup function
  glfwTerminate();
  return 0;
}
