CC = gcc

CFLAGS = -Wall
CFLAGS += -O0

BINS = dijkstra dijkstra_opt
LIBS = -pthread -lcdsl -L./../synch_implementations -I./../synch_implementations

all: $(BINS)

dijkstra: dijkstra.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

dijkstra_opt: dijkstra_opt.c
	$(CC) $(CFLAGS) -o $@ $< $(LIBS)

clean:
	rm -f *.o *~ $(BINS)
