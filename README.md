<h1 id="header"> APLAS2022 </h1>

<h1 id="intro"> Introduction </h1>
<h2> Paper Abstract </h2>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the <a href="https://arxiv.org/pdf/1708.07583.pdf">state-of-the-art NATE</a>'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p>

<h2> Experiments </h2>
<p>Recall the two main experiments we've done in this work.</p>
<ul>
  <li>Training NLP Language Model,<em> BERT</em>, through different methodologies for type error diagnosis.</li>
  <li><a href="#nate">Redo NATE's experiments under the <em>new metric</em>.</a></li>
</ul>

<h1> Reproducing the Evaluation</h3>
<h2 id="nate"> NATE's experiments under the new metric</h2>
<h3>Environment Installation & Setting up </h3>
<p> We provide an easy-to-use <a href="">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE</a>'s <a href="https://www.dropbox.com/s/b8a7nfwi8loiwvp/nate-artifact.ova?dl=0">virtual machine</a>, for people who want to reproduce NATE's experiments under the new metric. The user and password are both "<em>nate</em>". The VM should already have everything installed. You just need to open the terminal and activate the python virtualenv using the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
<p>As the VM is now ready to reproduce the results, let's recall NATE's experiments:</p>
<ol>
  <li><a href="#features">Impact of contextual features on blame/diagnosis accuracy</a></li>
  <li><a href="#techniques">Blame/Diagnosis accuracy of different techniques</a></li>
</ol>
<p>The commands of running these experiments are given in the following sections. <b>Notice: It is possible that accuracy of the same command <em>differ slightly</em> every time you execute it.</b></p>
<p align="right"><a href="#header">↑Intro</a></p>

---------------------------------
<h3 id="features">   1. Feature Matters </h3>
<br>
<b>LOGISTIC</b>:
<table align="center">
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
<tr><th>sp14->sp14</th><th><b>./loc1414_l.sh</b></th><th><b>./s1414_l.sh</b></th><th><b>./c1414_l.sh</b></th><th><b>./t1414_l.sh</b></th><th><b>./cs1414_l.sh</b></th><th><b>./ts1414_l.sh</b></th><th><b>./ct1414_l.sh</b></th><th><b>./cts1414_l.sh</b></th></tr>
<tr><th>sp14->fa15</th><th><b>./loc1415_l.sh</b></th><th><b>./s1415_l.sh</b></th><th><b>./c1415_l.sh</b></th><th><b>./t1415_l.sh</b></th><th><b>./cs1415_l.sh</b></th><th><b>./ts1415_l.sh</b></th><th><b>./ct1415_l.sh</b></th><th><b>./cts1415_l.sh</b></th></tr>
<tr><th>fa15->sp14</th><th><b>./loc1514_l.sh</b></th><th><b>./s1514_l.sh</b></th><th><b>./c1514_l.sh</b></th><th><b>./t1514_l.sh</b></th><th><b>./cs1514_l.sh</b></th><th><b>./ts1514_l.sh</b></th><th><b>./ct1514_l.sh</b></th><th><b>./cts1514_l.sh</b></th></tr>
<tr><th>fa15->fa15</th><th><b>./loc1515_l.sh</b></th><th><b>./s1515_l.sh</b></th><th><b>./c1515_l.sh</b></th><th><b>./t1515_l.sh</b></th><th><b>./cs1515_l.sh</b></th><th><b>./ts1515_l.sh</b></th><th><b>./ct1515_l.sh</b></th><th><b>./cts1515_l.sh</b></th></tr>
</table>

<b>MLP-500 model:</b>
<table align="center">
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
<tr><th>sp14->sp14</th><th><b>./loc1414_h.sh</b></th><th><b>./s1414_h.sh</b></th><th><b>./c1414_h.sh</b></th><th><b>./t1414_h.sh</b></th><th><b>./cs1414_h.sh</b></th><th><b>./ts1414_h.sh</b></th><th><b>./ct1414_h.sh</b></th><th><b>./cts1414_h.sh</b></th></tr>
<tr><th>sp14->fa15</th><th><b>./loc1415_h.sh</b></th><th><b>./s1415_h.sh</b></th><th><b>./c1415_h.sh</b></th><th><b>./t1415_h.sh</b></th><th><b>./cs1415_h.sh</b></th><th><b>./ts1415_h.sh</b></th><th><b>./ct1415_h.sh</b></th><th><b>./cts1415_h.sh</b></th></tr>
<tr><th>fa15->sp14</th><th><b>./loc1514_h.sh</b></th><th><b>./s1514_h.sh</b></th><th><b>./c1514_h.sh</b></th><th><b>./t1514_h.sh</b></th><th><b>./cs1514_h.sh</b></th><th><b>./ts1514_h.sh</b></th><th><b>./ct1514_h.sh</b></th><th><b>./cts1514_h.sh</b></th></tr>
<tr><th>fa15->fa15</th><th><b>./loc1515_h.sh</b></th><th><b>./s1515_h.sh</b></th><th><b>./c1515_h.sh</b></th><th><b>./t1515_h.sh</b></th><th><b>./cs1515_h.sh</b></th><th><b>./ts1515_h.sh</b></th><th><b>./ct1515_h.sh</b></th><th><b>./cts1515_h.sh</b></th></tr>
</table>
<b>MLP-10 model:</b>
<table align="center">
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
  <tr><th>sp14->sp14</th><th><b>./loc1414_h10.sh</b></th><th><b>./s1414_h10.sh</b></th><th><b>./c1414_h10.sh</b></th><th><b>./t1414_h10.sh</b></th><th><b>./cs1414_h10.sh</b></th><th><b>./ts1414_h10.sh</b></th><th><b>./ct1414_h10.sh</b></th><th><b>./cts1414_h10.sh</b></th></tr>
<tr><th>sp14->fa15</th><th><b>./loc1415_h10.sh</b></th><th><b>./s1415_h10.sh</b></th><th><b>./c1415_h10.sh</b></th><th><b>./t1415_h10.sh</b></th><th><b>./cs1415_h10.sh</b></th><th><b>./ts1415_h10.sh</b></th><th><b>./ct1415_h10.sh</b></th><th><b>./cts1415_h10.sh</b></th></tr>
<tr><th>fa15->sp14</th><th><b>./loc1514_h10.sh</b></th><th><b>./s1514_h10.sh</b></th><th><b>./c1514_h10.sh</b></th><th><b>./t1514_h10.sh</b></th><th><b>./cs1514_h10.sh</b></th><th><b>./ts1514_h10.sh</b></th><th><b>./ct1514_h10.sh</b></th><th><b>./cts1514_h10.sh</b></th></tr>
<tr><th>fa15->fa15</th><th><b>./loc1515_h10.sh</b></th><th><b>./s1515_h10.sh</b></th><th><b>./c1515_h10.sh</b></th><th><b>./t1515_h10.sh</b></th><th><b>./cs1515_h10.sh</b></th><th><b>./ts1515_h10.sh</b></th><th><b>./ct1515_h10.sh</b></th><th><b>./cts1515_h10.sh</b></th></tr>
</table>
<p>Each command takes about 20 to 30 minutes to output the <em>final accuracy</em>, which is <em>proportional to</em> the number of features that you want the models to focus on.</p>
<p>Using the second rows of the first two tables, you can get something that looks similar to the graph demonstrated below, which reflects the performance of the models <em>trained on sp14</em> and <em>tested on fa15</em>:</p>
<p align="center"><img src="https://user-images.githubusercontent.com/90864900/184788168-0a4017d3-a288-4fb7-a9f1-a23e594f7a1c.png"></p>
You can of course, try other dataset combinations using other rows of the tables.
<p align="right"><a href="#header">↑Intro</a></p>

------------------------------------------
<h3 id="techniques"> 2. Technique matters </h3>
<p>We provide you a python script that you can use to get the diagnosis accuracy of different techniques, which includes <em>decision tree, random forest, Sherrloc</em> and <em>OCaml compiler</em>. Type <pre>python ./computeAccuracy.py</pre> to run the script.
<br>
Some messages will display on the terminal asking you to <em>properly</em> type the technique and dataset you want to use. Do put single or double quotation marks besides you answers as shown in the following example to make sure they can be read by the script:
<pre>
Please properly type the dataset you want to test. ('sp14' or 'fa15'): 'sp14'
Please properly type the technique you wish to use
        'decision-tree'
        'random-forest'
        'sherrloc'
        'ocaml'
: "random-forest"
The accuracy is on its way...
The final accuracy is 38.79%
</pre>

<h3>Conclusion</h3>
Following these instructions, you can get the accuracy of any model/technique used by NATE under the new metric, and be perfectly capable of reproduce similar graphs demonstrated in our paper. As every time you execute the command or the script, the final accuracy may differ slightly, the results you will get is going to look almost identical to us.
</p>
<p align="right"><a href="#header">↑Intro</a></p>
