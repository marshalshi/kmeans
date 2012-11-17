the code is very simple in order to finish several k-means algorithm.

about the initial function of kmeans, i use random, k-center and k-means++.

the file "a", "aa" and "gau" is the test file.
this code just for 2-D points.

how to use:
>python2 gui.py

at last, the final result will be store in filename+'cluster'. e.g. your file name is "m", the result will go into file "mcluser".
in addition, i use subprocess.Popen to open the "mcluster" after getting the result. but in it, i use a shell command "gedit XXX" to open it.
if ur OS(linux/unix) has installed gedit, u can run it. but for windows/mac, i have no idea, because i don't use them. u can try it by urself,or change the code (in main.py).

(because i use the pylab in order to draw the graph, the running time of the code is very long. 
the running time of file "gau" which has 5000 points is around 30s, but we can get the k cluster about 7s.)