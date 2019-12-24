CC = gcc

CFLAGS = -Wall
CFLAGS += -O0

BINS = phods phods_opt phods_opt_2dimensions

all: $(BINS)

phods: phods.c
	$(CC) $(CFLAGS) -o $@ $<

phods_opt: phods_opt.c
	$(CC) $(CFLAGS) -o $@ $<

phods_opt_2dimensions: phods_opt_2dimensions.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o *~ $(BINS)
