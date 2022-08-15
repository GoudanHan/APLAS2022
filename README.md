# APLAS2022

<h1 id="intro"> Introduction </h1>
<p>
Strong type system helps programmers to eliminate many errors without much burden of supplying type annotations. However, this flexibility makes it highly non-trivial to diagnose the failure mode, especially for novice programmers.  Compared to classic constraint solving and optimization based approaches, the data-driven approach has shown great promise of identifying the root cause of type errors with high accuracy. Instead of relying on hand-engineered features, this work explores natural language models for type error localization, which can be trained in an end-to-end fashion without requiring any features. We demonstrate that, for novice type error diagnosis, language model based approach significantly outperforms the previous state-of-the-art data-driven approach. Specifically, our transformer model could predict type errors correctly 62% of the time, outperforming the state-of-the-art [NATE](https://arxiv.org/pdf/1708.07583.pdf)'s data-driven model by 11%, in a more rigorous metric of accuracy measurement. Furthermore, we also apply structural probe to explain the performance difference of different language models. 
</p>

<h2 id="gd"> Environment Installation & Getting Started </h2>
<p> We provide an easy-to-use <a href="">VM</a>, an updated version of <a href="https://github.com/ucsd-progsys/nate">NATE's virtual machine</a>, for people who want to reproduce the diagnosis accuracies of NATE's models under the new metric. The user and password are both "nate". The VM should already have everything you need installed. You just need to activate the python virtualenv with the following commands:</b>
</p>

```
cd ~/Desktop/nate/
source .venv/bin/activate
```
<p align="center"><img src="https://user-images.githubusercontent.com/90864900/184725729-f836ee33-9cd0-4124-ad52-83c5c986d088.png">
</p>



