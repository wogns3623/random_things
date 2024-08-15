#version 330 core

// // input from vertex shader
// in vec4 vertex_color;

// input from application
uniform vec4 our_color;

out vec4 frag_color;

void main() {
  frag_color = our_color;
}
