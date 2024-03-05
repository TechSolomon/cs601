// https://github.com/olawlor/cs601/blob/master/orcjit/examples/input.c
long jitentry(long x) {
  if (x > 5) {
    x = x * 10;
  }
  return x;
}
