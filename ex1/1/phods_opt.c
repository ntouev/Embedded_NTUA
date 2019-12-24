/*Parallel Hierarchical One-Dimensional Search for motion estimation*/
/*Initial algorithm - Used for simulation and profiling             */

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define N 144     /*Frame dimension for QCIF format*/
#define M 176     /*Frame dimension for QCIF format*/
#define p 7       //Search space. Restricted in a [-p,p] region around the
                  //original location of the block.
int B;

#define FOR_LOOP_I(i)\
    distx = 0;\
    disty = 0;\
\
    /*For all pixels in the block*/\
    for(k=0; k<B; k++)\
    {\
        for(l=0; l<B; l++)\
        {\
            p1 = current[B*x+k][B*y+l];\
\
            if((B*x + __vectors_x__ + i + k) < 0 ||\
            (B*x + __vectors_x__ + i + k) > (N-1) ||\
            (B*y + __vectors_x__ + l) < 0 ||\
            (B*y + __vectors_x__ + l) > (M-1))\
            {\
                p2 = 0;\
            } else {\
                p2 = previous[B*x+__vectors_x__+i+k][B*y+__vectors_x__+l];\
            }\
\
            if((B*x + __vectors_x__ + k) <0 ||\
            (B*x + __vectors_x__ + k) > (N-1) ||\
            (B*y + __vectors_x__ + i + l) < 0 ||\
            (B*y + __vectors_x__ + i + l) > (M-1))\
            {\
                q2 = 0;\
            } else {\
                q2 = previous[B*x+__vectors_x__+k][B*y+__vectors_x__+i+l];\
            }\
\
            distx += abs(p1-p2);\
            disty += abs(p1-q2);\
        }\
    }\
\
    if(distx < min1)\
    {\
        min1 = distx;\
        bestx = i;\
    }\
\
    if(disty < min2)\
    {\
        min2 = disty;\
        besty = i;\
    }\

#define FOR_LOOP_S(s)\
    min1 = 255*B*B;\
    min2 = 255*B*B;\
\
    FOR_LOOP_I(-s);\
    FOR_LOOP_I(0);\
    FOR_LOOP_I(s);\
\
    __vectors_x__ += bestx;\
    __vectors_x__ += besty;

void read_sequence(int current[N][M], int previous[N][M])
{
    FILE *picture0, *picture1;
    int i, j;

    if((picture0=fopen("akiyo0.y","rb")) == NULL)
    {
        printf("Previous frame doesn't exist.\n");
        exit(-1);
    }

    if((picture1=fopen("akiyo1.y","rb")) == NULL)
    {
        printf("Current frame doesn't exist.\n");
        exit(-1);
    }

    /*Input for the previous frame*/
    for(i=0; i<N; i++)
    {
        for(j=0; j<M; j++)
        {
            previous[i][j] = fgetc(picture0);
        }
    }

    /*Input for the current frame*/
    for(i=0; i<N; i++)
    {
        for(j=0; j<M; j++)
        {
            current[i][j] = fgetc(picture1);
        }
    }

    fclose(picture0);
    fclose(picture1);
}


void phods_motion_estimation(int current[N][M], int previous[N][M],
    int vectors_x[N/B][M/B],int vectors_y[N/B][M/B])
{
    double time;
    struct timeval ts,tf;
    gettimeofday(&ts,NULL);
    int x, y, i, j, k, l, p1, p2, q2, distx, disty, S, min1, min2, bestx, besty;

    distx = 0;
    disty = 0;

    /* Initialize the vector motion matrices*/
    for(i=0; i<N/B; i++)
    {
        for(j=0; j<M/B; j++)
        {
            vectors_x[i][j] = 0;
            vectors_y[i][j] = 0;
        }
    }

    /* For all blocks in the current frame
     * Loop unrolled. s and i take fixed values, not variable.
     */
    for(x=0; x<N/B; x++)
    {
        for(y=0; y<M/B; y++)
        {
            int __vectors_x__ = vectors_x[x][y];
            FOR_LOOP_S(4);
            FOR_LOOP_S(2);
            FOR_LOOP_S(1);
        }
    }
    gettimeofday(&tf,NULL);
    time=(tf.tv_sec-ts.tv_sec)+(tf.tv_usec-ts.tv_usec)*0.000001;
    printf("%lf\n", time);
}

int main(int argc, char **argv)
{
    if (argc == 1)
    {
        B = 16;
    }
    else if (argc == 2)
    {
        B = atoi(argv[1]);
    }
    else
    {
        printf("Usage: ./phods_opt block_size\n");
        exit(1);
    }

    int current[N][M], previous[N][M], motion_vectors_x[N/B][M/B],
    motion_vectors_y[N/B][M/B], i, j;

	read_sequence(current,previous);
    phods_motion_estimation(current,previous,motion_vectors_x,motion_vectors_y);

    return 0;
}
