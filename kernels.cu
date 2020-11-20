extern "C" __global__ void add(float *a, float *b) { 
}

// Strange, but valid formatting
        extern "C"     __global__    void       add2(
                        float *  a, 
                        float *b) { 
}

// This function gets called with too few arguments
extern "C" __global__ void toofew(float *a, float *b) { 
}

// This function gets called with too many arguments
extern "C" __global__ void toomany(float *a, float *b, int *c) { 
}

// Extern block containing several functions
extern "C" {
        __global__ void block_toofew(float *a, float *b) { }
        __global__ void block_toomany(float *a, float *b, int *c) {  }
}
