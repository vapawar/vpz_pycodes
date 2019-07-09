tria =[]

for row in range(12):
   for col in range(row+1):
      if col == 0:
         tria.append([1])
      elif col == row:
         tria[row].append(1)
      else:
         tria[row].append(tria[row-1][col]+tria[row-1][col-1])

for row in tria:
   nvals = len(row)
   spaces = (80 - 5 * nvals)/2
   paddington = " " * spaces
   bear = ""
   for val in row:
      bear += "%5x" % val
   print paddington + bear

raw_input()
