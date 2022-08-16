# APLAS2022

<h1 id="intro"> Introduction </h1>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the state-of-the-art [NATE](https://arxiv.org/pdf/1708.07583.pdf)'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p>

<h2 id="gd"> Environment Installation & Getting Started </h2>
<p> We provide an easy-to-use <a href="">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE's virtual machine</a>, for people who want to reproduce NATE's experiments under the new metric. The user and password are both "<em>nate</em>". The VM should already have everything installed. You just need to activate the python virtualenv using the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
<p>As the VM is now ready to reproduce the results, let's recall NATE's experiments:</p>
<ul>
  <li>Impact of contextual features on blame/diagnosis accuracy</li>
  <li>Blame/Diagnosis accuracy of different techniques</li>
</ul>
<p>The commands of  running these experiments are given in the following sections. <b>Notice: It is possible that the accuracy of the same command <em>differ slightly</em> every time you execute it.</b></p>



