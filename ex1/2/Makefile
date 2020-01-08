CC = gcc

CFLAGS = -Wall
CFLAGS += -O0

BINS = tables tables_opt_exhaustive tables_opt_simplex

all: $(BINS)

tables: tables.c
	$(CC) $(CFLAGS) -o $@ $<

tables_opt_exhaustive: tables_opt_exhaustive.c
	$(CC) $(CFLAGS) -o $@ $<

tables_opt_simplex: tables_opt_simplex.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o tuning_tables_orio_* *.dot *.json *~ $(BINS)
