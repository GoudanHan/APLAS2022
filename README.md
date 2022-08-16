<h1 id="header"> APLAS2022 </h1>

<h1 id="intro"> Introduction </h1>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the <a href="https://arxiv.org/pdf/1708.07583.pdf">state-of-the-art NATE</a>'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p>

<h2 id="gd"> Environment Installation & Getting Started </h2>
<p> We provide an easy-to-use <a href="">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE</a>'s <a href="https://www.dropbox.com/s/b8a7nfwi8loiwvp/nate-artifact.ova?dl=0">virtual machine</a>, for people who want to reproduce NATE's experiments under the new metric. The user and password are both "<em>nate</em>". The VM should already have everything installed. You just need to activate the python virtualenv using the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
<p>As the VM is now ready to reproduce the results, let's recall NATE's experiments:</p>
<ol>
  <li>Impact of contextual features on blame/diagnosis accuracy</li>
  <li>Blame/Diagnosis accuracy of different techniques</li>
</ol>
<p>The commands of running these experiments are given in the following sections. <b>Notice: It is possible that the accuracy of the same command <em>differ slightly</em> every time you execute it.</b></p>
<p align="right"><a href="#header">↑Top</a></p>

---------------------------------
<h3>   1. Feature Matters </h3>
<table align="center" >
  <tr>
    <th></th>
    <th>Local Syn</th>
    <th>+S(ize)</th>
    <th>+C(ontext)</th>
    <th>+T(ype)</th>
    <th>+C+S</th>
    <th>+T+S</th>
    <th>+C+T</th>
    <th>+C+T+S</th>
  </tr>
  <tr>
    <th>sp14->sp14</th>
<th><b>./loc1414_h</b></th><th><b>./s1414_h</b></th><th><b>./c1414_h</b></th><th><b>./t1414_h</b></th><th><b>./cs1414_h</b></th><th><b>./ts1414_h</b></th><th><b>./ct1414_h</b></th><th><b>./cts1414_h</b></th>
  </tr>    <th>sp14->fa15</th>
    <th><b>./loc1415_h</b></th><th><b>./s1415_h</b></th><th><b>./c1415_h</b></th><th><b>./t1415_h</b></th><th><b>./cs1415_h</b></th><th><b>./ts1415_h</b></th><th><b>./ct1415_h</b></th><th><b>./cts1415_h</b></th>
  </tr>
    <th>fa15->sp14</th>
    <th><b>./loc1514_h</b></th><th><b>./s1514_h</b></th><th><b>./c1514_h</b></th><th><b>./t1514_h</b></th><th><b>./cs1514_h</b></th><th><b>./ts1514_h</b></th><th><b>./ct1514_h</b></th><th><b>./cts1514_h</b></th>
  </tr>
    <th>fa15->fa15</th>
    <th><b>./loc1515_h</b></th><th><b>./s1515_h</b></th><th><b>./c1515_h</b></th><th><b>./t1515_h</b></th><th><b>./cs1515_h</b></th><th><b>./ts1515_h</b></th><th><b>./ct1515_h</b></th><th><b>./cts1515_h</b></th>
  </tr>
</table>
<p>Each command takes about 20 to 30 minutes to output the <em>final accuracy</em>, which is proportional to the number of features that you want the models to focus on.</p>
<p>The accuracy you get from these command should look similar to the this graph shown in our paper:</p>
<p align="center"><img src="https://user-images.githubusercontent.com/90864900/184788168-0a4017d3-a288-4fb7-a9f1-a23e594f7a1c.png"></p>
<p align="right"><a href="#header">↑Top</a></p>
