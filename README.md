<h1 id="header"> APLAS2022 </h1>

<h1 id="intro"> Artifacts </h1>
<!-- <h2> Paper Abstract </h2>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the <a href="https://arxiv.org/pdf/1708.07583.pdf">state-of-the-art NATE</a>'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p> -->
<ul>
  <li><a href="#training">Kaggle Notebooks </a>
    <ol>
      <li>Our machine learning models</li>
      <li>NATE's dataset, SP14 and FA15</li>
      <li><em>Dataset</em>: 20k OCaml programs written by beginners</li>
      <li><em>Dataset</em>: 350k OCaml programs from GitHub</li>
    </ol>
  </li>
  <li><a href="#nate">Our Virtual Machine</a>
    <ol>
      <li>NATE's models under the new metric</li>
      <li>Scripts and commands to get models' blame/diagnosis accuracy</li>
    </ol>
  </li>
  <li><a href="#graph">Scripts for Generating Graphs</a></li>
</ul>
<h2> Experiments </h2>
<p>Recall the two main experiments we've done in this work.</p>
<ul>
  <li><a href="#training">Training NLP Language Model,<em> BERT</em>, through different methodologies for type error diagnosis.</a></li>
  <li><a href="#nate">Redo NATE's experiments under the <em>new metric</em>.</a></li>
</ul>

<h2 id="training">Training NLP Language Model, BERT, through different methodologies for type error diagnosis.</h2>
<h3>Environment Introduction & Setting up </h3>
For this experiment, we used Kaggle notebook and its GPU accelerator to train the following models: 
<ul>
  <li>BERT-small</li>
  <li>BERT-medium</li>
  <li>BERT-base</li>
  <li>CodeBERT</li>
  <li>BERT-large pre-trained on OCaml</li>
</ul>
You can find the notebooks here: <a href="https://www.kaggle.com/code/tianyuhan2/typeinference/edit">The notebook to train BERT-small, BERT-base, BERT-large, and CodeBERT</a>, <a href="https://www.kaggle.com/code/tianyuhan2/typeerrorinference0611/edit">The notebook to train OCamlBERT-large</a>, and <a href="https://www.kaggle.com/allengeng123/inference/edit">The notebook to directly calculate accruacy of models</a>.

<h3>Turn on GPU</h3>
Once you opened the notebook, on the right side, you can change the accelerator to GPU. Then you are all set to run the notebook! Just click on the Run All in the top menu bar and then the notebook will prompt you to enter a model's name. For now, the notebook supports training bert-small, bert-base, bert-large, codebert, and OCaml bert.



<h3>Output</h3>
After the notebook finishes running, you can see the trained model files on the right side under the output directory (/kaggle/working). You can find the links to the models <a href="https://huggingface.co/GoudanHan"> here</a>.


<h2 id="nate"> NATE's experiments under the new metric</h2>
<h3>Environment Installation & Setting up </h3>
<p> We provide an easy-to-use <a href="https://www.dropbox.com/s/nasq90j0p7jukbf/nate.ova?dl=0">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE</a>'s <a href="https://www.dropbox.com/s/b8a7nfwi8loiwvp/nate-artifact.ova?dl=0">virtual machine</a>, for people who want to reproduce NATE's experiments under the new metric. The user and password are both "<em>nate</em>".</p>
<p>The VM should already have everything installed; however, it is possible that the graphical user interface of the VM fails to launch. We encountered the same issue while working on NATE's VM. The good news is you just need the terminal to run the experiments. Press
<b><em>Alt</em> and <em>F3</em></b> together if no display or black screen, then you should see the terminal open.
To activate the python virtualenv, type in the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
---------------------------------
<p>VM is now ready to reproduce the results. The commands of running the experiments are given in the following sections. <b>Notice: It is possible that accuracy of the same command <em>differ slightly</em> every time you execute it.</b></p>
<p>For models, <em>LOGISTIC</em>, <em>MLP-10</em> and <em>MLP-500</em>. We provide you commands for getting the new accuracy of the three ML models used by NATE. Each command takes about <em>10 to 30 minutes</em> to output the <em>final accuracy</em>, which relates to the number of features that you want the model to focus on.</p>
<table align="center">
  <tr>
    <th></th>
    <th>SP14->SP14</th>
    <th>SP14->FA15</th>
    <th>FA15->SP14</th>
    <th>FA15->FA15</th>
 </tr>
 <tr>
    <th>LOGISTIC</th>
    <th>./cts1414_l.sh</th>
    <th>./cts1415_l.sh</th>
    <th>./cts1514_l.sh</th>
    <th>./cts1515_l.sh</th>
 </tr>
 <tr>
    <th>MLP-10</th>
    <th>./cts1414_l.sh</th>
    <th>./cts1415_l.sh</th>
    <th>./cts1514_l.sh</th>
    <th>./cts1515_l.sh</th>
 </tr>
 <tr>
    <th>MLP-500</th>
    <th>./cts1414_l.sh</th>
    <th>./cts1415_l.sh</th>
    <th>./cts1514_l.sh</th>
    <th>./cts1515_l.sh</th>
 </tr>
</table>
<p>As NATE claims that <b>"+C(ontext)+T(ype)+S(ize)"</b> is the most powerful feature combination in error blaming. Hence, these three are the features we use for NATE's models in all experiments of this work.</p>
<p>We provide you a python script to get diagnosis/blaming accuracy of NATE's other models including <em>decision tree, random forest, Sherrloc</em> and <em>OCaml compiler</em>. Type <pre>python ./computeAccuracy.py</pre> to run the script.
<br>
Some messages will display on the terminal asking you to <em>properly</em> type the technique and dataset you want to use. Do <b>put</b> <em>single or double quotation marks</em> besides you answers as shown in the following example to make sure they can be read by the script:
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

<h2 id="graph">Graphs && Conclusion</h2>
<p>Following the above instructions, you can get the accuracy of any model used by NATE under <em>the new metric</em>, and be perfectly capable of reproduce similar graphs demonstrated in our paper. As every time you execute the command or the script, the final accuracy may differ slightly,but the results you will get is going to look <b>almost identical</b> to us. For those who are interested in our graphs and data, you can find the following Python scripts in our artifact submission, which the names of them corresponds to the figures 5 to 7 in our paper. 
</p>
<ul>
  <li><em>Accuracy of Type Error Localization Techniques.py</em></li>
  <li><em>Impact of type error threshold on blame accuracy.py</em></li>
  <li><em>Impacts on training loss.py</em></li>
</ul>
<p align="right"><a href="#header">↑Intro</a></p>
