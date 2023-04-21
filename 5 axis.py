import keyboard

axis_x = 0
axis_y = 0
axis_z = 0
axis_w = 0
axis_v = 0

l = axis_x
h = axis_y
w = axis_z
nX = axis_w
emF = axis_v




for i in range(10**1000):
 if keyboard.is_pressed('w'):
    l = l + 1
 elif keyboard.is_pressed('d'):
    h = h + 1
 elif keyboard.is_pressed('q'):
    w = w + 1
 elif keyboard.is_pressed('z'):
    nX = nX + 1
 elif keyboard.is_pressed('r'):
    emF = emF + 1
 elif keyboard.is_pressed('s'):
    l = l - 1
 elif keyboard.is_pressed('a'):
    h = h - 1
 elif keyboard.is_pressed('e'):
    w = w - 1
 elif keyboard.is_pressed('x'):
    nX = nX - 1
 elif keyboard.is_pressed('f'):
    emF = emF - 1
 coord_1d = [l]
 coord_2d = [l, h]
 coord_3d = [l, w, h]
 coord_4d = [l, w, h, nX]
 coord_5d = [l, w, h, nX, emF]
 print(f'\r{str(coord_5d)}', end='')
 f = open("axis_v.txt", "w")
 f.write(str(emF))
 f.close()
 f = open("axis_w.txt", "w")
 f.write(str(nX))
 f.close()
 f = open("axis_x.txt", "w")
 f.write(str(h))
 f.close()
 f = open("axis_y.txt", "w")
 f.write(str(l))
 f.close()
 f = open("axis_z.txt", "w")
 f.write(str(w))
 f.close()