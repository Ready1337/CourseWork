# Search-for-attractive-sets-of-recurrent-sequences

There is no term "attractive set", but there are sets of points (x_n, y_n) to which sequences tend at different values of parameters p and starting points (x_0, y_0)

$\[x_{n+1} = F1(x_n, y_n, p) = p(3y_n + 1)x_n(1 - x_n)\]$
$\[y_{n+1} = F2(x_n, y_n, p) = p(3x_n + 1)y_n(1 - y_n)\]$

By their meaning, these relations allow predicting the behavior of a group of neurons.

<b>Problem statements:</b>
* Create a function that calculates x_(n+1) and y_(n+1) from the passed x_n, y_n, p. To calculate this function, use Namba(https://habr.com/ru/post/484136).<p></p>
* Create a function that calculates the sequence for the transmitted starting points (x_0,y_0) and the parameter p.
Calculate the first 10000 members of the sequence, and then write the next 1000 iterations to a file. It is recommended to use numpy and data formats that work with numpy methods.save, numpy.download, numpy.save text, numpy.upload the text. Check that it has not gone to "infinity" (calculations can be stopped if x or y is greater than 1000) or NaN (not a number) has appeared.<p></p>
* Create a function that sets several p (51 points in the range from 0 to 2) and stores graphs as sets of points {(x_n,y_n)}. The parameter value should be clearly indicated on the graphs and in the file names.<p></p>
* Construct a bifurcation diagram. There is an example of a diagram for one-dimensional mapping x_(n+1)=f(x_n,a) in the bifurcation_on_air.ipynb file. Make it similar, but in a three-dimensional version, where along the vertical axis the value of the parameter p is in the range from 0 to 2.<p></p>
* Create a function that builds a pool of attractions for a given parameter p. The idea here is as follows: for some parameters, the system comes to a cyclic change, that is, 
```math
(x_i,y_i)=(5,1), (x_(i+1),y_(i+1))=(1,5), (x_(i+2),y_(i+2))=(5,1), (x_(i+3),y_(i+3))=(1,5)
```
<ul>and so on. This is an example of a cycle of length 2. And sometimes it does not come, or it comes to cycles of a different length. It all depends on the starting points x_0,y_0. It is necessary to take several points from the square [0,1] ×[0,1] as the starting points and determine what the system has converged to. Depending on this, determine the color for the dots.<p></p></ul>

<b>It should turn out something like this:</b><ul>
![pool](https://ic.wampi.ru/2021/11/18/RISUNOK1.png)</ul>
