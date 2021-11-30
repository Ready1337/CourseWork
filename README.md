# Search-for-attractive-sets-of-recurrent-sequences

## Problem: find attractive sets of recurrent sequences

There is no term "attractive set", but there are sets of points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_n,&space;y_n)" title="(x_n,  y_n)" />  to which sequences tend at different values of parameters <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" /> and starting points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_0,&space;y_0)" title="(x_0, y_0)" />

<img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;y_{n&plus;1}&space;=&space;F2(x_n,&space;y_n,&space;p)&space;=&space;p(3x_n&space;&plus;&space;1)y_n(1&space;-&space;y_n)" title="y_{n+1} = F2(x_n, y_n, p) = p(3x_n + 1)y_n(1 - y_n)" />
<img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;x_{n&plus;1}&space;=&space;F1(x_n,&space;y_n,&space;p)&space;=&space;p(3y_n&space;&plus;&space;1)x_n(1&space;-&space;x_n)" title="x_{n+1} = F1(x_n, y_n, p) = p(3y_n + 1)x_n(1 - x_n)" />

By their meaning, these relations allow predicting the behavior of a group of neurons.

## Statements:
* Create a function that calculates <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;x_{n&plus;1}" title="x_{n+1}" /> and <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;y_{n&plus;1}" title="y_{n+1}" /> from the passed <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;x_n,&space;y_n,&space;p" title="x_n, y_n, p" />. To calculate this function, use Namba(https://habr.com/ru/post/484136).<p></p>
* Create a function that calculates the sequence for the transmitted starting points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_0,y_0)" title="(x_0,y_0)" /> and the parameter <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" />.
Calculate the first 10000 members of the sequence, and then write the next 1000 iterations to a file. It is recommended to use numpy and data formats that work with numpy methods.save, numpy.download, numpy.save text, numpy.upload the text. Check that it has not gone to "infinity" (calculations can be stopped if x or y is greater than 1000) or NaN (not a number) has appeared.<p></p>
* Create a function that sets several <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" /> (51 points in the range from 0 to 2) and stores graphs as sets of points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_n,y_n)" title="(x_n,y_n)" />. The parameter value should be clearly indicated on the graphs and in the file names.<p></p>
* Construct a bifurcation diagram. There is an example of a diagram for one-dimensional mapping <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;x_{n&plus;1}=f(x_n,a)" title="x_{n+1}=f(x_n,a)" /> in the bifurcation_on_air.ipynb file. Make it similar, but in a three-dimensional version, where along the vertical axis the value of the parameter <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" /> is in the range from 0 to 2.<p></p>
* Create a function that builds a pool of attractions for a given parameter <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" />. The idea here is as follows: for some parameters, the system comes to a cyclic change, that is, <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_i,y_i)=(5,1)" title="(x_i,y_i)=(5,1)" />, <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_{i&plus;1},y_{i&plus;1})=(1,5)" title="(x_{i+1},y_{i+1})=(1,5)" />, <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_{i&plus;2},y_{i&plus;2})=(5,1)" title="(x_{i+2},y_{i+2})=(5,1)" />, <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_{i&plus;3},y_{i&plus;3})=(1,5)" title="(x_{i+3},y_{i+3})=(1,5)" /> and so on. This is an example of a cycle of length 2. And sometimes it does not come, or it comes to cycles of a different length. It all depends on the starting points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;x_0,y_0" title="x_0,y_0" />. It is necessary to take several points from the square <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;[0,1]\times&space;[0,1]" title="[0,1]\times [0,1]" /> as the starting points and determine what the system has converged to. Depending on this, determine the color for the dots.<p></p></ul>

<b>It should turn out something like this:</b><ul>
![pool](https://ic.wampi.ru/2021/11/18/RISUNOK1.png)</ul>

## Report
The implementation of computer simulation of sequences and graphs can be found in the <b>src</b> folder.

Let's describe the undocumented results that are reflected in the implementation of pool modeling in the form of constant parameters for functions.

* Let's construct a bifurcation diagram with the starting points <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(0.25,&space;0.16)" title="(0.25, 0.16)" /> and the parameter <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" />, varying in the range <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;[0,&space;2]" title="[0, 2]" /> with a step of <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;0.001" title="0.001" /> (The values <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x,&space;y)" title="(x, y)" /> are taken specially, obtained empirically by repeatedly constructing a bifurcation diagram).
<p><b>It turns out the following picture:</b></p>
<a href="https://ibb.co/c3S47H5"><img src="https://i.ibb.co/xLtxR0v/myplot1.png" alt="myplot1" border="0"></a>

* Obviously, it is necessary to choose <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" /> values approximately in the range <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;[0.79,&space;1.08]" title="[0.79, 1.08]" /> for more detailed consideration of the bifurcation diagram. That's what we'll do.
<p><b>It turns out the following picture:</b></p>
<a href="https://ibb.co/9brS7S4"><img src="https://i.ibb.co/8r7tHtx/myplot2.png" alt="myplot2" border="0"></a><br /><a target='_blank' href='https://ru.imgbb.com/'></a>
At this stage, the bifurcation itself is already clearly visible.

<p></p>

* Now let's move on to the construction of the pool of attraction, more precisely to its "cross sections" for different parameters <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;p" title="p" />.

The phrase "cross-section" is not quite suitable only due to the fact that there is no single starting point with specific coordinates <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;(x_0,&space;y_0)" title="(x_0, y_0)" /> when constructing the pool of attraction. On the contrary, the range of the starting points of their direct product <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;[0,&space;1]&space;\times&space;[0,&space;1]" title="[0, 1] \times [0, 1]" /> with a sufficient step is used. However, the phrase helps to understand what happens during the initial acquaintance.

<b>The following graphs are obtained for the parameters <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;[0.79,&space;0.9]" title="[0.79, 0.9]" /> with a step of <img src="https://latex.codecogs.com/png.latex?\inline&space;\bg_white&space;0.01" title="0.01" />:</b>
<a href="https://ibb.co/0D34n3V"><img src="https://i.ibb.co/BzRWfRK/79.png" alt="79" border="0"></a>
<a href="https://ibb.co/8rJphzk"><img src="https://i.ibb.co/bsxZfHt/80.png" alt="80" border="0"></a>
<a href="https://ibb.co/GnvqhwS"><img src="https://i.ibb.co/YP7xr9s/81.png" alt="81" border="0"></a>
<a href="https://ibb.co/9bnw1CF"><img src="https://i.ibb.co/x1hmBRp/82.png" alt="82" border="0"></a>
<a href="https://ibb.co/S6VDdB5"><img src="https://i.ibb.co/D1wP8Qz/83.png" alt="83" border="0"></a>
<a href="https://ibb.co/NKHnx2k"><img src="https://i.ibb.co/vkKv14r/84.png" alt="84" border="0"></a>
<a href="https://ibb.co/C5ygxrV"><img src="https://i.ibb.co/VWGRXKM/85.png" alt="85" border="0"></a>
<a href="https://ibb.co/hKCdHHv"><img src="https://i.ibb.co/jLHwGGF/86.png" alt="86" border="0"></a>
<a href="https://ibb.co/QCYgkMC"><img src="https://i.ibb.co/jW3NzDW/87.png" alt="87" border="0"></a>
<a href="https://ibb.co/w4cdGmw"><img src="https://i.ibb.co/HqhKw8x/88.png" alt="88" border="0"></a>
<a href="https://ibb.co/26BK8wv"><img src="https://i.ibb.co/QcGm8ZP/89.png" alt="89" border="0"></a>
<a href="https://ibb.co/2czDg9f"><img src="https://i.ibb.co/wpn9Mkx/90.png" alt="90" border="0"></a>
