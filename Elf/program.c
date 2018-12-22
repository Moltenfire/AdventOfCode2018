static int r0, r1, r2, r3, r4, r5;

#include <stdio.h>

int main(int argc, char *argv[])
{
    r0 = r1 = r2 = r3 = r4 = r5 = 0;
    for(;;r1++)
    switch (r1) {
    case 0: r1 = r1 + 16; break;
    case 1: r3 = 1; break;
    case 2: r5 = 1; break;
    case 3: r4 = r3 * r5; break;
    case 4: r4 = r4 == r2 ? 1 : 0; break;
    case 5: r1 = r4 + r1; break;
    case 6: r1 = r1 + 1; break;
    case 7: r0 = r3 + r0; break;
    case 8: r5 = r5 + 1; break;
    case 9: r4 = r5 > r2 ? 1 : 0; break;
    case 10: r1 = r1 + r4; break;
    case 11: r1 = 2; break;
    case 12: r3 = r3 + 1; break;
    case 13: r4 = r3 > r2 ? 1 : 0; break;
    case 14: r1 = r4 + r1; break;
    case 15: r1 = 1; break;
    case 16: r1 = r1 * r1; break;
    case 17: r2 = r2 + 2; break;
    case 18: r2 = r2 * r2; break;
    case 19: r2 = r1 * r2; break;
    case 20: r2 = r2 * 11; break;
    case 21: r4 = r4 + 7; break;
    case 22: r4 = r4 * r1; break;
    case 23: r4 = r4 + 13; break;
    case 24: r2 = r2 + r4; break;
    case 25: r1 = r1 + r0; break;
    case 26: r1 = 0; break;
    case 27: r4 = r1; break;
    case 28: r4 = r4 * r1; break;
    case 29: r4 = r1 + r4; break;
    case 30: r4 = r1 * r4; break;
    case 31: r4 = r4 * 14; break;
    case 32: r4 = r4 * r1; break;
    case 33: r2 = r2 + r4; break;
    case 34: r0 = 0; break;
    case 35: r1 = 0; break;
    default: printf("[%d,%d,%d,%d,%d,%d]\n", r0, r1, r2, r3, r4, r5); return 0;
    }
}
