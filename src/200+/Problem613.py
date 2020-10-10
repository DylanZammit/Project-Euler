###MATHEMATICA
# P[x_, y_] := 
#  ArcCos[(x^2 + y^2 - 3 x - 4 y)/
#     Sqrt[(x^2 + y^2) ((x - 3)^2 + (y - 4)^2)]]/360
# Integrate[P[x, y], {x, 0, 3}, {y, 0, 4/3 x}]/6
# With[{d = 
#    N[(12 \[Pi] + 32 Log[2] + 9 Log[3] - 25 Log[5])/(4320 \[Degree]), 
#     10]}, Defer[d \[Degree]]]