#include <stdio.h>

#define BUF_SIZE 256

int main(void) {
  FILE *fp = fopen("data.txt", "r");
  if (fp == NULL) {
    printf("File open error!\n");
    return 0;
  }

  int n, m;

  // read file from last to find integer m
  fseek(fp, -1, SEEK_END);
  while (fgetc(fp) != '\n') {
    fseek(fp, -2, SEEK_CUR);
  }
  fscanf(fp, "%d", &m);

  // read file from first to find integer n
  fseek(fp, 0, SEEK_SET);
  fscanf(fp, "%d", &n);
  // truncate next newline
  fseek(fp, 1, SEEK_CUR);

  // read next line until reach the last line
  int line = 1;
  char buf[BUF_SIZE];

  while (fgets(buf, BUF_SIZE, fp) != NULL) {
      printf("%s", buf);
    // // if line is m, skip, else print
    // if (line != m) {
    //   printf("%s", buf);
    // }

    // // increase line number if meet '\n'
    // if (buf[0] == '\n') {
    //   line++;
    // }

    // // meet the last line, break
    // if (line == n) {
    //   break;
    // }
  }

}
